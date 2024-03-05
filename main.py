import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

load_dotenv() 

octoai_api_token = os.getenv("OCTOAI_API_TOKEN") 
if not octoai_api_token:  # Check if token is retrieved successfully
    raise ValueError("OCTOAI_API_TOKEN not found in .env file or environment variables.")

ENDPOINT_URL = "https://text.octoai.run/v1/chat/completions"

template = """Complete the following steps: \n 1. Create a drink recipe contain {liquor} and is sweet \n 2. Output the response as json with the following fields:{json_format} """
prompt = PromptTemplate.from_template(template)
liquor = "Soju"
json_format = """{"name": "Sour Nostalgia", "description": "A unique cocktail with a nostalgic twist, featuring a sour flavor profile with a hint of nostalgia", "ingredients": [{"name": "Vodka", "quantity": "2 oz"}, {"name": "Lemon Juice", "quantity": "1 oz"}], "instructions": "Add all ingredients to a cocktail shaker without ice. Dry shake vigorously for 10-15 seconds. Add ice and shake again until well chilled"}"""

llm = OctoAIEndpoint(
    endpoint_url=ENDPOINT_URL,
    octoai_api_token=octoai_api_token,  # Pass token as a named parameter
    model_kwargs={
        "model": "gemma-7b-it",
        "max_tokens": 1024,
        "presence_penalty": 0,
        "temperature": 0.1,
        "top_p": 0.9,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. Keep your responses limited to one short paragraph if possible.",
            }
        ],
    },
)


inputs = {"liquor": liquor, "json_format": json_format}  

llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.invoke(inputs)["text"])