import os
import openai
import re

# Your OpenAI API key
openai.api_key = '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'  # Replace with your actual API key

# Base directory where the guides are located
base_guides_dir = r"C:\Users\joser\EntraIDcampjo\guides"

# List of predefined Azure Identity product categories
azure_identity_categories = [
    "Azure Active Directory (AAD)",
    "Azure AD B2C",
    "Azure AD B2B",
    "Microsoft Identity Platform",
    "Conditional Access",
    "Multi-Factor Authentication (MFA)",
    "Identity Protection",
    "Azure AD Connect",
    "Azure AD Domain Services",
    "Managed Identities",
    "Privileged Identity Management (PIM)",
    "Other"  # Default category for uncategorized files
]

# Initialize counters for evaluated, skipped, and updated files
total_files_count = 0
skipped_files_count = 0
updated_files_count = 0

# Function to generate troubleshooting steps and categorize the error code
def generate_troubleshooting_steps_and_category(code, description):
    prompt = f"""
    For the error code {code} with the following description: "{description}",
    - Provide a detailed troubleshooting guide.
    - Suggest the most appropriate Azure Identity product category or service this error relates to.
    - Initial diagnostic steps
    - Common issues that cause this error
    - Step-by-step resolution strategies
    - Additional notes or considerations
    - Documentation where steps can be found for guidance
    - Advice for data collection event viewer logs, nettrace, fiddler if related to the issue
    
    Your response should start with the category, followed by the troubleshooting guide.
    """
    
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Split the response into category and guide
            full_response = response['choices'][0]['message']['content'].strip()
            category, guide = full_response.split("\n", 1)
            
            # Ensure the category is in the predefined Azure Identity categories
            if category.strip() not in azure_identity_categories:
                return "Other", guide.strip()
            
            return category.strip(), guide.strip()
        except openai.error.APIError as e:
            print(f"API error: {e}. Retrying in 60 seconds...")
            time.sleep(60)
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded: {e}. Waiting for 60 seconds...")
            time.sleep(60)
        except openai.error.OpenAIError as e:
            print(f"General OpenAI error: {e}.")
            return "Other", "Troubleshooting steps could not be generated due to an error."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "Other", "Troubleshooting steps could not be generated due to an error."

# Function to sanitize and shorten the category name for valid directory creation
def sanitize_category_name(category):
    # Replace invalid characters with an underscore or space
    sanitized_category = re.sub(r'[<>:"/\\|?*]', '_', category)
    # Shorten the category to a reasonable length, if it's too long
    if len(sanitized_category) > 50:
        sanitized_category = sanitized_category[:50].rsplit(' ', 1)[0] + '_etc'
    return sanitized_category.strip('_')

# Function to match the description to a predefined Azure Identity product category
def match_to_azure_identity_category(description):
    for category in azure_identity_categories:
        if category.lower() in description.lower():
            return category
    return None

# Iterate through each Markdown file in the directory
for filename in os.listdir(base_guides_dir):
    if filename.endswith(".md"):
        total_files_count += 1  # Increment total files counter
        filepath = os.path.join(base_guides_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as file:
                content = file.read()

        lines = content.splitlines()
        
        # Skip over any leading empty lines
        first_non_empty_line = next((line for line in lines if line.strip()), "")
        
        if first_non_empty_line.startswith("#"):
            parts = first_non_empty_line[1:].split(":", 1)  # Remove '#' and split on the first ':'
            if len(parts) == 2:
                code = parts[0].strip()
                description = parts[1].strip()
                
                # Check if the file already contains a category
                if "Category:" in content:
                    print(f"Skipping {filename}: Category already exists.")
                    skipped_files_count += 1
                    continue
                
                # Try to match to a predefined Azure Identity category
                matched_category = match_to_azure_identity_category(description)
                
                if matched_category:
                    sanitized_category = sanitize_category_name(matched_category)
                    troubleshooting_steps = ""  # No need to generate new steps if category is matched
                else:
                    # Get the category and troubleshooting steps from OpenAI
                    category, troubleshooting_steps = generate_troubleshooting_steps_and_category(code, description)
                    sanitized_category = sanitize_category_name(category)
                
                # Ensure the category is valid; otherwise, use "Other"
                if sanitized_category not in azure_identity_categories:
                    sanitized_category = "Other"
                
                # Determine the product and create a directory if needed
                category_dir = os.path.join(base_guides_dir, sanitized_category)
                os.makedirs(category_dir, exist_ok=True)
                
                # Check if the file already contains troubleshooting steps
                if "## Troubleshooting Steps" in content:
                    # Just add the category if troubleshooting steps already exist
                    updated_content = content + f"\n\nCategory: {sanitized_category}"
                else:
                    # Add both category and troubleshooting steps
                    updated_content = content + f"\n\nCategory: {sanitized_category}\n\n## Troubleshooting Steps\n" + troubleshooting_steps

                # Save the updated content to the new category directory
                new_filepath = os.path.join(category_dir, filename)
                with open(new_filepath, 'w', encoding='utf-8') as file:
                    file.write(updated_content)

                # Optionally, delete the original file if it has been moved
                os.remove(filepath)

                print(f"Updated {filename} and moved to category {sanitized_category}.")
                updated_files_count += 1
            else:
                print(f"Skipping {filename}: Unable to parse code and description.")
                skipped_files_count += 1
                continue
        else:
            print(f"Skipping {filename}: Invalid format.")
            skipped_files_count += 1
            continue

# Print the total number of evaluated, updated, and skipped files
print(f"\nTotal files evaluated: {total_files_count}")
print(f"Total number of skipped files due to existing categories or invalid format: {skipped_files_count}")
print(f"Total number of files updated and moved to new categories: {updated_files_count}")
