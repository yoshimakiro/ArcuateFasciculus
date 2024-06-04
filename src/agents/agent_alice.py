from autogen import UserProxyAgent

import os
from utils.docker_utils import save_dockerfile, build_docker_image, run_docker_image, save_result

class AgentAlice(UserProxyAgent):
    def __init__(self):
        super().__init__(
            "agent_alice",
            system_message="You will review the Dockerfile provided by Bob, save it, attempt to build the Docker image, "
                           "run the image, and report any errors or success back to Bob.",
            llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
            code_execution_config={"work_dir": "docker_build", "use_docker": True},
            human_input_mode="NEVER",
            is_termination_msg=lambda msg: "Docker image built successfully" in msg["content"],
        )

    def handle_message(self, message, proposal_path):
        dockerfile_content = message["content"]
        save_dockerfile(dockerfile_content, os.path.join(proposal_path, 'Dockerfile'))
        build_result = build_docker_image(proposal_path)
        if build_result != 0:
            result_message = "Error: Docker image build failed."
            save_result(result_message, proposal_path)
            return result_message
        run_result = run_docker_image()
        if run_result != 0:
            result_message = "Error: Docker container run failed."
            save_result(result_message, proposal_path)
            return result_message
        result_message = "Docker image built and ran successfully."
        save_result(result_message, proposal_path)
        return result_message
