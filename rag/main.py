# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload
# pip install pypdf
# pip install pinecone-client


from langchain_community.document_loaders import UnstructuredPDFLoader, PyPDFLoader
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

# print (f'Now you have {len(texts)} documents')

from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
# PINECONE_API_ENV = os.getenv('PINECONE_API_ENV', 'us-east1-gcp') # You may need to switch with your env

pc = Pinecone(api_key=PINECONE_API_KEY)

pc.create_index(
    name="quickstart",
    dimension=8, # Replace with your model dimensions
    metric="euclidean", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-west-2"
    ) 
)

index = pc.Index("quickstart")

index.upsert(
  vectors=[
    {"id": "vec1", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
    {"id": "vec2", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
    {"id": "vec3", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
    {"id": "vec4", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]}
  ],
  namespace="ns1"
)

index.upsert(
  vectors=[
    {"id": "vec5", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
    {"id": "vec6", "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
    {"id": "vec7", "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
    {"id": "vec8", "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]}
  ],
  namespace="ns2"
)

index.describe_index_stats()
