# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload


from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

loader = PyPDFLoader("./mlbook2.pdf")
data = loader.load()

# print (f'You have {len(data)} document(s) in your data')
# print (f'There are {len(data[0].page_content)} characters in your sample document')
# print (f'Here is a sample: {data[2].page_content[:200]}')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(data)



# from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore




OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

pc = Pinecone(api_key=PINECONE_API_KEY)

use_serverless = True

index_name = input("Which index do you want to load the data to? ")

spec = ServerlessSpec(cloud='aws', region='us-west-2')

    
index = pc.Index(index_name)



model_name = 'text-embedding-ada-002'

embeddings = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=OPENAI_API_KEY
)

text_field = "text"
vectorstore = PineconeVectorStore(
    index, embeddings, text_field
)

#----- add data to vector store
docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=index_name)

print(f"***** Successfully added data to Vector Store in index: {index_name} *****")
print(index.describe_index_stats())