import streamlit as st
import sys
import os

# Add the project's root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from Backend.utils import main

def evaluate_result():
    st.subheader("Evaluated Result")

    # Load CSS from file
    def load_css(file_name):
        with open(file_name) as f:
            return f.read()

    # Inject sidebar CSS into the Streamlit app
    st.markdown(f'<style>{load_css("Frontend/CSS/sidebar_styles.css")}</style>', unsafe_allow_html=True)
    st.markdown(f'<style>{load_css("Frontend/CSS/button.css")}</style>', unsafe_allow_html=True)


    # Add Sidebar into the Streamlit app
    st.sidebar.title("GradeSmart.AI")
    st.sidebar.divider()
    if st.sidebar.button("Home", type="primary"):
        st.session_state.current_page = "home_page"
        st.rerun()
    
    if st.sidebar.button("Student", type="primary"):
        st.session_state.current_page = "upload_student_answer"
        st.rerun()
    
    if st.sidebar.button("Examiner", type="primary"):
        st.session_state.current_page = "upload_teacher_answer"
        st.rerun()
    st.sidebar.button("Evaluate", type="primary", use_container_width=True)


    # Check if the PDF and DataFrame are stored in session state
    if "pdf_document" in st.session_state and "df" in st.session_state:
        pdf_document = st.session_state.pdf_document        
        df = st.session_state.df
        df.columns = df.columns.str.strip()

        # Use the main function to process the DataFrame and PDF
        result_df = main(df, pdf_document)

        # Display the resulting DataFrame
        st.write("Processed Result:")
        st.dataframe(result_df)
    else:
        st.write("PDF or DataFrame not found. Please go back to the previous pages to upload and prepare the data.")

    # Button to navigate back to the previous page
    if st.button("Go Home"):        
        st.session_state.current_page = "home_page"
        st.rerun()


if __name__ == "__main__":
    evaluate_result()

