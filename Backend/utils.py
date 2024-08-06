import os
import io
from pymupdf import Document
from typing import List
from PIL import Image
import pandas as pd
import google.generativeai as genai
genai.configure(api_key=os.environ["API_KEY"])


VISION_PROMPT = 'Extract question-answers from the given images in this JSON schema : {"Q1": "A1", "Q2": "A2", "Q3": "A3", "Q4(i)": "A4(i)", ...}.'
EVALUATION_PROMPT = """\
You are a class 6 science teacher looking to grade the answer sheet of a student.

This comparison is case insensitive. \
Grade the answers taking help from the given guidelines on a scale of 0 to 10, 0 being completely incorrect and 10 being completely correct. \
Guidelines provide expected answers which students may not follow completely, use your judgement to grade them accordingly.

Your response must follow this JSON schema :
{
    "Q1": {"reason_for_difference": "Reason", "reason_for_similarity": "Reason", "assigned_score": "Score"},
    "Q2": {"reason_for_difference": "Reason", "reason_for_similarity": "Reason", "assigned_score": "Score"},
    ...
}
"""


def crop_image_with_overlap(images: List[Image.Image], num_crops: int, overlap_percentage: float) -> List[Image.Image]:
    cropped_images = []
    for image in images:
        width, height = image.size

        step = (1 - overlap_percentage / 100)
        crop_height = int(height / ((num_crops - 1) * step + 1))

        crops = []
        for i in range(num_crops):
            start_y = int(i * crop_height * step)
            end_y = min(height, start_y + crop_height)
            crops.append((0, start_y, width, end_y))
        
        for i, crop in enumerate(crops):
            cropped_image = image.crop(crop)
            cropped_images.append(cropped_image)
            
    return cropped_images


def extract_images(pdf: Document|None, crop: bool = True, num_crops: int|None = 3, overlap_percentage: float|None = 20) -> List[Image.Image]:
    images = []
    if pdf:
        for page in pdf:
            pix = page.get_pixmap()
            img_bytes = pix.tobytes("jpg")
            img = Image.open(io.BytesIO(img_bytes))
            images.append(img)
        if crop:
            images = crop_image_with_overlap(images=images, num_crops=num_crops, overlap_percentage=overlap_percentage)
    return images


def clean_question_number(question_number: str) -> str:
    return question_number.replace("q", "Q").replace(" ", "")


def read_images(images: List[Image.Image], model_name: str = "gemini-1.5-flash", prompt: str = VISION_PROMPT) -> pd.DataFrame:
    contents = []
    contents = images
    contents.append(prompt)
    model = genai.GenerativeModel(model_name=model_name, generation_config={"response_mime_type": "application/json"})
    response = model.generate_content(contents)
    response = eval(response.text.replace("null", "\"\""))
    student_answers = []
    for question, answer in response.items():
        student_answers.append({"cleaned_question_number": question, "Student Answer": answer})
    df = pd.DataFrame(student_answers)
    df["cleaned_question_number"] = df["cleaned_question_number"].apply(clean_question_number)
    return df


def compare_objectives(type: str, guideline: str, student_answer: str) -> int:
    if type == "Objective":
        return 1 if guideline.upper()[0] == student_answer.upper()[0] else 0


def compare_subjectives(subjectives_df: pd.DataFrame, model_name: str = "gemini-1.5-flash", prompt: str = EVALUATION_PROMPT) -> pd.DataFrame:
    guidelines = {}
    student_answers = {}
    for _, row in subjectives_df.iterrows():
        guidelines[row["cleaned_question_number"]] = row["Guideline"]
        student_answers[row["cleaned_question_number"]] = row["Student Answer"]

    contents = [prompt, f"Guidelines: \n{guidelines}", f"Answer Sheet: \n{student_answers}"]
    model = genai.GenerativeModel(model_name=model_name, generation_config={"response_mime_type": "application/json"})
    response = model.generate_content(contents)
    response = eval(response.text.replace("null", "\"\""))

    results = []
    for question, obj in response.items():
        results.append({
            "cleaned_question_number": question,
            "Score": obj["assigned_score"],
            "Improvement Area": obj["reason_for_difference"],
            "Reason for credits": obj["reason_for_similarity"]
        })
    return pd.DataFrame(results)


def get_score(score_x, score_y) -> int:
    return score_x if pd.notna(score_x) else score_y


def main(df: pd.DataFrame, pdf: Document):
    images = extract_images(pdf)
    vision_response = read_images(images)

    df["cleaned_question_number"] = df["Question Number"].apply(clean_question_number)
    df = pd.merge(left=df, right=vision_response, on="cleaned_question_number")
    df["Score"] = df.apply(lambda x: compare_objectives(x["Question Type"], x["Guideline"], x["Student Answer"]), axis=1)
    
    subjectives_df = df[df["Question Type"] == "Subjective"].copy()
    subjectives_df = subjectives_df[["cleaned_question_number", "Guideline", "Student Answer"]]
    subjectives_df = compare_subjectives(subjectives_df)

    df = pd.merge(df, subjectives_df, how="left", on="cleaned_question_number")
    df['Score'] = df.apply(lambda x: get_score(x["Score_x"], x["Score_y"]), axis=1)
    df.drop(columns=["cleaned_question_number", "Score_x", "Score_y"], inplace=True)
    return df