import streamlit as st

st.title("Hello!")
st.text("I am learning streamlit which is a python framework")
st.subheader("These are small projects/pages I made while learning different syntax")
st.subheader("Just click on one of these or you can also access all the pages from the sidebar")

st.navigation([
    st.Page("pages/project1.py", title="Know your Favourite Language", icon="1️⃣"),
    st.Page("pages/project2.py", title="My Other Project", icon="2️⃣"),
])