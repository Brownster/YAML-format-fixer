import re
import os

def process_yaml_files(directory, file_extension=".eyaml"):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory, filename)
            
            # Read the contents of the file
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Normalize line endings and ensure document start marker
            lines = [line.replace('\r\n', '\n') for line in lines]  # Convert line endings to Unix style
            if lines and not lines[0].strip().startswith('---'):
                lines.insert(0, '---\n')

            # Ensure space after '#' in comments
            lines = [re.sub(r'(^#)([^\s])', r'# \2', line) for line in lines]

            # Remove excess blank lines at the beginning
            while lines and lines[0].strip() == '':
                lines.pop(0)

            # Write the changes back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(lines)

            print(f"Processed {filename}")

# Define the path to your directory containing YAML files
yaml_directory = "/home/marc/Downloads/nodes/"  # Replace with your directory path

# Run the function on your directory
process_yaml_files(yaml_directory)
