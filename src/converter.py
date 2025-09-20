"""
Core logic for converting PDF files to raw Markdown.

This module uses the `markitdown` library to perform the initial
conversion from a PDF document to a Markdown string.
"""
from pathlib import Path
from markitdown import MarkItDown

def convert_pdf_to_markdown(pdf_path: Path) -> str:
    """
    Converts a PDF file to a raw Markdown string.
    """
    converter = MarkItDown()
    markdown_result = converter.convert(pdf_path)
    return markdown_result.text_content
