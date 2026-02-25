import requests
import streamlit as st

def get_gemini_response_for_essays(input):
    #call the essay url
    response= requests.post("http://localhost:8000/essay/invoke", #API URL which is responsible in calling the essay version
    json = {"input":{"topic":input}})

    return response.json()["output"]["content"]


def get_gemini_response_for_poems(input1):
    response1 = requests.post("http://localhost:8000/poem/invoke",
    json = {"input":{"topic":input1}})
    return response1.json()["output"]["content"]


st.title("Langchain Model")
input = st.text_input("Write an essay on: ")
input1 = st.text_input("Write a poem on: ")

if input:
    st.write(get_gemini_response_for_essays(input))

if input1:
    st.write(get_gemini_response_for_poems(input1))