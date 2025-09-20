# Research for Dockerization

## Technology Choices

### Containerization

- **Decision**: Use Docker to containerize the application.
- **Rationale**: Docker is the industry standard for containerization. It allows for easy packaging of the application and its dependencies, ensuring it runs consistently across different environments. This directly addresses the problem statement of simplifying the trial process for new users.
- **Alternatives considered**: Podman, containerd. While viable, Docker has a larger community and more extensive documentation, making it more suitable for this project's goal of easy adoption.

### Container Registry

- **Decision**: Use Docker Hub for distributing the image.
- **Rationale**: Docker Hub is the default and most widely used container registry. It's a public registry that's easy to use and well-integrated with the Docker CLI. For a public, open-source project, it's the simplest choice for distribution. The user's initial thought was "dockerhub면 되겠지 대안 있나?" ("Docker Hub should be fine, are there alternatives?"). While there are alternatives, Docker Hub is the most straightforward for this use case.
- **Alternatives considered**:
    - **GitHub Container Registry (GHCR)**: A strong alternative, especially since the code is likely on GitHub. It integrates well with GitHub Actions.
    - **GitLab Container Registry**: Similar to GHCR, but for GitLab users.
    - **Cloud-specific registries (ECR, ACR, GCR)**: These are more suitable for applications deployed within a specific cloud ecosystem.
    - For the purpose of a simple, public distribution, Docker Hub remains the most logical choice.

## Implementation Details

### Dockerfile

- A multi-stage build is not necessary for this project's scope (as per the spec).
- A simple `Dockerfile` will be created, using a Python base image, copying the source code, installing dependencies, and setting an entrypoint.

### `.dockerignore`

- A `.dockerignore` file will be created to prevent unnecessary files (like `.git`, `.venv`, `__pycache__`) from being included in the Docker image, which helps to keep the image size small.
