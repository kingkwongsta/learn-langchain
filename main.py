import os
from dotenv import load_dotenv


load_dotenv()
OCTOAI_TOKEN = os.getenv("OCTOAI_TOKEN")
ENDPOINT_URL = "https://text.octoai.run/v1/chat/completions"



from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.\n Instruction:\n{question}\n Response: """
prompt = PromptTemplate.from_template(template)

llm = OctoAIEndpoint(
    endpoint_url=ENDPOINT_URL,
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
            },
        ],
    },
)

question = "Who was leonardo davinci?"

llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.invoke(question))
print("hello")
