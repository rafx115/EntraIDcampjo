import os
import re

# Path to the directory containing the Markdown files
md_dir = "/workspaces/EntraIDcampjo/guides"

# Function to correct common Markdown errors
def correct_markdown_errors(content):
    # Ensure a blank line before and after headings
    content = re.sub(r'(^|\n)(#+\s)', r'\1\n\2', content)
    
    # Ensure a space after hash in headings
    content = re.sub(r'(^|\n)(#+)([^\s#])', r'\1\2 \3', content)
    
    # Ensure that lists are surrounded by blank lines
    content = re.sub(r'(^|\n)(\*|\-|\+)\s', r'\1\n\2 ', content)
    content = re.sub(r'(\*|\-|\+)\s([^\n]*)(\n)([^\n\*\-])', r'\1 \2\n\n\4', content)
    
    # Ensure line length is limited to 80 characters (adjust as necessary)
    lines = content.splitlines()
    corrected_lines = []
    for line in lines:
        if len(line) > 80 and not line.startswith("#"):
            corrected_lines.extend(re.findall(r'.{1,80}(?:\s+|$)', line))
        else:
            corrected_lines.append(line)
    
    return '\n'.join(corrected_lines)

# Function to process all Markdown files in the directory
def process_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Correct the errors
            corrected_content = correct_markdown_errors(content)
            
            # Save the corrected content back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(corrected_content)
            
            print(f"Corrected errors in {filename}")

# Run the script
process_markdown_files(md_dir)
