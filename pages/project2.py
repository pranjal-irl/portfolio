import streamlit as st

st.title("Know about your coding level")
st.text("You probably know where you are but have you ever thought in this way?")

st.text("Starting with the basic question")
phase = st.selectbox("Which phase of life are you in while coding?", ["School 🙋‍♂️","In Between School and College period 👻" "College 🧑‍🎓", "Doing internship 😋", "Doing a Job 🧑‍💻", "Jobless at Home 😭🙏"])
if phase:
    st.write("Alright...Good Luck for the Future gang!")

time = st.radio("How long have you been coding?" , ["0-2 months" , "2-6 months" , "6 months - 1 year" , "1-2 years" , "2-5 years" , "5-10 years" , "10+ years"])
if time == "0-2 months":
    st.write("So you are a beginner like me (when I am making this)✌️")
elif time == "2-6 months":
    st.write("So you surely know some things now 😼")
elif time == "6 months - 1 year":
    st.write("Getting Better and Better! 💪")
elif time == "1-2 years":
    st.write("Putting the work in! 🔥")
elif time == "2-5 years":
    st.write("That's Tufff 🥶")
elif time == "5-10 years":
    st.write("You're killing it ngl! 🫶")
elif time == "10+ years":
    st.write("A master of work 🫡")
