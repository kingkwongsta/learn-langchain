# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload
# pip install pdfminer.six
# pip install pdf2image
# pip install opencv-python
# pip install unstructured_inference


from langchain_community.document_loaders import UnstructuredPDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

loader = PyPDFLoader("mlbook.pdf")
data = loader.load()

print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your sample document')
print (f'Here is a sample: {data[0].page_content[:200]}')