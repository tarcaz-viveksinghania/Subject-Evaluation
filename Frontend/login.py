# import streamlit as st

# # Initialize session state for users if it does not exist
# if "users" not in st.session_state:
#     st.session_state.users = {}

# # Function to handle login
# def login(username, password):
#     if username in st.session_state.users and st.session_state.users[username] == password:
#         return True
#     return False

# # Function to handle signup
# def signup(username, password):
#     if username in st.session_state.users:
#         return False
#     st.session_state.users[username] = password
#     return True

# # Streamlit app
# def main():
#     st.title("Login / Signup Page")

#     # Tabs for login and signup
#     tabs = st.tabs(["Login", "Signup"])

#     with tabs[0]:
#         st.subheader("Login")
#         username = st.text_input("Username", key="login_username")
#         password = st.text_input("Password", type="password", key="login_password")
#         if st.button("Login"):
#             if login(username, password):
#                 st.success(f"Welcome {username}")
#             else:
#                 st.error("Invalid username or password")

#     with tabs[1]:
#         st.subheader("Signup")
#         new_username = st.text_input("New Username", key="signup_username")
#         new_password = st.text_input("New Password", type="password", key="signup_password")
#         if st.button("Signup"):
#             if signup(new_username, new_password):
#                 st.success("You have successfully signed up")
#             else:
#                 st.error("Username already exists")

# if __name__ == '__main__':
#     main()
