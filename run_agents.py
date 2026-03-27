from agent_tools import get_weather, get_crypto_price
from dotenv import load_dotenv
from pydantic_ai import Agent as PydanticAgent
from pydantic_ai.providers.anthropic import AnthropicProvider
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.mistral import MistralProvider
from pydantic_ai.models.mistral import MistralModel
import os

load_dotenv()

tool_map = {
    "get_weather": get_weather,
    "get_crypto_price": get_crypto_price
}

def get_model(model_name: str):
    match model_name:
        case "gpt-4.1-mini":
            provider = OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"))
            return OpenAIChatModel(self.model_Name, provider=provider)
        case "mistral-medium-2508":
            provider = MistralProvider(api_key=os.getenv("MISTRAL_API_KEY"))
            return MistralModel(self.model_name, provider=provider)
        case "claude-sonnet-4-6":
            provider = AnthropicProvider(api_key=os.getenv("ANTHROPIC_API_KEY"))
            return AnthropicModel(self.model_name, provider=provider)
        case "gemini-2.5-flash":
            provider = GoogleProvider(api_key=os.getenv("GOOGLE_API_KEY"))
            return GoogleModel(self.model_name, provider=provider)
        case _:
            return None

class Agent():
    def __init__(self, agent_name, model_name, agent_prompt, agent_tools):
        self.name = agent_name
        self.model_name = model_name
        self.prompt = agent_prompt
        self.agent_tools = agent_tools
        self.agent = self.start_agent()
        self.messages = []

    def start_agent(self):
        model = self.get_model(self.model_name)
        tools_list = []

        # have to turn string into actual function reference
        for tool in self.agent_tools.split(","):
            if tool in tool_map:
                tools_list.append(tool_map[tool])

        return PydanticAgent(
            model,
            tools=tools_list
        )

    def query_agent(self, msg: str):
        result = self.agent.run_sync(msg)
        print(result.output)
