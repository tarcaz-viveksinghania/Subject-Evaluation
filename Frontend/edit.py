import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder

def edit_page():
    st.subheader("Edit Examiner's Answer Sheet")

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

    if st.sidebar.button("Upload Student Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_student_answer"
        st.rerun()

    st.sidebar.button("Upload Examiner Answer Sheet", type="primary", use_container_width=True)
    
    if st.sidebar.button("Evaluate", type="primary"):
        st.session_state.current_page = "evaluate_page"
        st.rerun()
    


    # Check if either DataFrame is present
    if st.session_state.df is not None or st.session_state.upload_df is not None:
        # Determine which DataFrame to use for editing
        if st.session_state.df is not None:
            df_question_paper = st.session_state.df
            session_key = "df_edited"
        else:
            df_question_paper = st.session_state.upload_df
            session_key = "df_edited"
        
        # Show the data editor and allow editing
        edited_df = st.data_editor(df_question_paper, use_container_width=True, hide_index=True)
        

    else:
        st.warning("No DataFrame available for editing.")
    















    # Create a three-column layout
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    # Place the "Go Back" button in the leftmost column
    with col1:
        if st.button("Back"):
            st.session_state.current_page = "upload_teacher_answer"
            st.rerun()
    
    with col5:
        if st.button("Save"):
            # Save the edited DataFrame back into the correct session state
            st.session_state[session_key] = edited_df
            st.success("Changes saved!")
    
    with col9:
        if st.button("Evaluate"):
            st.session_state.current_page = "evaluate_page"
            st.rerun()


    

    



if __name__ == "__main__":
    edit_page()




    # # Dropdown menu
    # options = ["Select", "Option 1", "Option 2", "Option 3"]
    # selected_option = st.selectbox("Choose Examiner's Answer Sheet", options)

    # # Show content from the specified CSV if "Option 2" is selected
    # if selected_option == "Option 2":
    #     try:         
    #         # Load CSV file
    #         df_question_paper = pd.read_csv("Frontend/Database/Exam Evaluation_ CSVs   - Sample CSV 1_ Examiner's Guidelines .csv")
            
    #         # Store the uploaded DataFrame in session state
    #         st.session_state.df = df_question_paper

    #         # Configure the grid options to enable text wrapping
    #         # gb = GridOptionsBuilder.from_dataframe(df_question_paper)
    #         # gb.configure_default_column(
    #         #     wrapText=True,  # Enables text wrapping
    #         #     autoHeight=True,  # Adjusts row height based on content
    #         # )
    #         # grid_options = gb.build()

    #         # # Display the dataframe with AgGrid
    #         # AgGrid(df_question_paper, gridOptions=grid_options, fit_columns_on_grid_load=True)

    #         st.data_editor(df_question_paper, use_container_width=True, hide_index=True)

    #     except FileNotFoundError:
    #         st.error("The file 'Database/Exam Evaluation_ CSVs.csv' was not found.")
    #     except pd.errors.EmptyDataError:
    #         st.error("The file is empty.")
    #     except Exception as e:
    #         st.error(f"An error occurred: {e}")

    # st.divider()

    # # File uploader for CSV files
    # uploaded_file = st.file_uploader("Upload Examiner's Answer Sheet", type="csv")

    # if uploaded_file is not None:
    #     df = pd.read_csv(uploaded_file)

    #     # Store the uploaded DataFrame in session state
    #     st.session_state.df = df

    #     # Display the uploaded CSV data in grid format
    #     # gb = GridOptionsBuilder.from_dataframe(df)
    #     # gb.configure_default_column(
    #     #     wrapText=True,  # Enables text wrapping
    #     #     autoHeight=True,  # Adjusts row height based on content
    #     # )
    #     # grid_options = gb.build()

    #     # AgGrid(df, gridOptions=grid_options, fit_columns_on_grid_load=True)
    #     st.data_editor(df_question_paper, use_container_width=True, hide_index=True)

    #     # Save the uploaded file to the 'Database' folder
    #     try:
    #         os.makedirs("Database", exist_ok=True)  # Create the folder if it doesn't exist
    #         file_path = os.path.join("Database", uploaded_file.name)
    #         df.to_csv(file_path, index=False)
    #         st.success(f"File saved to {file_path}")
    #     except Exception as e:
    #         st.error(f"Failed to save file: {e}")