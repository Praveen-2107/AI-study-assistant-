import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

# Connect to Gemini
client = genai.Client()

# Page title
st.title("🤖 AI Study Assistant")

st.write("Ask me anything about your studies!")

# Get the student's question
question = st.text_input("Enter your question:")

# Ask Gemini when the button is clicked
if st.button("Ask AI"):

    if question:

        with st.spinner("🤖 AI is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=f"""
                Explain the following question to a college student.
                Use simple language and give an example if useful.

                Question:
                {question}
                """
            )

        st.subheader("🤖 AI Answer")
        st.write(response.text)

    else:
        st.warning("Please enter a question.")