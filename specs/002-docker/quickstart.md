# Quickstart: Running with Docker

This guide explains how to build and run the PDF to Markdown converter using Docker.

## Prerequisites

- Docker installed on your system.

## Build the Docker Image

1.  Clone the repository.
2.  Navigate to the root directory of the project.
3.  Build the Docker image by running the following command:

    ```bash
    docker build -t pdf-to-markdown .
    ```

## Run the Converter

To run the converter, you need to mount a local directory (containing your PDF files) into the container.

1.  Place the PDF you want to convert in a directory on your host machine (e.g., `./pdf`).
2.  Create an output directory (e.g., `./markdown`).
3.  Run the following command:

    ```bash
    docker run --rm \
      -v $(pwd)/pdf:/app/pdf \
      -v $(pwd)/markdown:/app/markdown \
      pdf-to-markdown \
      --input-path pdf/<your-pdf-file>.pdf \
      --output-path markdown/<your-output-file>.md
    ```

    Replace `<your-pdf-file>.pdf` with the name of your PDF file and `<your-output-file>.md` with the desired output filename.

The converted Markdown file will be available in the `./markdown` directory on your host machine.

