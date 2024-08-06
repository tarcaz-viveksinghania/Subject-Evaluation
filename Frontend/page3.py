import streamlit as st
import sys
import os

# Add the project's root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from Backend.utils import main

def display_page3():
    st.title("Page 3")
    st.write("This is the third page of the Streamlit app.")

    # Check if the PDF and DataFrame are stored in session state
    if "pdf_document" in st.session_state and "df" in st.session_state:
        pdf_document = st.session_state.pdf_document        
        df = st.session_state.df
        df.columns = df.columns.str.strip()

        # Use the main function to process the DataFrame and PDF
        result_df = main(df, pdf_document)

        # Display the resulting DataFrame
        st.write("Processed DataFrame:")
        st.dataframe(result_df)
    else:
        st.write("PDF or DataFrame not found. Please go back to the previous pages to upload and prepare the data.")

    # Button to navigate back to the previous page
    if st.button("Go Back to Next Page"):
        st.session_state.current_page = "next_page"
        st.rerun()
