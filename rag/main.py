# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload
# pip install pypdf
# pip install pinecone-client
# pip install -qU langchain-openai
# pip install langchain-pinecone


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



# from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore




OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

pc = Pinecone(api_key=PINECONE_API_KEY)

use_serverless = True

index_name = 'learn'

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
# docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=index_name)


# print(index.describe_index_stats())
query = "What is Machine Learning?"
# print(vectorstore.similarity_search(
#     query,  # our search query
#     k=3  # return 3 most relevant docs
# ))
# print(index.describe_index_stats())

from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQAWithSourcesChain


# completion llm
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

qa_with_sources = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# print(qa.invoke(query))
print(qa_with_sources.invoke(query))
