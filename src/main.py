"""
Main entry point for the PDF to Markdown conversion CLI.

This module uses the `click` library to create a command-line interface
that takes a PDF file path as input, orchestrates the conversion to
Markdown, refines the output using a generative AI model, and saves the
result to a new file.
"""
import click
from pathlib import Path
from src.converter import convert_pdf_to_markdown
from src.post_processor import refine_markdown

@click.command()
@click.argument('pdf_path', type=click.Path(exists=True))
def cli(pdf_path):
    """
    Converts a PDF file to a refined Markdown file.
    """
    pdf_path = Path(pdf_path)
    click.echo(f"Converting {pdf_path.name}...")

    try:
        raw_markdown = convert_pdf_to_markdown(pdf_path)
        click.echo("Refining Markdown with Gemini...")

        refined_markdown = refine_markdown(raw_markdown)

        output_dir = Path("markdown")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / pdf_path.with_suffix('.md').name
        with open(output_path, 'w') as f:
            f.write(refined_markdown)

        click.echo(f"Successfully created {output_path}")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()
