import streamlit as st
import page1
import page2
import page3
import edit
from streamlit_navigation_bar import st_navbar


def home_page():
    # Set the title of the app
    st.title("GradeSmart.AI", anchor=False)    
    
    # Display options for navigation
    st.header("Your AI companion to richer and faster feedback on student tests", anchor=False)
    st.subheader("Choose an option to proceed:", anchor=False)


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
    st.sidebar.button("Home", type="primary")
    
    if st.sidebar.button("Upload Student Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_student_answer"
        st.rerun()
    
    if st.sidebar.button("Upload Examiner Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_teacher_answer"
        st.rerun()
    
    if st.sidebar.button("Evaluate", type="primary"):
        st.session_state.current_page = "evaluate_page"
        st.rerun()
    
    # Function to place the button at the bottom
    # def add_button_to_sidebar():
    #     st.markdown(
    #         """
    #         <style>
    #             .bottom-button {
    #                 position: absolute;
    #                 bottom: 0;
    #                 width: 100%;
    #             }
    #         </style>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    #     st.sidebar.markdown(
    #         """
    #         <div class="bottom-button">
    #             <form action="#">
    #                 <button type="submit">Bottom Button</button>
    #             </form>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    

    # # Add the button at the bottom
    # add_button_to_sidebar()










    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Upload Student's Answers Sheets"):
            st.session_state.current_page = "upload_student_answer"
            st.rerun()

    with col3:
        if st.button("Upload Examiner's Answer Sheets"):
            st.session_state.current_page = "upload_teacher_answer"
            st.rerun()

    with col5:
        if st.button("Obtain rich, personalised feedback"):
            st.session_state.current_page = "evaluate_page"
            st.rerun()
    
    st.divider() # Divider for spacing

    # Footer buttons: Logout 
    col6 = st.container()
    with col6:
        if st.button("Logout"):
            st.info("Logout functionality will be implemented later.")



# Main function to manage page navigation
def main():
    st.set_page_config(layout="wide", page_title="GradeSmart.AI")
    
    # st_navbar(["GradeSmart.AI", "Your AI companion to richer and faster feedback on student tests"])
    

    if "current_page" not in st.session_state:
        st.session_state.current_page = "home_page"

    if st.session_state.current_page == "home_page":
        home_page()
    
    elif st.session_state.current_page == "upload_student_answer":
        page1.student_pdf()
        
    elif st.session_state.current_page == "upload_teacher_answer":
        page2.examiner_pdf()
    
    elif st.session_state.current_page == "edit_teacher_answer":
        edit.edit_page()

    elif st.session_state.current_page == "evaluate_page":
        page3.evaluate_result()


# Main entry point for the app
if __name__ == "__main__":
    main()

