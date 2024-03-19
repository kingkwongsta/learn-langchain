# .venv\Scripts\Activate.ps1
# cd .venv
# source bin/activate
# uvicorn main:app --reload
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = UnstructuredPDFLoader("mlbook.pdf")
data = loader.load()

print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')