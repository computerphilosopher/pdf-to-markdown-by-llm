"""
Handles the post-processing of Markdown content using a generative AI model.

This module takes a raw Markdown string, sends it to the Google Gemini API
with a prompt to refine it, and returns the improved version.
"""
import os
import concurrent.futures
import functools
from typing import Dict
import google.generativeai as genai


def _refine_chunk(chunk: str, model: genai.GenerativeModel, generation_config: Dict) -> str:
    """
    Sends a single chunk of Markdown to the Gemini API for refinement.

    Returns:
        The refined Markdown string, or the original chunk if refinement fails.
    """
    prompt = f"""Your task is to refine the following raw Markdown text extracted from a PDF. Your only job is to improve its structure and formatting for better readability.

**ABSOLUTE REQUIREMENT: You MUST NOT summarize, shorten, omit, or truncate any part of the original text. The output MUST contain 100% of the original content. This is a literal conversion, not a summary. Any form of content reduction is a failure.**

Raw Markdown to be refined:

{chunk}"""

    try:
        response = model.generate_content(prompt, generation_config=generation_config)
        # Safely extract text from response parts, avoiding the .text accessor.
        text_from_parts = "".join(part.text for part in response.parts if hasattr(part, 'text'))
        if text_from_parts:
            return text_from_parts
        else:
            # If no text is returned, log a warning and return the original chunk.
            finish_reason_name = "UNKNOWN"
            if response.candidates and response.candidates[0].finish_reason:
                finish_reason_name = response.candidates[0].finish_reason.name
            print(f"Warning: A chunk could not be refined (finish reason: {finish_reason_name}). Appending original chunk.")
            return chunk
    except Exception as e:
        print(f"Error refining chunk: {e}. Appending original chunk.")
        return chunk


def refine_markdown(raw_markdown: str) -> str:
    """
    Refines a raw Markdown string using the Gemini API, handling large texts
    by processing them in chunks concurrently.
    """
    # It's recommended to manage the API key securely.
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    generation_config = {
        "max_output_tokens": 8192,
    }

    # To avoid exceeding the model's output token limit (8192), we process the text
    # in smaller chunks. This character limit is set conservatively to ensure the
    # refined (potentially longer) output does not hit the token ceiling.
    CHUNK_CHARACTER_LIMIT = 2000

    # 1. Split the text into chunks
    paragraphs = raw_markdown.split('\n\n')
    chunks = []
    current_chunk = ""
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 2 < CHUNK_CHARACTER_LIMIT:
            if current_chunk:
                current_chunk += "\n\n"
            current_chunk += paragraph
        else:
            chunks.append(current_chunk)
            current_chunk = paragraph
    if current_chunk:
        chunks.append(current_chunk)

    # 2. Process chunks in parallel
    try:
        # Allow configuring the number of parallel workers via environment variable
        max_workers = int(os.environ.get("GEMINI_MAX_WORKERS", 10))
    except (ValueError, TypeError):
        print("Warning: Invalid value for GEMINI_MAX_WORKERS. Using default of 10.")
        max_workers = 10

    print(f"Refining {len(chunks)} chunks with {max_workers} parallel workers...")

    # Create a partial function to pass the model and config to the worker threads
    refine_with_context = functools.partial(_refine_chunk, model=model, generation_config=generation_config)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Use executor.map for parallel processing, which returns results in order.
        refined_chunks = list(executor.map(refine_with_context, chunks))

    # 3. Combine the results
    return "\n\n".join(refined_chunks)