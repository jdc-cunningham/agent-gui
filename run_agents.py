class Agent():
    def __init__(self, agent_name, model_name, agent_prompt):
        self.name = agent_name
        self.model_name = model_name
        self.prompt = agent_prompt

    def start_agent(self):
