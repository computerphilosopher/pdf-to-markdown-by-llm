# PDF to Markdown CLI

This is a Python-based command-line tool to convert PDF files into high-quality, readable Markdown. It uses the `markitdown` library for the initial conversion and then leverages the Google Gemini API to refine the output for better structure and readability.

## Features

-   Convert PDF files to Markdown.
-   Automatically refine Markdown using the Gemini Pro model.
-   Simple and easy-to-use CLI.

## Quickstart (Docker)

This is the easiest way to run the application without setting up a local Python environment.

### Prerequisites

-   Docker installed on your system.
-   You have a Google Gemini API key.

### Usage

1.  **Set your Gemini API Key:**
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```

2.  **Run the script:**
    The `run-docker.sh` script will build the Docker image and run the converter on the PDF file you provide.

    ```bash
    ./run-docker.sh path/to/your/file.pdf
    ```
    For example:
    ```bash
    ./run-docker.sh pdf/sample.pdf
    ```

The converted Markdown file will be saved in the `markdown` directory.

## Running from Source

If you prefer to run the application from the source code, follow these steps.

### 1. Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd pdf-to-markdown-cli
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Configuration

-   **Set up your Gemini API Key:**
    Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey) and set it as an environment variable:
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```

### 3. Running the tool

To convert a PDF, run the following command from the project's root directory:

```bash
python -m src.main /path/to/your/file.pdf
```

The tool will create a new Markdown file in the `markdown/` directory.

## Configuration

You can configure the application using the following environment variables:

-   `GEMINI_API_KEY`: **(Required)** Your Google Gemini API key.
-   `GEMINI_MAX_WORKERS`: The maximum number of parallel workers for the Markdown refinement process. This can improve performance when processing large documents. The default value is `10`.
    ```bash
    export GEMINI_MAX_WORKERS=20
    ```

## Development

### Running Tests

To run the test suite, use `pytest`:

```bash
pytest
```
