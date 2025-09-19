# Gemini Agent Context: PDF to Markdown CLI

This project is a Python-based CLI tool to convert PDF files to readable Markdown.

## Key Technologies

*   **Language**: Python 3
*   **CLI Framework**: `click`
*   **PDF Conversion**: `markitdown` library (https://github.com/microsoft/markitdown)
*   **Markdown Refinement**: Gemini API (`google-generativeai`)
*   **Testing**: `pytest`

## Core Logic

1.  The CLI takes a PDF file path as input.
2.  It uses the `markitdown` library to perform the initial conversion to a Markdown string.
3.  This raw Markdown is then passed to the Gemini API with a prompt to improve its readability and structure.
4.  The refined Markdown is saved to a `.md` file.

## Project Structure

```
src/
├── main.py         # CLI entry point
├── converter.py    # Core conversion logic
└── post_processor.py # Gemini API interaction

tests/
├── test_converter.py
└── test_post_processor.py
```
