import streamlit as st
st.title("Pages")
st.subheader("I am learning streamlit which is a python framework")
st.text("These are small projects/pages I made while learning different syntax")
a = st.button("Know about your Favourite Programming Language")
if a:
    st.switch_page("pages/project1.py")
b = st.button("Know about your coding level")
if b :
    st.switch_page("pages/project2.py")
    