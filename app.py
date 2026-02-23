from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

#Step 1 : Load ENV
load_dotenv()

#Step 2 : Create a Chat Template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a cool and useful assistant at the end of every querry you will be answering it in a puzzle manner."),
        ("user", "{question}")
    ]
)


llm = ChatGoogleGenerativeAI(
    temparature = 1.0,
    model = "gemini-2.5-flash"
)


st.title("Hehe")
input = st.text_input("What do you want to know?")


output = StrOutputParser()

chain = prompt|llm|output

if input:
    st.write(chain.invoke({"question":input}))