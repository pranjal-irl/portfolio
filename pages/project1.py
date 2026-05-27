import streamlit as st

st.title("Knowing your favourite programming language")
st.header("Made with Streamlit")
st.text("Welcome to my first interactive app!")

st.subheader("Choose your favourite programming language :")
language = st.selectbox("Your fav language :" , ["Select a language", "Java Script", "CSS", "Python", "HTML", "Java", "C", "C++", "Markdown" ])
if language != "Select a language":
    st.write(f"You chose {language}. Excellent choice!")
    
if language == "Java Script":
    st.write("We use JavaScript primarily because it is the only programming language that runs directly in web browsers, making it the essential tool for turning static pages into interactive experiences.")
elif language == "CSS":
    st.write("We use CSS (Cascading Style Sheets) to handle the visual presentation of a website, essentially turning 'boring' text into a designed interface. While HTML builds the structure (like the skeleton of a house), CSS provides the styling (like the paint and furniture).")
elif language == "Python":
    st.write("Python is a general-purpose programming language used because of its extreme versatility, English-like readability, and vast ecosystem of pre-built tools. Unlike specialized languages, Python can be used for everything from building complex AI models to automating simple daily tasks.")
elif language == "HTML":
    st.write("We use HTML (HyperText Markup Language) because it is the fundamental building block of the web, providing the essential structure and meaning to online content. While CSS handles the 'look' and JavaScript handles the 'action', HTML is the 'skeleton' that holds everything together.")
elif language == "Java":
    st.write("Java is one of the most widely used programming languages because it is platform-independent, meaning code written once can run on almost any device (Windows, Mac, Linux) without being rewritten. This 'Write Once, Run Anywhere' (WORA) capability is powered by the Java Virtual Machine (JVM).")
elif language == "C":
    st.write("C is used for its extreme speed, efficiency, and low-level memory access, making it essential for system-level programming, operating systems (like Linux kernel parts), and embedded systems. It acts as a bridge between high-level languages and hardware, offering portability and foundational knowledge for computer science.")
elif language == "C++":
    st.write("C++ is a powerhouse in the tech world primarily because it offers a rare combination of high-level abstraction and low-level control. Developers use it when performance, memory efficiency, and direct hardware interaction are the top priorities.")
elif language == "Markdown":
    st.write("Markdown is used primarily because it is a fast, easy-to-read, and future-proof way to format text without the clutter of complex rich-text editors (like Microsoft Word or Google Docs). Created to be simple to write and read, it serves as a lightweight alternative to HTML.")

if language != "Select a language":  
    st.success("You can call yourself a Coding Brat!")