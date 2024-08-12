import os
import openai

# Your OpenAI API key
openai.api_key = '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'  # Replace with your actual API key

# Base directory where the guides are located
base_guides_dir = r"C:\Users\joser\EntraIDcampjo\guides"

# Initialize counters for evaluated, skipped, and updated files
total_files_count = 0
skipped_files_count = 0
updated_files_count = 0

# Function to generate troubleshooting steps
def generate_troubleshooting_steps(code, description):
    prompt = f"""
    For the error code {code} with the following description: "{description}",
    - Provide a detailed troubleshooting guide.
    - Initial diagnostic steps
    - Common issues that cause this error
    - Step-by-step resolution strategies
    - Additional notes or considerations
    - Documentation where steps can be found for guidance
    - Advice for data collection event viewer logs, nettrace, fiddler if related to the issue
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
            # Get the troubleshooting guide
            guide = response['choices'][0]['message']['content'].strip()
            return guide
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
for filename in os.listdir(base_guides_dir):
    if filename.endswith(".md"):
        total_files_count += 1  # Increment total files counter
        filepath = os.path.join(base_guides_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            print(f"Skipping {filename}: Unable to read the file in utf-8 encoding.")
            skipped_files_count += 1
            continue

        lines = content.splitlines()
        
        # Skip over any leading empty lines
        first_non_empty_line = next((line for line in lines if line.strip()), "")
        
        if first_non_empty_line.startswith("#"):
            parts = first_non_empty_line[1:].split(":", 1)  # Remove '#' and split on the first ':'
            if len(parts) == 2:
                code = parts[0].strip()
                description = parts[1].strip()
                
                # Check if the file already contains troubleshooting steps
                if "## Troubleshooting Steps" in content:
                    print(f"Skipping {filename}: Troubleshooting steps already exist.")
                    skipped_files_count += 1
                    continue
                
                # Get the troubleshooting steps from OpenAI
                troubleshooting_steps = generate_troubleshooting_steps(code, description)
                
                # Add troubleshooting steps to the content
                updated_content = content + f"\n\n## Troubleshooting Steps\n" + troubleshooting_steps

                # Save the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(updated_content)

                print(f"Updated {filename}.")
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
print(f"Total number of skipped files due to existing troubleshooting steps or invalid format: {skipped_files_count}")
print(f"Total number of files updated: {updated_files_count}")
