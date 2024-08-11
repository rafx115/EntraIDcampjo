import requests
from bs4 import BeautifulSoup
import os
import re

URL = "https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes#aadsts-error-codes"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

error_codes = []

# Find the table containing the AADSTS error codes
tables = soup.find_all('table')

# Iterate through tables and check for the one that contains 'AADSTS'
for index, table in enumerate(tables):
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 2:
            code_text = cells[0].get_text(strip=True)
            if 'AADSTS' in code_text:  # Check if this row contains an AADSTS code
                match = re.search(r'AADSTS\d+', code_text)
                if match:
                    code = match.group(0)
                    description = cells[1].get_text(strip=True)
                    error_codes.append({
                        'code': code,
                        'description': description,
                        'guide': f"This guide will help resolve issues related to {description.lower()}."
                    })
    if error_codes:  # Stop once the correct table has been found and processed
        break

# Check if any error codes were found
if not error_codes:
    print("No AADSTS error codes found. Please check the structure of the page.")
    exit()

# Set the output directory to the specified path
output_dir = "/workspaces/EntraIDcampjo/guides"

# Ensure the output directory exists
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
    # Ensure the filename is directly under the specified directory
    filename = os.path.join(output_dir, f"{error['code'].lower()}.md")
    content = template.format(
        code=error['code'],
        description=error['description'],
        guide=error['guide']
    )
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Created {filename}")

print(f"All guides created in {output_dir}")
