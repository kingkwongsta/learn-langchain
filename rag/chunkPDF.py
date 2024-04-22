from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_pdf(pdf, chunk_size, chunk_overlap):

    loader = PyPDFLoader(pdf)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(data)
    print("**************************************************")
    print("<<<<<<<<<< PDF Successfully Chunk >>>>>>>>>>")
    print (f'You have {len(data)} document(s) in your data')
    print (f'There are {len(data[0].page_content)} characters in your sample document')
    # print (f'Here is a sample: {data[80].page_content[:200]}')
    print (f'Here is a sample: {data[80]}')
    print("**************************************************")
    
    return texts