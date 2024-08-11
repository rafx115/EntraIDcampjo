import os
from bs4 import BeautifulSoup
import requests

# URL of the Microsoft error codes page
url = "https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes#aadsts-error-codes"

# Fetch and parse the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Locate the table containing the error codes
table = soup.find("table", {"class": "table table-sm margin-top-none"})

# List to store error codes and their descriptions
error_codes = []

# Extract error codes and descriptions
if table:
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 2:
            code = cells[0].text.strip()
            description = cells[1].text.strip()
            error_codes.append((code, description))

# Check if any error codes were found
if not error_codes:
    print("No AADSTS error codes found. Please check the structure of the page.")
    exit()

# Directory to save the guides
output_dir = os.path.abspath("/workspaces/EntraIDcampjo/guides")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Template for the Markdown file
template = """
# {code}: {description}

## Introduction
This guide will help resolve issues related to {code} - {description}.

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

## Steps to Resolve

### Step 1: Initial Actions
1. Log in to the Azure AD portal.
2. Navigate to the "Users" section.
3. Select the affected user.
4. Perform necessary actions as described for the error.

### Step 2: Verify MFA Settings
1. Ensure that the user has MFA configured.
2. If necessary, guide the user through the MFA setup process.

## Additional Resources
- Link to further documentation or troubleshooting resources.

"""

# Generate the guides
for code, description in error_codes:
    filename = f"{code.lower()}.md"
    filepath = os.path.join(output_dir, filename)

    content = template.format(code=code, description=description)

    with open(filepath, "w") as file:
        file.write(content)

    print(f"Created {filepath}")

print(f"All guides created in {output_dir}")