# Subject Evaluation App

## Project Overview

The Subject Evaluation App is a Streamlit-based web application designed for evaluating student answers based on provided guidelines and PDF documents. The app allows users to upload PDF files and CSV data, which are then processed to generate evaluation scores for each student answer. The application features multiple pages for uploading PDFs, reviewing data, and displaying evaluation results.

## Features

- **PDF Upload and Viewing**: Users can upload PDF files and navigate through their pages.
- **CSV Data Upload**: Users can upload CSV files containing student answers and evaluation criteria.
- **Data Processing**: The app processes the uploaded data and PDFs to generate evaluation scores.
- **Interactive Display**: Users can view and interact with the processed data in a grid format.

## Installation

To run this project locally, you need to have Python 3.7+ installed. Follow these steps to set up the project:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/tarcaz-viveksinghania/Subject-Evaluation
   cd subject-evaluation-app
   ```

2. **Create a Virtual Environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    
    # On Windows use  
    `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## Project Structure

- `page1.py`: Main entry point Streamlit application. PDF upload and viewing functionality.
- `page2.py`: Handles CSV data upload and processing.
- `page3.py`: Displays the processed data and evaluation results.
- `utils.py`: Contains utility functions for processing PDFs and data.
- `requirements.txt`: Lists the Python dependencies for the project.

## Usage

### Upload PDF Files

1. Navigate to the first page of the app.
2. Upload the PDF files using the file uploader.
3. Use navigation buttons to view different pages of the PDF.

### Upload CSV Data

1. Go to the next page.
2. Select an option or upload the CSV file containing student answers and guidelines.
3. The CSV data will be displayed and saved for processing.

### View Evaluation Results

1. Navigate to the results page to view the processed evaluation scores.
2. The application will display the evaluation results in an interactive grid format.



## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the Repository.
2. Create a New Branch for your changes.
3. Commit Your Changes.
4. Push to the Branch.
5. Submit a Pull Request.

## Contact

For any questions or feedback, please contact [vivek@tarcaz.com](mailto:your.vivek@tarcaz.com).

#
This `README.md` provides a comprehensive guide to understanding, installing, and using your Streamlit application.
