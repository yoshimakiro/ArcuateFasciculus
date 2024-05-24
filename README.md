
# ArcuateFasciculus

ArcuateFasciculus is a submodule of the [Principia Sapiens](https://github.com/yoshimakiro/PrincipiaSapiens) project and a preliminary attempt to facilitate collaborative problem-solving between indepedent thinkers. This project utilizes open-source tools and libraries to foster free and open innovation.

```
ArcuateFasciculus
.
├── Dockerfile
├── README.md                <---- You are here
├── requirements.txt
├── setup.sh
├── build
│   └── lib
│       └── agents
│           ├── agent_alice.py
│           ├── agent_bob.py
│           ├── halfin.py
│           └── __init__.py
├── conversations
│   └── topic_0000001
│       └── sandbox
│           └── proposal_0000001
│               ├── Dockerfile
│               └── result.log
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── agents
│   │   ├── agent_alice.py
│   │   ├── agent_bob.py
│   │   ├── halfin.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── agent_alice.cpython-310.pyc
│   │       ├── agent_bob.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   └── utils
│       ├── docker_utils.py
│       ├── init.py
│       └── __pycache__
│           └── docker_utils.cpython-310.pyc
└── tests
    ├── __init__.py
    ├── test_agent_alice.py
    ├── test_agent_bob.py
    ├── test_docker_utils.py
    └── test_halfin.py
```




## Setup

### Prerequisites

- Docker
- Python 3.8+

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yoshimakiro/ArcuateFasciculus.git
    cd ArcuateFasciculus
    ```

2. Create a virtual environment, install requirements, and activate it:
    ```bash
    source setup.sh
    ```

## Running the Application

To run the main application:

```bash
python src/main.py
```

## Testing

Unit tests are located in the `tests/` directory. To run the tests:

```bash
pytest tests/
```

## Docker Support

The project includes a Dockerfile to containerize the entire platform. Build and run the Docker container:

```bash
docker build -t arcuate-fasciculus .
docker run --rm -it arcuate-fasciculus
```

## Example Files

#### `src/agents/agent_bob.py`

```python
from autogen import ConversableAgent
import os

class AgentBob(ConversableAgent):
    def __init__(self):
        super().__init__(
            "agent_bob",
            system_message="You are tasked with constructing a deployable Docker image for Ubuntu 22.04. "
                           "Provide a complete Dockerfile that builds a working Docker image.",
            llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
            human_input_mode="NEVER",
        )
```

#### `src/agents/agent_alice.py`

```python
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
```

## Contribution Guidelines

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Acknowledgments

Thanks to the developers and contributors of the Autogen library, the cryptographic libraries, and other open-source tools used in this project.


## Contributors

- **Founder**: Yoshi Makiro

- **Special thanks**: HaI 🧡 @ ChatGPT and OpenAI

## Contact Information

For any queries or support, contact us here on github.
