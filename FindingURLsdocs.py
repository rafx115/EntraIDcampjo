import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to extract all links from a given page
def extract_links(base_url, visited_urls=None):
    if visited_urls is None:
        visited_urls = set()

    if base_url in visited_urls:
        return []

    try:
        with requests.Session() as session:
            logging.info(f"Fetching content from {base_url}...")
            response = session.get(base_url)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')

            visited_urls.add(base_url)

            links = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]
            documentation_links = [link for link in links if '/entra/identity/' in link]
            new_links = list(set(documentation_links) - visited_urls)

            logging.info(f"Found {len(new_links)} new links on {base_url}")
            return new_links

    except Exception as e:
        logging.error(f"Failed to process {base_url}: {e}")
        return []

def process_url(url, visited_urls):
    return extract_links(url, visited_urls)

def gather_all_links(base_url):
    visited_urls = set()
    all_links = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(process_url, base_url, visited_urls): base_url}
        total_links = 0

        while future_to_url:
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    new_links = future.result()
                    all_links.extend(new_links)
                    total_links += len(new_links)
                    logging.info(f"Processed {url}, total links gathered: {total_links}")

                    # Schedule new links for processing
                    for link in new_links:
                        if link not in visited_urls:
                            future_to_url[executor.submit(process_url, link, visited_urls)] = link

                except Exception as e:
                    logging.error(f"Error processing {url}: {e}")

                # Remove completed future
                del future_to_url[future]

    return list(set(all_links))

# Main URL to start from
base_url = "https://learn.microsoft.com/en-us/entra/identity/"

# Gather all links starting from the base URL
all_documentation_links = gather_all_links(base_url)

# Print out all the gathered URLs
logging.info("All gathered documentation links:")
for link in all_documentation_links:
    logging.info(link)

# Define the output path
output_path = r"C:\Users\joser\EntraIDcampjo\docs\documentation_links.txt"

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save these URLs to the specified file path
with open(output_path, "w", encoding="utf-8") as file:
    for link in all_documentation_links:
        file.write(link + "\n")

logging.info(f"Finished gathering {len(all_documentation_links)} documentation links.")
logging.info(f"Links saved to {output_path}")
