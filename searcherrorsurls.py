import os
import requests
from bs4 import BeautifulSoup
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Base directory where categorized URL files are stored
input_base_dir = r"C:\Users\joser\EntraIDcampjo\docs\categorized_urls"
output_base_dir = r"C:\Users\joser\EntraIDcampjo\docs\openai_results"

# Ensure the output base directory exists
os.makedirs(output_base_dir, exist_ok=True)

# Function to fetch and summarize content from a URL using OpenAI
def fetch_and_summarize(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the main content from the page
            content = soup.get_text()

            # Debug: Print content length
            print(f"Fetched content from {url}, length: {len(content)}")

            if len(content) < 100:
                print(f"Content from {url} is too short to process.")
                return None

            # Summarize the content using OpenAI API
            summary_response = openai.Completion.create(
                engine="text-davinci-003",  # or "gpt-4" if available
                prompt=f"Extract and summarize error codes and their descriptions from the following content:\n\n{content}",
                max_tokens=1500  # Adjust this based on your needs
            )
            summary = summary_response['choices'][0]['text']
            return summary.strip()
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Failed to process {url}: {e}")
        return None

# Iterate over each categorized file
for category_dir in os.listdir(input_base_dir):
    category_path = os.path.join(input_base_dir, category_dir)
    
    if not os.path.isdir(category_path):
        continue  # Skip if it's not a directory
    
    output_category_dir = os.path.join(output_base_dir, category_dir)

    # Ensure the category output directory exists
    os.makedirs(output_category_dir, exist_ok=True)

    # Process each file in the category
    for filename in os.listdir(category_path):
        input_file_path = os.path.join(category_path, filename)
        output_file_path = os.path.join(output_category_dir, f"openai_{filename}")

        if os.path.isfile(input_file_path):  # Check if it's a file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                urls = file.read().splitlines()

            # Prepare to write the results
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for url in urls:
                    print(f"Processing URL: {url}")
                    summary = fetch_and_summarize(url)
                    if summary:
                        output_file.write(f"URL: {url}\n{summary}\n\n")
                    else:
                        print(f"No content or summary returned for {url}")

        print(f"Finished processing {filename}, results saved to {output_file_path}")

print("Finished processing all URLs.")
