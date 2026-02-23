from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatTemplate
from langchain_core.output_parsers import StrOutputParser


#Step 1 : Load ENV
load_dotenv()

#Step 2 : Create a Chat Template
prompt = ChatTemplate(
    [
        ("system", "You are a cool and useful assistant at the end of every querry you will be answering it in a puzzle manner."),
        ("user", "{question}")
    ]
)


llm = ChatGoogleGenerativeAI(
    temparature = 1.0,
    model = "gemini-flash-2.5"
)

