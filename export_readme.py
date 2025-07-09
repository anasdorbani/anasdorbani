import imgkit
import os
import base64

# Path to the FullReadme HTML file
html_file_path = "FullReadme.html"
output_image_path = "resource/README_image.png"
background_image_path = "resource/johannes-andersson-UCd78vfC8vU-unsplash.jpg"

# Create resource directory if it doesn't exist
os.makedirs("resource", exist_ok=True)

# Check if HTML file exists
if not os.path.exists(html_file_path):
    print(f"Error: {html_file_path} not found")
    exit(1)

# Check if background image exists
if not os.path.exists(background_image_path):
    print(f"Error: {background_image_path} not found")
    exit(1)


# Convert background image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded_string}"


# Read the HTML file and replace the image src with base64
with open(html_file_path, "r") as file:
    html_content = file.read()

# Replace the relative image path with base64 data
base64_image = image_to_base64(background_image_path)
html_content = html_content.replace(
    "./resource/johannes-andersson-UCd78vfC8vU-unsplash.jpg", base64_image
)

# Write the modified HTML to a temporary file
temp_html_path = "temp_readme.html"
with open(temp_html_path, "w") as file:
    file.write(html_content)

# Options for better image generation
options = {
    "width": 1080,
    "height": 1080,
    "quality": 100,
    "format": "png",
    "encoding": "UTF-8",
}

try:
    # Convert HTML to image using imgkit
    imgkit.from_file(temp_html_path, output_image_path, options=options)
    print(f"Successfully exported README as image: {output_image_path}")

    # Clean up temporary file
    os.remove(temp_html_path)

except Exception as e:
    print(f"Error generating image: {e}")
    # Clean up temporary file if it exists
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    exit(1)
