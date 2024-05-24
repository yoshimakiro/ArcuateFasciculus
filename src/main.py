import os
from agents.agent_bob import AgentBob
from agents.agent_alice import AgentAlice

def main():
    agent_bob = AgentBob()
    agent_alice = AgentAlice()

    topic = "topic_1"
    proposal_number = 1
    proposal_path = f"conversations/{topic}/sandbox/proposal_{proposal_number}"

    initial_message = "Please provide a Dockerfile for an Ubuntu 22.04 image with basic setup."
    result = agent_bob.initiate_chat(agent_alice, message=initial_message)

    alice_response = agent_alice.handle_message(result, proposal_path)
    print(alice_response)

if __name__ == "__main__":
    main()
