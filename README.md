# Static Site Generator

A Python-based static site generator that converts Markdown files into a complete HTML website. Built as part of the Boot.dev curriculum, this project demonstrates core programming concepts including file I/O, recursive algorithms, HTML generation, and text parsing.

## Features

- **Markdown to HTML conversion**: Parses Markdown syntax and generates semantic HTML
- **Recursive directory processing**: Automatically processes nested folder structures
- **Template system**: Uses customizable HTML templates for consistent page layouts
- **Static asset copying**: Handles CSS, images, and other static files
- **Block-level parsing**: Supports headings, paragraphs, code blocks, quotes, lists (ordered and unordered)
- **Inline formatting**: Handles bold, italic, code, links, and images

## Installation
No external dependencies are requires. This uses only the Python standard library

1. Clone this repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. Ensure you have Python3.x installed:
```bash
python --version
```
## Usage
- Run the generator from the project root:
```bash
python src/main.py
```
- This will: 
    - Clear the ```public/``` directory
    - Copy static assets from ```static/``` to ```public```
    - Convert all Markdown files from ```content/``` to HTML in ```public/```
    - Generate a complete static website ready to deploy

## Project Structure
```
├── content/          # Markdown source files
├── static/           # CSS, images, and other static assets
├── public/           # Generated HTML output (git-ignored)
├── src/              # Source code
│   ├── main.py       # Entry point
│   ├── htmlnode.py   # HTML node classes
│   ├── textnode.py   # Text node classes
│   └── ...           # Other modules
└── template.html     # HTML template for pages
```
## Customization
- Content: Add or modify Markdown files in the ```content/``` directory
- Styling: Edit CSS files in the ```static/``` directory
- Template: Modify ```template.html``` to change the page layout
- Functionality: Expand the parset in src/ to support additional markdown features

## Example Usage
- Input (```content/index.md```):
    ```bash
    # Welcome
    This is a **bold** statement with a [link](https://google.com)
    ```
- Output (```public/index.html```):
    ```bash
    <h1>Welcome</h1>
    <p>This is a <b>bold</b> statement with a <a href="https://www.google.com">link</a>.</p>
    ```
## Testing
Run the test suite:
```bash
python -m unittest discover
```


