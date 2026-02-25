from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn 
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "Simple Server"
)


model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 1.0
)

add_routes(
    app,
    model,
    path="/geminiAI"

)




prompt1 = ChatPromptTemplate.from_template("Write me a paragraph about {topic} with 100 words ") 
prompt2 = ChatPromptTemplate.from_template("Write me a poem about the specific {topic} with 50 words.")

add_routes(
    app,
    prompt1|model,
    path = "/essay"

)

add_routes(
    app,
    prompt2|model,
    path = "/poem"
)



if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port = 8000)



