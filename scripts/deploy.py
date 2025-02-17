import docker
import os
import sys

IMAGE_NAME = "z3-server"
TAG = "latest"
DOCKERFILE_PATH = "../"


def build_and_push(usrname, pwd):
    client = docker.from_env()
    repo = f"{usrname}/{IMAGE_NAME}"
    try:
        print("building Docker image...")
        image, _ = client.images.build(path=DOCKERFILE_PATH, tag=f"{IMAGE_NAME}:{TAG}")
        print(f"image {IMAGE_NAME}:{TAG} built successfully")

        image.tag(repo, tag=TAG)
        print("logging into Docker Hub...")
        client.login(username=usrname, password=pwd)
        print(f"pushing {repo}:{TAG} image...")
        push_logs = client.image.push(repo, tag=TAG)
        print(push_logs)
        print("Image pushed usccessfully")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    username = os.getenv("DOCKER_USERNAME")
    password = os.getenv("DOCKER_PASSWORD")
    if not username or not password:
        print(
            "Error: DOCKER_USERNAME and DOCKER_PASSWORD environment variables need to be set"
        )
        sys.exit(1)
    build_and_push(username, password)
