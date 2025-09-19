# Quickstart Guide: PDF to Markdown CLI Tool

This guide will walk you through the basic usage of the PDF to Markdown CLI tool.

## Prerequisites

1.  **Python 3.9+** installed.
2.  The tool installed (installation instructions to be added).
3.  A **Gemini API Key** set as an environment variable:
    ```bash
    export GEMINI_API_KEY='YOUR_API_KEY'
    ```

## Usage

To convert a PDF file, use the `pdf-to-markdown` command, passing the path to your PDF file as an argument.

```bash
pdf-to-markdown /path/to/your/document.pdf
```

This will create a new Markdown file named `document.md` in the same directory.

### Specifying an Output File

You can also specify a different output path for the Markdown file.

```bash
pdf-to-markdown /path/to/your/document.pdf --output /path/to/save/new_document.md
```

## Example

1.  You have a file named `report.pdf`.
2.  Run the command:
    ```bash
    pdf-to-markdown report.pdf
    ```
3.  A new file, `report.md`, will be created in the same directory. The content of this file will be the Markdown version of the PDF, refined for readability by Gemini.