import streamlit as st

import streamlit as st

def set_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.pexels.com/photos/34804021/pexels-photo-34804021.jpeg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to apply the background
set_bg_image()

# Rest of your app code goes below



st.title("Hello!")
st.text("I am learning streamlit which is a python framework")
st.subheader("These are small projects/pages I made while learning different syntax")
st.subheader("Just click on one of these or you can also access all the pages from the sidebar at the top left")

st.page_link("pages/project1.py", label="Know your Fav Programming Language", icon="1️⃣")
st.page_link("pages/project2.py", label="Know about your Coding Level", icon="2️⃣")