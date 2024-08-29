import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder

def examiner_pdf():
    st.subheader("Choose or Upload Examiner's Answer Sheet", anchor=False)

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

    if st.sidebar.button("Upload Student Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_student_answer"
        st.rerun()

    st.sidebar.button("Upload Examiner Answer Sheet", type="primary", use_container_width=True)
    
    if st.sidebar.button("Evaluate", type="primary"):
        st.session_state.current_page = "evaluate_page"
        st.rerun()



    # Initial states
    # disable_file_upload = False
    # disable_selected_option = False

    # Initialize session state variables if they don't exist
    if "df" not in st.session_state:
        st.session_state.df = None
    
    if "upload_df" not in st.session_state:
        st.session_state.upload_df = None




    # Session state to persist the state across re-runs
    if 'disable_file_upload' not in st.session_state:
        st.session_state.disable_file_upload = False
    if 'disable_selected_option' not in st.session_state:
        st.session_state.disable_selected_option = False

    






    
    # Dropdown menu
    options = ["Select", "Option 1", "Option 2", "Option 3"]
    selected_option = st.selectbox("Choose Examiner's Answer Sheet", options, disabled=st.session_state.disable_selected_option)

    # Disable file uploader if a selection is made (other than "Select")
    if selected_option != "Select":
        st.session_state.disable_file_upload = True
    else:
        st.session_state.disable_file_upload = False



    # Show content from the specified CSV if "Option 2" is selected
    if selected_option == "Option 2":
        try:         
            # Load CSV file
            df_question_paper = pd.read_csv("Frontend/Database/Exam Evaluation_ CSVs   - Sample CSV 1_ Examiner's Guidelines .csv")
            
            # Store the uploaded DataFrame in session state
            st.session_state.df = df_question_paper

            st.dataframe(df_question_paper, use_container_width=True, hide_index=True)

        except FileNotFoundError:
            st.error("The file 'Database/Exam Evaluation_ CSVs.csv' was not found.")
        except pd.errors.EmptyDataError:
            st.error("The file is empty.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    if selected_option != "Option 2":
        st.session_state.df = None


    if st.session_state.disable_selected_option == False and st.session_state.disable_file_upload == False:
        st.markdown(
        """
            <div style="display: flex; align-items: center; text-align: center;">
                <hr style="flex-grow: 1; border: 0.2px solid light grey;">
                <span style="margin: 0 10px;">OR</span>
                <hr style="flex-grow: 1; border: 0.2px solid light grey;">
            </div>
        """, 
        unsafe_allow_html=True
        )

    
    # st.write("------------------------------------------------------------------------------------------------------OR------------------------------------------------------------------------------------------------------")







    # File uploader for CSV files
    uploaded_file = st.file_uploader("Upload Examiner's Answer Sheet", type="csv", disabled=st.session_state.disable_file_upload)

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.upload_df = df # Store the uploaded DataFrame in session state
        
        st.session_state.disable_selected_option = True
 
        if not st.session_state.get('upload_rerun_triggered', False):
            st.session_state.upload_rerun_triggered = True
            st.rerun()
        
        # Display the CSV file uploaded
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Save the uploaded file to the 'Database' folder
        try:
            os.makedirs("Database", exist_ok=True)  # Create the folder if it doesn't exist
            file_path = os.path.join("Database", uploaded_file.name)
            df.to_csv(file_path, index=False)
            st.success(f"File saved to {file_path}")
        except Exception as e:
            st.error(f"Failed to save file: {e}")
        
        # Reset the rerun trigger since a file is uploaded
        st.session_state.rerun_triggered = False
        
    
    else:
        st.session_state.disable_selected_option = False
        st.session_state.upload_rerun_triggered = False
        st.session_state.upload_df = None

        # Trigger a rerun only once when the file is removed
        if not st.session_state.get('rerun_triggered', False):
            st.session_state.rerun_triggered = True
            st.rerun()
        
        
    


    st.divider()




    


    









    # Create a three-column layout
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, = st.columns(10)

    # Place the "Back" button in the leftmost column
    with col1:
        if st.button("Back"):
            st.session_state.current_page = "upload_student_answer"
            st.rerun()
    
    # Place the "Back" button in the leftmost column
    with col6:
        if st.session_state.df is not None or st.session_state.upload_df is not None:
            if st.button("Edit"):
                if "df" not in st.session_state:
                    st.warning("At least one student answer sheet needs to be selected")
                else:            
                    st.session_state.current_page = "edit_teacher_answer"
                    st.rerun()
    

    # Place the "Go to Page 3" button in the rightmost column
    with col10:
        if st.button("Evaluate"):
            if "df" not in st.session_state:
                st.error("At least one student answer sheet needs to be selected")
            else:
                st.session_state.current_page = "evaluate_page"
                st.rerun()

    


if __name__ == "__main__":
    examiner_pdf()


