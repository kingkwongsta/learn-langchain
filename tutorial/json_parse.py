
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

prompt = PromptTemplate.from_template("Create a food recipe based on {cuisine} cuisine")
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0125")
output_parser = JsonOutputParser()

chain = prompt | model |output_parser
print(chain.invoke({"cuisine": "japanese"}))