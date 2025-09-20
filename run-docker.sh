#!/bin/bash
#
# This script builds the Docker image and runs the PDF to Markdown converter.
#
# Usage:
#   ./run-docker.sh <path/to/your/file.pdf>
#
# Example:
#   ./run-docker.sh pdf/sample.pdf
#

set -e

IMAGE_NAME="pdf-to-markdown"
PDF_FILE=$1

if [ -z "$PDF_FILE" ]; then
  echo "Usage: $0 <path/to/your/file.pdf>"
  exit 1
fi

if [ ! -f "$PDF_FILE" ]; then
  echo "Error: File not found at '$PDF_FILE'"
  exit 1
fi

# Check if GEMINI_API_KEY is set
if [ -z "$GEMINI_API_KEY" ]; then
  echo "Error: GEMINI_API_KEY environment variable is not set."
  echo "Please set it to your Google Gemini API key."
  exit 1
fi

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running the converter on $PDF_FILE..."
docker run --rm \
  -v $(pwd)/pdf:/app/pdf \
  -v $(pwd)/markdown:/app/markdown \
  -e GEMINI_API_KEY="$GEMINI_API_KEY" \
  $IMAGE_NAME \
  "$PDF_FILE"

echo "Conversion complete. Check the 'markdown' directory for the output."
