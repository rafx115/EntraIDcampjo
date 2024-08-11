import os
import openai
import time

# Your OpenAI API key
openai.api_key = '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'

# Base directory where the guides are located
base_guides_dir = r"C:\Users\joser\EntraIDcampjo\guides"

# Initialize counters for evaluated and skipped files
total_files_count = 0
skipped_files_count = 0

# Function to generate troubleshooting steps and categorize the error code
def generate_troubleshooting_steps_and_category(code, description):
    prompt = f"""
    For the error code {code} with the following description: "{description}",
    - Provide a detailed troubleshooting guide.
    - Suggest the most appropriate product category or service this error relates to.
    - Initial diagnostic steps
    - Common issues that cause this error
    - Step-by-step resolution strategies
    - Additional notes or considerations
    - Documentation where steps can be found for guidance
    - Advice for data collection event viewer logs, netrace, fiddler if are related to the issue
    
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
            return category.strip(), guide.strip()
        except openai.error.APIError as e:
            print(f"API error: {e}. Retrying in 60 seconds...")
            time.sleep(60)
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded: {e}. Waiting for 60 seconds...")
            time.sleep(60)
        except openai.error.OpenAIError as e:
            print(f"General OpenAI error: {e}.")
            return "Uncategorized", "Troubleshooting steps could not be generated due to an error."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "Uncategorized", "Troubleshooting steps could not be generated due to an error."

# Iterate through each Markdown file in the directory
for filename in os.listdir(base_guides_dir):
    if filename.endswith(".md"):
        total_files_count += 1  # Increment total files counter
        filepath = os.path.join(base_guides_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.splitlines()
            
            # Check if the file already contains troubleshooting steps
            if "## Troubleshooting Steps" in content:
                print(f"Skipping {filename}: Troubleshooting steps already exist.")
                skipped_files_count += 1
                continue
            
            # Skip over any leading empty lines
            first_non_empty_line = next((line for line in lines if line.strip()), "")
            
            if first_non_empty_line.startswith("#"):
                parts = first_non_empty_line[1:].split(":", 1)  # Remove '#' and split on the first ':'
                if len(parts) == 2:
                    code = parts[0].strip()
                    description = parts[1].strip()
                    
                    # Get the category and troubleshooting steps from OpenAI
                    category, troubleshooting_steps = generate_troubleshooting_steps_and_category(code, description)
                    
                    # Determine the product and create a directory if needed
                    product_dir = os.path.join(base_guides_dir, category)
                    os.makedirs(product_dir, exist_ok=True)
                    
                    # Save the file in the appropriate product directory
                    filepath = os.path.join(product_dir, filename)
                else:
                    print(f"Skipping {filename}: Unable to parse code and description.")
                    skipped_files_count += 1
                    continue
            else:
                print(f"Skipping {filename}: Invalid format.")
                skipped_files_count += 1
                continue
        
        # Append troubleshooting steps to the file content
        updated_content = content + "\n\n## Troubleshooting Steps\n" + troubleshooting_steps
        
        # Save the updated content back to the file using utf-8 encoding
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Updated {filename} with troubleshooting steps in category {category}.")

# Print the total number of evaluated and skipped files
print(f"\nTotal files evaluated: {total_files_count}")
print(f"Total number of skipped files due to invalid format: {skipped_files_count}")
