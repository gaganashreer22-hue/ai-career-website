import streamlit as st
import google.generativeai as genai

# PAGE CONFIG
st.set_page_config(page_title="AI Career Guide", page_icon="🎓")

# LOGIN STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "student" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Wrong username or password")

# AFTER LOGIN
else:
    st.title("🎓 AI Career Guidance System")
    st.write("Type ANY career and get real guidance in sentences.")

    career = st.text_input("Enter your career (example: Doctor, Pilot, Designer)")

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    if st.button("Get Career Guidance") and career:
        prompt = f"""
        You are a career counselor in India.

        A student wants to become a {career}.

        Explain in simple English and FULL SENTENCES:
        - What stream to choose after 10th/12th
        - What entrance exams are required
        - What courses to take
        - Best colleges in India for this career
        """

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        st.subheader("Career Guidance")
        st.write(response.text)
