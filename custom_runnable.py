from langchain.schema.runnable.base import Runnable
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

class CustomRunnable(Runnable):
    def __init__(self, model: OctoAIEndpoint, parser: JsonOutputParser):
        self.model = model
        self.parser = parser

    async def run(self, input_data):
        response = await self.model.run(input_data)
        return self.parser.parse(response)