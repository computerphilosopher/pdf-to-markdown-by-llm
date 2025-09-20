"""
Concrete implementation of a converter using the 'markitdown' library.
"""
from pathlib import Path
from markitdown import MarkItDown
from .base import BaseConverter


class MarkitdownConverter(BaseConverter):
    """
    A converter that uses the markitdown library to convert PDFs to Markdown.
    """

    def convert(self, source_path: Path) -> str:
        """
        Converts a PDF file to a raw Markdown string using markitdown.

        Args:
            source_path: The path to the PDF file.

        Returns:
            A string containing the raw Markdown content.
        """
        converter = MarkItDown()
        markdown_result = converter.convert(source_path)
        return markdown_result.text_content
