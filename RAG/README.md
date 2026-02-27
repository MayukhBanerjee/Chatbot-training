Step 1: 
Load Source Data - The files may be pdf, md, txt files
This step is known as Data Ingestion

Step 2: 
We will 
    1)load - read from data source
    2) Feature engineering - Transform into smaller chunks : All LLMS have a context size 
    3) Embeddings - How we can use all these chunks into vectors
    4) Store it in a database for retreival


How to create vectors? 
We can use embeddings and then we need to store in the database.
We use ChromaDB , Faiss CPU , Lance etc. as Vector Databases



In short
Step 1: Data Ingestion

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPdfLoader
from langchain_community.document_loaders import WebBase Loader  and import bs4

loader = TextLoader(chunk_size , chunk_overlap)
loader = PyPdfLoader()
loader = WebBaseLoader(link = "", bs_kwargs = dict(parse_only = bs4.SoupStrainer(class="")),)


Step 2: 

