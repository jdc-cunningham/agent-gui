from agent_tools import get_weather
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.models.google import GoogleModel
import os

load_dotenv()

def get_model_creds(model_name: str):
    match model_name:
        case "gpt-4.1-mini":
            return os.getenv("OPEN_API_KEY")
        case "mistral-medium-2508":
            return os.getenv("MISTRAL_API_KEY")
        case "claude-sonnet-4-6":
            return os.getenv("ANTHROPIC_API_KEY")
        case "gemini-2.5-flash":
            return os.getenv("GOOGLE_API_KEY")
        case _:
            return ""

class Agent():
    def __init__(self, agent_name, model_name, agent_prompt, agent_tools):
        self.name = agent_name
        self.model_name = model_name
        self.prompt = agent_prompt
        self.agent_tools = agent_tools
        self.agent = self.start_agent()

    def start_agent(self):
        provider = GoogleProvider(api_key=get_model_creds(self.model_name))
        model = GoogleModel(self.model_name, provider=provider)

        self.agent = Agent(
            model,
            tools=self.tools
        )

    def query_agent(self, msg: str):
        result = self.agent.run_sync(msg)
