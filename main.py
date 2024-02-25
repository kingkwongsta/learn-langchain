import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
output_parser = StrOutputParser()
loader = WebBaseLoader("https://docs.smith.langchain.com")
docs = loader.load()
embeddings = OpenAIEmbeddings()




def main():
   prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
   llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
   chain = prompt | llm | output_parser
   print(chain.invoke({"input": "how can langsmith help with testing?"}))




    

if __name__ == "__main__":
    main()