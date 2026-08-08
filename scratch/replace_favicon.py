import os
import glob
import re

root_dir = r"c:\Users\ADMIN\Desktop\HTML & JS\meelad_software_0.1"

# 1. Update favicon.svg
favicon_path = os.path.join(root_dir, "favicon.svg")
microphone_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#eab308"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="128" fill="url(#bgGrad)"/>
  <g transform="translate(140.8, 102.4) scale(0.6)">
    <path d="M192 0C139 0 96 43 96 96V256c0 53 43 96 96 96s96-43 96-96V96c0-53-43-96-96-96zM64 216c0-13.3-10.7-24-24-24s-24 10.7-24 24v40c0 89.1 66.2 162.7 152 174.4V464H120c-13.3 0-24 10.7-24 24s10.7 24 24 24h72 72c13.3 0 24-10.7 24-24s-10.7-24-24-24H216V430.4c85.8-11.7 152-85.3 152-174.4V216c0-13.3-10.7-24-24-24s-24 10.7-24 24v40c0 70.7-57.3 128-128 128s-128-57.3-128-128V216z" fill="url(#goldGrad)"/>
  </g>
</svg>"""

with open(favicon_path, "w", encoding="utf-8") as f:
    f.write(microphone_svg)

# 2. Update HTML files to use ONLY the SVG favicon and add a cache buster
html_files = glob.glob(os.path.join(root_dir, "*.html")) + glob.glob(os.path.join(root_dir, "pages", "*.html"))

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove old .ico and .png favicon links
    content = re.sub(r'<link rel="icon" type="image/x-icon" href="\./favicon\.ico">\s*', '', content)
    content = re.sub(r'<link rel="icon" type="image/png" sizes="32x32" href="\./favicon-32x32\.png">\s*', '', content)
    content = re.sub(r'<link rel="icon" type="image/png" sizes="16x16" href="\./favicon-16x16\.png">\s*', '', content)
    content = re.sub(r'<link rel="apple-touch-icon" sizes="180x180" href="\./apple-touch-icon\.png">\s*', '', content)
    
    # Also handle the ../ prefix if in pages/ directory
    content = re.sub(r'<link rel="icon" type="image/x-icon" href="\.\./favicon\.ico">\s*', '', content)
    content = re.sub(r'<link rel="icon" type="image/png" sizes="32x32" href="\.\./favicon-32x32\.png">\s*', '', content)
    content = re.sub(r'<link rel="icon" type="image/png" sizes="16x16" href="\.\./favicon-16x16\.png">\s*', '', content)
    content = re.sub(r'<link rel="apple-touch-icon" sizes="180x180" href="\.\./apple-touch-icon\.png">\s*', '', content)

    # Update the svg link with a cache buster parameter
    content = re.sub(r'(<link rel="icon" type="image/svg\+xml" href=".*?favicon\.svg)(">)', r'\1?v=microphone\2', content)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Favicon updated successfully.")
