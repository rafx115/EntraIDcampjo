import requests
from bs4 import BeautifulSoup
import os

URL = "https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes#aadsts-error-codes"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

error_codes = []

# Scrape error codes and descriptions
for section in soup.find_all('div', {'class': 'table-row'}):
    code = section.find('div', {'class': 'table-cell code'}).get_text(strip=True)
    description = section.find('div', {'class': 'table-cell description'}).get_text(strip=True)
    error_codes.append({
        'code': code,
        'description': description,
        'guide': f"This guide will help resolve issues related to {description.lower()}."
    })

# Directory to save the guides
output_dir = "guides"
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
import requests
from bs4 import BeautifulSoup
import os

URL = "https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes#aadsts-error-codes"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

error_codes = []

# Scrape error codes and descriptions
for section in soup.find_all('div', {'class': 'table-row'}):
    code = section.find('div', {'class': 'table-cell code'}).get_text(strip=True)
    description = section.find('div', {'class': 'table-cell description'}).get_text(strip=True)
    error_codes.append({
        'code': code,
        'description': description,
        'guide': f"This guide will help resolve issues related to {description.lower()}."
    })
    print(f"Found error code: {code}, description: {description}")

# Check if any error codes were found
if not error_codes:
    print("No error codes found. Please check the structure of the page.")
    exit()

# Directory to save the guides
output_dir = "guides"
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
