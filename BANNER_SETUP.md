# Portfolio Banner Setup

This repository implements a dynamic banner generation system similar to GitHub stats, automatically generating and hosting a styled portfolio banner image.

## How It Works

1. **HTML Template**: `FullReadme.html` contains the styled banner with your portfolio information
2. **Image Generation**: `export_readme.py` converts the HTML to a PNG image using `imgkit` and saves it to the `resource` directory
3. **GitHub Actions**: Automatically generates and deploys the image from the `resource` directory to GitHub Pages on every push
4. **Dynamic Display**: The main README.md displays the hosted image from GitHub Pages

## Files Overview

- `FullReadme.html` - Styled HTML banner template
- `export_readme.py` - Python script to convert HTML to image
- `requirements.txt` - Python dependencies
- `generate_banner.sh` - Local development script
- `.github/workflows/generate-banner.yml` - GitHub Actions workflow
- `README.md` - Main README displaying the hosted banner

## Setup Instructions

### 1. Enable GitHub Pages
1. Go to your repository settings
2. Navigate to "Pages" section
3. Set source to "Deploy from a branch"
4. Select "gh-pages" branch
5. Click "Save"

### 2. Run the Workflow
The workflow will run automatically on every push to the main branch, or you can trigger it manually:
1. Go to "Actions" tab in your repository
2. Click on "Generate Portfolio Banner"
3. Click "Run workflow"

### 3. Local Development
To test locally:
```bash
# Install wkhtmltopdf (macOS)
brew install wkhtmltopdf

# Run the generation script
./generate_banner.sh
```

## Image URL
Once deployed, your banner will be available at:
- **Primary**: `https://anasdorbani.github.io/anasdorbani/README_image.png` (GitHub Pages)
- **Fallback**: `./resource/README_image.png` (committed to repository)

The README.md is configured to use the GitHub Pages URL first, with automatic fallback to the committed image if needed.

## Customization
- Edit `FullReadme.html` to modify the banner content and styling
- Update `export_readme.py` to change image dimensions or quality
- Modify the GitHub Actions workflow for different deployment options

## Troubleshooting

### Common Issues
1. **wkhtmltoimage options error**: If you get errors about unsupported options, the script uses only basic options that work with most versions
2. **Image quality**: Adjust the `quality` parameter in `export_readme.py` (0-100)
3. **Image dimensions**: Modify `width` and `height` in the options dictionary

### Local Testing
If you encounter issues locally, try:
```bash
# Test wkhtmltoimage directly
wkhtmltoimage --width 1200 --height 630 --quality 100 FullReadme.html test_output.png
```

## Benefits
- **Dynamic**: Updates automatically when you push changes
- **GitHub-friendly**: Works within GitHub's limitations
- **Professional**: Creates a polished, modern banner
- **Maintainable**: Easy to update content and styling
