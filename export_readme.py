import imgkit
import os

# Path to the FullReadme HTML file
html_file_path = "FullReadme.html"
output_image_path = "resource/README_image.png"

# Create resource directory if it doesn't exist
os.makedirs("resource", exist_ok=True)

# Check if HTML file exists
if not os.path.exists(html_file_path):
    print(f"Error: {html_file_path} not found")
    exit(1)

# Options for better image generation
options = {
    'width': 1200,
    'height': 630,
    'disable-smart-width': '',
    'quality': 100,
    'format': 'png',
    'encoding': 'UTF-8',
    'crop-h': 630,
    'crop-w': 1200,
    'crop-x': 0,
    'crop-y': 0
}

try:
    # Convert HTML to image using imgkit
    imgkit.from_file(html_file_path, output_image_path, options=options)
    print(f"Successfully exported README as image: {output_image_path}")
except Exception as e:
    print(f"Error generating image: {e}")
    exit(1)
