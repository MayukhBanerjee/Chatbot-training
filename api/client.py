import requests
import streamlit as st

def get_gemini_response(input):
    #call the essay url
    response= requests.post("http://localhost:8000/essay/invoke",
    json = {"input":{"topic":input}})

    return response.json()["output"]["content"]



st.title("Langchain Model")
input = st.text_input("Write an essay on: ")
input1 = st.text_input("Write a poem on: ")

if input:
    st.write(get_gemini_response(input))

if input1:
    st.write(get_gemini_response(input1))