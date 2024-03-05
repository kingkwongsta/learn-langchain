import os
from dotenv import load_dotenv
from typing import List
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0125")

class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    instructions: List[str] = Field(description="List of cooking instructions")
    # servings: Optional[int] = Field(description="Number of servings")
    # cook_time: Optional[str] = Field(description="Total cooking time")

recipe_query = "Generate a recipe for {dish}"

parser = JsonOutputParser(pydantic_object=Recipe)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

print(chain.invoke({"query": recipe_query.format(dish="pasta")}))