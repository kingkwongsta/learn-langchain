
import os
from dotenv import load_dotenv
from typing import List
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    instructions: List[str] = Field(description="List of cooking instructions")
    # servings: Optional[int] = Field(description="Number of servings")
    # cook_time: Optional[str] = Field(description="Total cooking time")

parser = JsonOutputParser(pydantic_object=Recipe)
prompt = PromptTemplate(
    template="Create a food recipe based on {cuisine} cuisine",
    input_variables=["cuisine"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0125")

chain = prompt | model | parser
print(chain.invoke({"cuisine": "japanese"}))