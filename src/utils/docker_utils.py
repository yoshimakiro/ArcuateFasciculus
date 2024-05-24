import os

def save_dockerfile(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)

def build_docker_image(proposal_path):
    return os.system(f"docker build -t test_image {proposal_path}")

def run_docker_image():
    return os.system("docker run --rm test_image")

def save_result(result, proposal_path):
    with open(os.path.join(proposal_path, 'result.log'), 'w') as file:
        file.write(result)
