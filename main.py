import os

os.environ["OCTOAI_API_TOKEN"] = "OCTOAI_API_TOKEN"
os.environ["ENDPOINT_URL"] = "https://text.octoai.run/v1/chat/completions"

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.\n Instruction:\n{question}\n Response: """
prompt = PromptTemplate.from_template(template)