from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn 
from dotenv import load_env

#load the env
load_env()






