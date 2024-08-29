import streamlit as st
import fitz

# Function to render a specific page of the PDF
def render_pdf_page(pdf_document, page_number):
    page = pdf_document.load_page(page_number)
    pix = page.get_pixmap()
    img = pix.tobytes()
    return img



def student_pdf():
    st.subheader("Upload Student's Answers", anchor=False)

    # Load CSS from file
    def load_css(file_name):
        with open(file_name) as f:
            return f.read()
    
    # Inject sidebar CSS into the Streamlit app
    st.markdown(f'<style>{load_css("Frontend/CSS/sidebar_styles.css")}</style>', unsafe_allow_html=True)
    st.markdown(f'<style>{load_css("Frontend/CSS/button.css")}</style>', unsafe_allow_html=True)
    st.markdown(f'<style>{load_css("Frontend/CSS/styles.css")}</style>', unsafe_allow_html=True)

    # Add Sidebar into the Streamlit app
    st.sidebar.title("GradeSmart.AI")
    st.sidebar.divider()
    
    if st.sidebar.button("Home", type="primary"):
        st.session_state.current_page = "home_page"
        st.rerun()
    
    st.sidebar.button("Upload Student Answer Sheet", type="primary", use_container_width=True)
    
    if st.sidebar.button("Upload Examiner Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_teacher_answer"
        st.rerun()
    
    if st.sidebar.button("Evaluate", type="primary"):
        st.session_state.current_page = "evaluate_page"
        st.rerun()
    
    


    # Load the Google Fonts stylesheet in Streamlit
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )





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
            if st.button("◀") and st.session_state.page_number > 0:
                st.session_state.page_number -= 1
                st.rerun()
        with col2:
            st.write(f"Page {st.session_state.page_number + 1} of {total_pages}")
        with col3:
            if st.button("▶") and st.session_state.page_number < total_pages - 1:
                st.session_state.page_number += 1
                st.rerun()

    st.divider()

    # Button to navigate to the next Streamlit page
    col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(10)
    with col4:
        if st.button("Home", use_container_width=True):
            st.session_state.current_page = "home_page"
            st.rerun()
    with col13:
        if st.button("Next", use_container_width=True):
            st.session_state.current_page = "upload_teacher_answer"
            st.rerun()


if __name__ == "__main__":
    student_pdf()

