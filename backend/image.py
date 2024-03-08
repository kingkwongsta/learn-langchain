# https://api.python.langchain.com/en/latest/llms/langchain_community.llms.octoai_endpoint.OctoAIEndpoint.html
import os
from dotenv import load_dotenv
from typing import List
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint
from octoai.clients.image_gen import Engine, ImageGenerator

def getImage():
    load_dotenv()

    octoai_api_token = os.getenv("OCTOAI_API_TOKEN")
    if not octoai_api_token:
        raise ValueError("OCTOAI_API_TOKEN not found in .env file or environment variables.")

    endpoint_url = "https://image.octoai.run/generate/sdxl"
    model = OctoAIEndpoint(
        endpoint_url=endpoint_url,
        octoai_api_token=octoai_api_token,
        model_kwargs={
            "width": 1024,
            "height": 1024,
            "num_images": 1,
            "sampler": "DDIM",
            "steps": 30,
            "cfg_scale": 12,
            "use_refiner": True,
            "high_noise_frac": 0.8,
            "style_preset": "base",
        }
    )

    prompt = "a cat flying over the moon"  # Your desired image prompt

    # Create the PromptTemplate with empty input_variables (no dynamic inputs needed)
    prompt_template = PromptTemplate(
        template=prompt,
        input_variables=[]
    )

    chain = prompt_template | model

    # Invoke without any input data
    response = chain.invoke(input={})
    return response