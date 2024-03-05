import os
import json
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

load_dotenv() 

octoai_api_token = os.getenv("OCTOAI_API_TOKEN") 
if not octoai_api_token: 
    raise ValueError("OCTOAI_API_TOKEN not found in .env file or environment variables.")

ENDPOINT_URL = "https://text.octoai.run/v1/chat/completions"

userLiquor = "vodka"
userFlavor = "sweet"
userMood = "celebratory"
instructions = "create a unique creative advance cocktail based on the user preferences in the text delimited by triple periods"
json_format = {
    "name": "Sour Nostalgia",
    "description":
      "A unique cocktail with a nostalgic twist, featuring a sour flavor profile with a hint of nostalgia",
    "ingredients": [
      {
        "name": "Vodka",
        "quantity": "2 oz",
      },
      {
        "name": "Lemon Juice",
        "quantity": "1 oz",
      },
    ],
    "instructions":
      "Add all ingredients to a cocktail shaker without ice. Dry shake vigorously for 10-15 seconds. Add ice and shake again until well chilled",
  };

userPreferences = f"{userLiquor} and emphasizes a {userFlavor} flavor profile for a {userMood} mood"
negative = f"Do not include {userFlavor}, {userLiquor}, or {userMood} in the recipe name."
template = instructions + negative + str(json_format) + f"...{userPreferences}..."
prompt = PromptTemplate.from_template(template)

llm = OctoAIEndpoint(
    endpoint_url=ENDPOINT_URL,
    octoai_api_token=octoai_api_token, 
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

# inputs = {"name": "Sour Nostalgia", "userLiquor": userLiquor, "userFlavor": userFlavor,"userMood": userMood}
inputs = {
    "name": "Sour Nostalgia",
    "userLiquor": userLiquor,
    "userFlavor": userFlavor,
    "userMood": userMood
}

llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.invoke(inputs))
