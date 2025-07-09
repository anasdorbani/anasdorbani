#!/bin/bash

# Local development script to test the banner generation

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating banner image..."
python export_readme.py

echo "Banner generated successfully!"
echo "To test locally, open resource/README_image.png"
echo "After pushing to GitHub, the image will be available at:"
echo "https://anasdorbani.github.io/anasdorbani/README_image.png"
