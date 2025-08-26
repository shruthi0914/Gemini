from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_api_key"))


model=genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to generate response from the model and get response text
def generate_response(prompt):
    response=model.generate_content(prompt)
    return response.text

#INITIALIZE THE STREAMLIT APP
st.set_page_config(page_title="Q and A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input your prompt here",key="input")
submit=st.button("Submit")

if submit:
    response=generate_response(input)
    st.subheader("Response")
    st.write(response)

