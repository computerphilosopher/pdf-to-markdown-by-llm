"""
End-to-end tests for the CLI in `src/main.py`.

These tests use `click.testing.CliRunner` to invoke the CLI and assert
that it behaves as expected, mocking the actual conversion and
post-processing logic.
"""
import pytest
from click.testing import CliRunner
from pathlib import Path
from unittest.mock import patch
from src.main import cli

@patch('src.main.convert_pdf_to_markdown')
@patch('src.main.refine_markdown')
def test_cli_end_to_end(mock_refine_markdown, mock_convert_pdf_to_markdown):
    """
    Tests the CLI end-to-end, mocking the core conversion
    and refinement logic.
    """
    # Arrange
    mock_convert_pdf_to_markdown.return_value = "raw markdown"
    mock_refine_markdown.return_value = "refined markdown"

    runner = CliRunner()
    dummy_pdf = Path("test.pdf")
    dummy_pdf.write_text("dummy pdf content")
    output_file = Path("test.md")

    # Act
    result = runner.invoke(cli, [str(dummy_pdf)], catch_exceptions=False)

    # Assert
    assert result.exit_code == 0
    assert output_file.exists()
    assert output_file.read_text() == "refined markdown"
    mock_convert_pdf_to_markdown.assert_called_once_with(dummy_pdf)
    mock_refine_markdown.assert_called_once_with("raw markdown")

    # Clean up
    dummy_pdf.unlink()
    output_file.unlink()

@patch('src.main.convert_pdf_to_markdown')
@patch('src.main.refine_markdown')
def test_cli_handles_error(mock_refine_markdown, mock_convert_pdf_to_markdown):
    """
    Tests that the CLI handles exceptions gracefully and exits with an error.
    """
    # Arrange
    mock_convert_pdf_to_markdown.return_value = "raw markdown"
    mock_refine_markdown.side_effect = Exception("Test API Error")

    runner = CliRunner()
    dummy_pdf = Path("test.pdf")
    dummy_pdf.write_text("dummy pdf content")

    # Act
    result = runner.invoke(cli, [str(dummy_pdf)])

    # Assert
    assert result.exit_code != 0
    assert "An error occurred" in result.output
    assert "Test API Error" in result.output

    # Clean up
    dummy_pdf.unlink()
