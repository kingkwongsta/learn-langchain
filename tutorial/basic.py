
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

prompt = PromptTemplate.from_template("Why is {color} such an important color")
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0125")
output_parser = StrOutputParser()

chain = prompt | model 
print(chain.invoke({"color": "blue"}))