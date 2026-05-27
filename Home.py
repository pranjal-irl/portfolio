import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/project1.py", title="Know your Fav Programming Lang", icon="1️⃣"),
    st.Page("pages/project2.py", title="Know about your Coding Level", icon="2️⃣"),
])
pg.run()