# PDF to Markdown CLI

This is a Python-based command-line tool to convert PDF files into high-quality, readable Markdown. It uses the `markitdown` library for the initial conversion and then leverages the Google Gemini API to refine the output for better structure and readability.

## Features

-   Convert PDF files to Markdown.
-   Automatically refine Markdown using the Gemini Pro model.
-   Simple and easy-to-use CLI.

## Installation

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

4.  **Set up your Gemini API Key:**
    You need to have a Google Gemini API key to use the refinement feature.

    -   Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    -   Set it as an environment variable:
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY"
        ```

## Usage

To convert a PDF, run the following command:

```bash
python src/main.py /path/to/your/file.pdf
```

The tool will create a new Markdown file with the same name as the input PDF but with a `.md` extension (e.g., `file.md`) in the same directory.

### Example

```bash
python src/main.py "examples/sample.pdf"
```

Output:
```
Converting sample.pdf...
Refining Markdown with Gemini...
Successfully created sample.md
```

## Development

### Running Tests

To run the test suite, use `pytest`:

```bash
pytest
```
