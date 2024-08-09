import streamlit as st
import page1
import page2
import page3



def home_page():
    # Set the title of the app
    st.title("GradeSmart.AI")
    
    # Display options for navigation
    st.header("Welcome to GradeSmart.AI")
    st.subheader("Choose an option to proceed:")


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
    st.sidebar.button("Home", type="primary", use_container_width=True)
    
    if st.sidebar.button("Student", type="primary"):
        st.session_state.current_page = "upload_student_answer"
        st.rerun()
    
    if st.sidebar.button("Examiner", type="primary"):
        st.session_state.current_page = "upload_teacher_answer"
        st.rerun()
    
    if st.sidebar.button("Evaluate", type="primary"):
        st.session_state.current_page = "evaluate_page"
        st.rerun()

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Upload Student's Answers"):
            st.session_state.current_page = "upload_student_answer"
            st.rerun()

    with col3:
        if st.button("Upload Examiner's Answer Sheet"):
            st.session_state.current_page = "upload_teacher_answer"
            st.rerun()

    with col5:
        if st.button("Evaluate Answers"):
            st.session_state.current_page = "evaluate_page"
            st.rerun()
    
    st.divider() # Divider for spacing

    # Footer buttons: Logout and Proceed
    col6 = st.container()
    with col6:
        if st.button("Logout"):
            st.info("Logout functionality will be implemented later.")


# Main function to manage page navigation
def main():
    st.set_page_config(layout="wide", page_title="GradeSmart.AI")

    if "current_page" not in st.session_state:
        st.session_state.current_page = "home_page"

    if st.session_state.current_page == "home_page":
        home_page()
    
    elif st.session_state.current_page == "upload_student_answer":
        page1.student_pdf()
        
    elif st.session_state.current_page == "upload_teacher_answer":
        page2.examiner_pdf()

    elif st.session_state.current_page == "evaluate_page":
        page3.evaluate_result()


# Main entry point for the app
if __name__ == "__main__":
    main()

