import streamlit as st

st.title("Hello!")
st.text("I am learning streamlit which is a python framework")
st.subheader("These are small projects/pages I made while learning different syntax")
st.subheader("Just click on one of these or you can also access all the pages from the sidebar at the top left")

st.page_link("pages/project1.py", label="Know your Fav Programming Language", icon="1️⃣")
st.page_link("pages/project2.py", label="Know about your Coding Level", icon="2️⃣")