import os
import openai
import time

# Your OpenAI API key
openai.api_key = ''

# Directory where the guides are located
guides_dir = "/workspaces/EntraIDcampjo/guides"

# Initialize counters for evaluated and skipped files
total_files_count = 0
skipped_files_count = 0

# Function to generate troubleshooting steps using ChatGPT
def generate_troubleshooting_steps(code, description):
    prompt = f"""
    Provide a detailed troubleshooting guide for the error code {code} with the following description: {description}.
    Make sure to include:
    - Initial diagnostic steps
    - Common issues that cause this error
    - Step-by-step resolution strategies
    - Additional notes or considerations
    """
    
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.APIError as e:
            print(f"API error: {e}. Retrying in 60 seconds...")
            time.sleep(60)
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded: {e}. Waiting for 60 seconds...")
            time.sleep(60)
        except openai.error.OpenAIError as e:
            print(f"General OpenAI error: {e}.")
            return "Troubleshooting steps could not be generated due to an error."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "Troubleshooting steps could not be generated due to an error."

# Iterate through each Markdown file in the directory
for filename in os.listdir(guides_dir):
    if filename.endswith(".md"):
        total_files_count += 1  # Increment total files counter
        filepath = os.path.join(guides_dir, filename)
        
        with open(filepath, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            
            # Skip over any leading empty lines
            first_non_empty_line = next((line for line in lines if line.strip()), "")
            
            if first_non_empty_line.startswith("#"):
                parts = first_non_empty_line[1:].split(":", 1)  # Remove '#' and split on the first ':'
                if len(parts) == 2:
                    code = parts[0].strip()
                    description = parts[1].strip()
                else:
                    print(f"Skipping {filename}: Unable to parse code and description.")
                    skipped_files_count += 1
                    continue
            else:
                print(f"Skipping {filename}: Invalid format.")
                skipped_files_count += 1
                continue
        
        # Generate troubleshooting steps
        troubleshooting_steps = generate_troubleshooting_steps(code, description)
        
        # Append troubleshooting steps to the file content
        updated_content = content + "\n\n## Troubleshooting Steps\n" + troubleshooting_steps
        
        # Save the updated content back to the file
        with open(filepath, 'w') as file:
            file.write(updated_content)
        
        print(f"Updated {filename} with troubleshooting steps.")

# Print the total number of evaluated and skipped files
print(f"\nTotal files evaluated: {total_files_count}")
print(f"Total number of skipped files due to invalid format: {skipped_files_count}")
