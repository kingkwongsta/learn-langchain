from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_pdf(pdf, chunk_size, chunk_overlap):

    loader = PyPDFLoader(pdf)
    data = loader.load()

    #chunk_size=500 | chunk_overlap=50
    text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
    texts = text_splitter.split_documents(data)
    
    print("***** PDF Successfully Chunk *****")
    print (f'You have {len(data)} document(s) in your data')
    print (f'There are {len(data[0].page_content)} characters in your sample document')
    print (f'Here is a sample: {data[2].page_content[:200]}')

    
    return texts