"""
Unit tests for the PDF conversion logic in `src/converter.py`.
"""
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.converter import convert_pdf_to_markdown

@patch('src.converter.MarkItDown')
def test_convert_pdf_to_markdown(mock_markitdown):
    """
    Tests that the PDF conversion function calls the markitdown library correctly.
    """
    # Arrange
    mock_converter_instance = MagicMock()
    mock_converter_instance.convert.return_value = "# Mocked Markdown"
    mock_markitdown.return_value = mock_converter_instance

    dummy_pdf_path = Path("dummy.pdf")
    dummy_pdf_path.touch()

    # Act
    result = convert_pdf_to_markdown(dummy_pdf_path)

    # Assert
    mock_markitdown.assert_called_once()
    mock_converter_instance.convert.assert_called_once_with(dummy_pdf_path)
    assert result == "# Mocked Markdown"

    # Clean up
    dummy_pdf_path.unlink()