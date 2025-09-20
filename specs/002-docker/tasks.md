# Tasks: Dockerize for Easy Trial

**Input**: Design documents from `/specs/002-docker/`
**Prerequisites**: plan.md (required), research.md, data-model.md, quickstart.md

## Phase 3.1: Setup
- [ ] T001 [P] Create `.dockerignore` at the repository root to exclude unnecessary files from the Docker image.
- [ ] T002 Create `Dockerfile` at the repository root to define the Docker image for the application.

## Phase 3.2: Core Implementation
- [ ] T003 Update `README.md` with instructions on how to build and run the application using Docker, based on `specs/002-docker/quickstart.md`.

## Phase 3.3: Polish
- [ ] T004 (Optional) Create a `run-docker.sh` script at the repository root to simplify the `docker run` command for users.

## Dependencies
- T001 and T002 have no dependencies.
- T003 should be done after T002, as the `README.md` will refer to the `Dockerfile`.
- T004 is optional and can be done at any time after T002.

## Parallel Example
Tasks T001 and T002 can be run in parallel as they involve creating two different files.

```
# Launch T001 and T002 together:
Task: "Create .dockerignore at the repository root to exclude unnecessary files from the Docker image."
Task: "Create Dockerfile at the repository root to define the Docker image for the application."
```
