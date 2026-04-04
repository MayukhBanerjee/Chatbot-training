'''Aim: A normal chatbot using both a paid and Ollama LLMS'''

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

#prompt template


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You Are a very cool assistant and a helpful one , please respond to the user querries like a cool guy!"),
        ("user", "Question:{question}")
    ]
)


#streamlit framework
st.title("Langchain Demo with cool APIs")
input_text = st.text_input("Search the topic you want")


#GOOGLE LLM
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 1.0
)

output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))

