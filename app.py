import streamlit as st 
import os 
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv( "GOOGLE_API_KEY"))


#logics
model=genai.GenerativeModel("gemini-pro")
def get_ideas(query)  -> None:
    response = model.generate_content(query)
    return response.text

## steamlit for ui
st.set_page_config(page_title="keshavbot")

st.header("keshav Smart Bot")

input = st.text_input("Input:",key="input")
submit = st.button("ask the question")

if submit :
    response = get_ideas(input)
    st.subheader("your answer is")
    st.write(response)