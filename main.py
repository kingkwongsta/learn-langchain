# activate virtual env - go to .venvscripts
# enter: .\Activate.ps1
import os
import json
from dotenv import load_dotenv
from typing import List
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

load_dotenv() 

octoai_api_token = os.getenv("OCTOAI_API_TOKEN") 
if not octoai_api_token: 
    raise ValueError("OCTOAI_API_TOKEN not found in .env file or environment variables.")

ENDPOINT_URL = "https://text.octoai.run/v1/chat/completions"

class Recipe(BaseModel):
    name: str = Field(description="Name of the drink")
    description: str = Field(description="Description of the drink")
    ingredients: List[str] = Field(description="List of ingredients")
    instructions: List[str] = Field(description="List of mixing instructions")

instructions = "create a unique creative advance cocktail based on the following user preferences of {userLiquor}, {userFlavor}, {userMood}. \n"
negative = "Do not include {userFlavor}, {userLiquor}, or {userMood} in the recipe name. \n"
parser = JsonOutputParser(pydantic_object=Recipe)

template = instructions + negative
prompt = PromptTemplate(
    template="{template}.\n{format_instructions}\n{query}\n",
    input_variables=["userLiquor", "userFlavor", "userMood"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = OctoAIEndpoint(
    endpoint_url=ENDPOINT_URL,
    octoai_api_token=octoai_api_token, 
    model_kwargs={
        "model": "smaug-72b-chat",
        "max_tokens": 1024,
        "presence_penalty": 0,
        "temperature": 0.6,
        "top_p": 0.9,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert mixologist that outputs JSON",
            }
        ],
    },
)

chain = prompt | model | parser

print(chain.invoke({"userLiquor": "Soju", "userFlavor": "Sweet", "userMood": "Celebratory"}))