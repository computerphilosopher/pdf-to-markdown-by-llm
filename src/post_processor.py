"""
Handles the post-processing of Markdown content using a generative AI model.

This module takes a raw Markdown string, sends it to the Google Gemini API
with a prompt to refine it, and returns the improved version.
"""
import os
import google.generativeai as genai

def refine_markdown(raw_markdown: str) -> str:
    """
    Refines a raw Markdown string using the Gemini API, handling large texts
    by processing them in chunks.
    """
    # It's recommended to manage the API key securely.
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    generation_config = {
        "max_output_tokens": 8192,
    }

    # 1. Split the text into chunks
    # We'll use a character limit that's safely below the token limit.
    # Let's aim for roughly 4000 characters per chunk.
    paragraphs = raw_markdown.split('\n\n')
    chunks = []
    current_chunk = ""
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 2 < 4000:
            if current_chunk:
                current_chunk += "\n\n"
            current_chunk += paragraph
        else:
            chunks.append(current_chunk)
            current_chunk = paragraph
    if current_chunk:
        chunks.append(current_chunk)

    # 2. Process each chunk and 3. Combine the results
    refined_chunks = []
    for i, chunk in enumerate(chunks):
        print(f"Refining chunk {i + 1}/{len(chunks)}...")
        prompt = f"""Your task is to refine the following raw Markdown text extracted from a PDF. Your only job is to improve its structure and formatting for better readability.

**ABSOLUTE REQUIREMENT: You MUST NOT summarize, shorten, omit, or truncate any part of the original text. The output MUST contain 100% of the original content. This is a literal conversion, not a summary. Any form of content reduction is a failure.**

Raw Markdown to be refined:

{chunk}"""
        response = model.generate_content(prompt, generation_config=generation_config)
        refined_chunks.append(response.text)

    return "\n\n".join(refined_chunks)
