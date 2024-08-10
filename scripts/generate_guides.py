import requests
from bs4 import BeautifulSoup
import os

URL = "https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes#aadsts-error-codes"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

error_codes = []

# Scrape error codes and descriptions from the table
table = soup.find('table')
if table:
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 2:  # Ensure there are exactly two cells in the row
            code = cells[0].get_text(strip=True)
            description = cells[1].get_text(strip=True)
            error_codes.append({
                'code': code,
                'description': description,
                'guide': f"This guide will help resolve issues related to {description.lower()}."
            })

# Check if any error codes were found
if not error_codes:
    print("No error codes found. Please check the structure of the page.")
    exit()

# Directory to save the guides
output_dir = os.path.join(os.getcwd(), "guides")
os.makedirs(output_dir, exist_ok=True)

# Template for the Markdown file
template = """
# {code}: {description}

## Introduction
{guide}

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

## Troubleshooting
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.
"""

# Generate a Markdown file for each error code
for error in error_codes:
    filename = os.path.join(output_dir, f"{error['code'].lower()}.md")
    content = template.format(
        code=error['code'],
        description=error['description'],
        guide=error['guide']
    )
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Created {filename}")

print(f"All guides created in {/workspaces/EntraIDcampjo/guides}")
