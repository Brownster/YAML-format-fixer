import re
import os
import sys
import difflib

def adjust_comment_indentation(lines):
    new_lines = []  # Ensure new_lines is initialized
    for i, line in enumerate(lines):
        stripped_line = line.lstrip()
        if stripped_line.startswith("#"):
            next_line_index = i + 1
            while next_line_index < len(lines) and not lines[next_line_index].strip():
                next_line_index += 1
            if next_line_index < len(lines):
                next_line_indentation = len(lines[next_line_index]) - len(lines[next_line_index].lstrip())
                line = " " * next_line_indentation + stripped_line
        new_lines.append(line)
    return new_lines  # Return the new_lines list


def process_yaml_files(directory, file_extension=".eyaml"):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                original_lines = file.readlines()

            modified_lines = [line.rstrip() + '\n' for line in original_lines]
            if modified_lines and not modified_lines[0].strip().startswith('---'):
                modified_lines.insert(0, '---\n')

            modified_lines = adjust_comment_indentation(modified_lines)
            if modified_lines[-1].strip() == '---':
                modified_lines.pop()

            modified_lines = [line for i, line in enumerate(modified_lines) if i == 0 or not (line.isspace() and modified_lines[i - 1].isspace())]

            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)

            # Create and write the change report
            change_report = difflib.unified_diff(original_lines, modified_lines, fromfile=filename, tofile=filename, lineterm='\n')
            change_filename = os.path.splitext(filename)[0] + '-changes.txt'
            change_filepath = os.path.join(directory, change_filename)
            with open(change_filepath, 'w', encoding='utf-8') as change_file:
                change_file.writelines(change_report)

            print(f"Processed {filename}. Change report written to {change_filename}")

if __name__ == "__main__":
    # Get the directory path from command line argument
    if len(sys.argv) > 1:
        yaml_directory = sys.argv[1]
        process_yaml_files(yaml_directory)
    else:
        print("Please provide the directory path as an argument.")
