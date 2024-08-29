import streamlit as st
import sys
import os
# from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, AgGridTheme


# Add the project's root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from Backend.utils import main

def evaluate_result():
    st.subheader("Evaluated Result", anchor=False)

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
    
    if st.sidebar.button("Upload Examiner Answer Sheet", type="primary"):
        st.session_state.current_page = "upload_teacher_answer"
        st.rerun()
    st.sidebar.button("Evaluate", type="primary")



    # Check if the PDF and DataFrame are stored in session state
    if "pdf_document" in st.session_state and "df_edited" in st.session_state:
        pdf_document = st.session_state.pdf_document        
        df = st.session_state.df_edited
        df.columns = df.columns.str.strip()

        # Use the main function to process the DataFrame and PDF
        result_df = main(df, pdf_document)

        # Display the resulting DataFrame
        st.write("Processed Result:")

        # Configure the grid options to enable text wrapping
        gb = GridOptionsBuilder.from_dataframe(result_df)
        # gb.configure_default_column(cellStyle={'color': 'black', 'font-size': '12px'}, suppressMenu=True, wrapHeaderText=True, autoHeaderHeight=True)
        # custom_css = {".ag-header-cell-text": {"font-size": "12px", 'text-overflow': 'revert;', 'font-weight': 700},
        #               ".ag-theme-streamlit": {'transform': "scale(0.8)", "transform-origin": '0 0'}}
        
        gb.configure_default_column(
            wrapText=False,  # Enables text wrapping
            autoHeight=True,  # Adjusts row height based on content
        )
        
        grid_options = gb.build()

        # Display the dataframe with AgGrid
        AgGrid(result_df, 
               gridOptions=grid_options, 
               columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
               theme=AgGridTheme.BALHAM)
        
        # AgGrid(result_df, 
        #        gridOptions=grid_options, 
        #        custom_css=custom_css, 
        #        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS, 
        #        theme=AgGridTheme.BALHAM, # Only choices: AgGridTheme.STREAMLIT, AgGridTheme.ALPINE, AgGridTheme.BALHAM, AgGridTheme.MATERIAL
        #        height=350
        #        )
        

        
        
        # Add a text input for the user to add a comment
        comment = st.text_input("Add Comment (if any)")
        # Handle Save button click
        if st.button("Save"):
            if comment:
                result_df['Comment'] = comment  # Add the comment as a new column with the same value for all rows
            else:
                result_df['Comment'] = ""  # Add an empty column if no comment is provided

        
        # Convert the DataFrame to CSV or Excel
        # csv_data = result_df.to_csv(index=False)  # or to_excel if you prefer Excel files

    
    
    else:
        st.write("PDF or DataFrame not found. Please go back to the previous pages to upload and prepare the data.")

    
    
    st.divider()
    
    col1, col2, col3, col4, col5 = st.columns(5)
    # Button to navigate back to the previous page
    with col1:
        if st.button("Home"):        
            st.session_state.current_page = "home_page"
            st.rerun()
    with col5:
        if "pdf_document" in st.session_state and "df" in st.session_state:
            st.download_button(
            label="Download",
            data=result_df.to_csv(index=False),  # or to_excel if you prefer Excel files,
            file_name="result.csv",  # Change to 'result.xlsx' if using Excel
            mime='text/csv',  # Change to 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' for Excel
    )


        


if __name__ == "__main__":
    evaluate_result()

