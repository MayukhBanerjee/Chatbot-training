from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

#initialize the env
load_dotenv()

#initialize prompt template
prompt=ChatPromptTemplate(
    [
        ("system","You are a helpful assisstant. Please respond to all the user querries"),
        ("user","{question}")
    ]
)

#streamlit framework
st.title("Langchain with Ollama API")
input = st.text("Enter your querry")


#llm creation
llm = Ollama(model="llama2",
             temperature = 1.0)

output = StrOutputParser()

chain = prompt|llm|output


if input:
    st.write(chain.ivoke({"question":"{input}"}))




