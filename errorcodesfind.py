import requests
from bs4 import BeautifulSoup
import openai

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Function to fetch and summarize content from a URL
def fetch_and_summarize(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the main content from the page
    content = soup.get_text()

    # Summarize the content using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "gpt-4" if available
        prompt=f"Summarize the following content and extract any error codes or relevant descriptions:\n\n{content}",
        max_tokens=1500  # Adjust this based on your needs
    )
    summary = response['choices'][0]['text']
    return summary.strip()

# List of URLs to check (you would need to manually gather some starting points)
urls = [
    "https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks",
    "https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview",
    # Add more URLs here
]

# Iterate over the URLs and summarize each one
for url in urls:
    print(f"Processing URL: {url}")
    summary = fetch_and_summarize(url)
    print(f"Summary:\n{summary}\n")

    # Optionally save the summaries to a file
    with open("summaries.txt", "a", encoding="utf-8") as file:
        file.write(f"URL: {url}\n{summary}\n\n")
