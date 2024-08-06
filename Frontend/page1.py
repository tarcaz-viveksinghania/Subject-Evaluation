import streamlit as st
import fitz  # PyMuPDF
import page2  # Import the next_page module
import page3

st.set_page_config(page_title="Answer Sheet Evaluation", layout="wide")

# Function to render a specific page of the PDF
def render_pdf_page(pdf_document, page_number):
    page = pdf_document.load_page(page_number)
    pix = page.get_pixmap()
    img = pix.tobytes()
    return img

def pdf_viewer():
    st.title("PDF Viewer")

    # File uploader for a single PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        # Store only the PDF content in session state
        st.session_state.uploaded_pdf_content = uploaded_file.getvalue()

        # Open the PDF document and store it in session state
        pdf_document = fitz.open(stream=st.session_state.uploaded_pdf_content, filetype="pdf")
        st.session_state.pdf_document = pdf_document  # Store the PDF document object
        total_pages = pdf_document.page_count

        # Initialize page number in session state if not already
        if "page_number" not in st.session_state:
            st.session_state.page_number = 0

        # Display the current page of the selected PDF
        img = render_pdf_page(pdf_document, st.session_state.page_number)
        st.image(img)

        # Navigation buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Previous Page") and st.session_state.page_number > 0:
                st.session_state.page_number -= 1
                st.rerun()
        with col2:
            st.write(f"Page {st.session_state.page_number + 1} of {total_pages}")
        with col3:
            if st.button("Next Page") and st.session_state.page_number < total_pages - 1:
                st.session_state.page_number += 1
                st.rerun()

    st.divider()

    # Button to navigate to the next Streamlit page
    if st.button("Go to Next Page"):
        st.session_state.current_page = "next_page"
        st.rerun()

# Main function to manage page navigation
def main():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "pdf_viewer"

    if st.session_state.current_page == "pdf_viewer":
        pdf_viewer()
    elif st.session_state.current_page == "next_page":
        page2.display_next_page()
    elif st.session_state.current_page == "page3":
        page3.display_page3()

if __name__ == "__main__":
    main()
