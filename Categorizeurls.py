import os
from urllib.parse import urlparse

# Path to the text file containing the URLs
input_file_path = r"C:\Users\joser\EntraIDcampjo\docs\documentation_links.txt"

# Base output directory
output_base_dir = r"C:\Users\joser\EntraIDcampjo\docs\categorized_urls"

# Ensure the output base directory exists
os.makedirs(output_base_dir, exist_ok=True)

# Dictionary to store URLs categorized by their next segment after /identity/
categorized_urls = {}

# Read the URLs from the file
with open(input_file_path, 'r', encoding='utf-8') as file:
    all_documentation_links = file.read().splitlines()

# Categorize each URL based on the segment after /identity/
for url in all_documentation_links:
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')

    if 'identity' in path_segments:
        identity_index = path_segments.index('identity')
        if len(path_segments) > identity_index + 1:
            category = path_segments[identity_index + 1]
        else:
            category = 'root'  # For URLs that end directly after /identity/
    else:
        category = 'uncategorized'

    if category not in categorized_urls:
        categorized_urls[category] = []

    categorized_urls[category].append(url)

# Save categorized URLs into separate files
for category, urls in categorized_urls.items():
    category_dir = os.path.join(output_base_dir, category)
    os.makedirs(category_dir, exist_ok=True)

    output_file_path = os.path.join(category_dir, f"{category}_urls.txt")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + "\n")

    print(f"Saved {len(urls)} URLs under category '{category}' to {output_file_path}")

print("Finished categorizing and saving URLs.")
