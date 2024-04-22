# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload


from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()


# from langchain_openai import OpenAIEmbeddings
# from pinecone import Pinecone, ServerlessSpec
# from langchain_pinecone import PineconeVectorStore




# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# pc = Pinecone(api_key=PINECONE_API_KEY)

# use_serverless = True

# index_name = input("Which index do you want to load the data to? ")

# spec = ServerlessSpec(cloud='aws', region='us-west-2')

    
# index = pc.Index(index_name)



# model_name = 'text-embedding-ada-002'

# embeddings = OpenAIEmbeddings(
#     model=model_name,
#     openai_api_key=OPENAI_API_KEY
# )

# text_field = "text"
# vectorstore = PineconeVectorStore(
#     index, embeddings, text_field
# )

#----- add data to vector store
# docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=index_name)

# print(f"***** Successfully added data to Vector Store in index: {index_name} *****")
# print(index.describe_index_stats())