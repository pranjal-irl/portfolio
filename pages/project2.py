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



st.title("Just trying different widgets and getting used to it")

phase = st.selectbox("Which phase of life are you in while coding?", ["Choose phase", "School 🙋‍♂️","In Between School and College period 👻", "College 🧑‍🎓", "Doing internship 😋", "Doing a job 🧑‍💻", "Jobless at Home 😭🙏"])
if phase == "School 🙋‍♂️":
    st.write("Starting at the right time gang!")
if phase == "In Between School and College period 👻":
    st.write("Us bro us")
if phase == "College 🧑‍🎓":
    st.write("Grind time twin!")
if phase == "Doing internship 😋":
    st.write("Amazinggg!")
if phase == "Doing a job 🧑‍💻":
    st.write("Alright techie!")
if phase == "Jobless at Home 😭🙏":
    st.write("Keep going! the work will definitely pay off!")

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

import time
effect = "typewriter effect!!!!!"
def stream_text():
    for char in effect:
        yield char
        time.sleep(0.1)

if st.button("Click me for a magic"):
    st.write_stream(stream_text())

picture = st.camera_input("""Click a photo of yourself and see the magic!
                   Don't worry, I don't know how to save your picture to my device lol
                   """)
if picture is not None :
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Images/whatdoesheevendo.jpg")
    with col2:
        st.image(picture)
    with col3:
        st.image("Images/folkmeme.jpg")
    from streamlit_extras.let_it_rain import rain
    rain(emoji="🤣", font_size=54, falling_speed=5, animation_length=3)