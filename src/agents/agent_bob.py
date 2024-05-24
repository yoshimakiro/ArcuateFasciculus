import os
from autogen import ConversableAgent

class AgentBob(ConversableAgent):
    def __init__(self):
        super().__init__(
            "agent_bob",
            system_message="You are tasked with constructing a deployable Docker image for Ubuntu 22.04. "
                           "Provide a complete Dockerfile that builds a working Docker image.",
            llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
            human_input_mode="NEVER",
        )
