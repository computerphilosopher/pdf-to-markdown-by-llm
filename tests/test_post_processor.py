"""
Unit tests for the Markdown post-processing logic in `src/post_processor.py`.
"""
import pytest
from unittest.mock import patch, MagicMock
from src.post_processor import refine_markdown

@patch('src.post_processor.genai.GenerativeModel')
def test_refine_markdown(mock_generative_model):
    """
    Tests that the markdown refinement function calls the Gemini API correctly.
    """
    # Arrange
    mock_model_instance = MagicMock()
    mock_model_instance.generate_content.return_value.text = "Refined Markdown"
    mock_generative_model.return_value = mock_model_instance

    raw_markdown = "# Raw Title"

    # Act
    result = refine_markdown(raw_markdown)

    # Assert
    mock_generative_model.assert_called_with('gemini-2.5-flash')
    mock_model_instance.generate_content.assert_called_once()
    assert result == "Refined Markdown"

def test_refine_markdown_no_api_key(monkeypatch):
    """
    Tests that a ValueError is raised if the GEMINI_API_KEY is not set.
    """
    # Arrange
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    # Act & Assert
    with pytest.raises(ValueError, match="GEMINI_API_KEY environment variable not set."):
        refine_markdown("some markdown")