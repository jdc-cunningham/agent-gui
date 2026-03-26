from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.models.google import GoogleModel
import os

load_dotenv()
provider = GoogleProvider(api_key=os.getenv("GOOGLE_API_KEY"))
model = GoogleModel('gemini-2.5-flash', provider=provider)
agent = Agent(model)
result = agent.run_sync("Who are you")
print(result.output)

class Agent():
    def __init__(self, agent_name, model_name, agent_prompt):
        self.name = agent_name
        self.model_name = model_name
        self.prompt = agent_prompt

    def start_agent(self):
        print("start")
