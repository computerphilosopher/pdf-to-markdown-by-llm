"""
Main entry point for the PDF to Markdown conversion CLI.

This module uses the `click` library to create a command-line interface
that takes a PDF file path as input, orchestrates the conversion to
Markdown, refines the output using a generative AI model, and saves the
result to a new file.
"""
import click
from pathlib import Path
from .converters.markitdown_converter import MarkitdownConverter
from .post_processor import refine_markdown

@click.command()
@click.argument('pdf_path', type=click.Path(exists=True))
def cli(pdf_path: str) -> None:
    """
    Converts a PDF file to a refined Markdown file.
    """
    pdf_path_obj = Path(pdf_path)
    click.echo(f"Converting {pdf_path_obj.name}...")

    try:
        # 1. Instantiate and use the converter
        converter = MarkitdownConverter()
        raw_markdown = converter.convert(pdf_path_obj)
        
        # 2. Post-process the result
        click.echo("Refining Markdown with Gemini...")
        refined_markdown = refine_markdown(raw_markdown)

        # 3. Save the output
        output_dir = Path("markdown")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / pdf_path_obj.with_suffix('.md').name
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(refined_markdown)

        click.echo(f"Successfully created {output_path}")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()
