import os
import rjsmin
import io

def clear_output_file(output_file):
    with open(output_file, 'w') as file:
        file.write("")  # Write an empty string to clear the file

def minify_js_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Minify the content
        minified_content = rjsmin.jsmin(content)
        
        # Return the minified content
        return minified_content
    except Exception as e:
        print(f"Error minifying {file_path}: {e}")
        # Return an empty string in case of error
        return ""

def combine_js_files(directory, output_file):
    combined_content = ""
    for root, dirs, files in os.walk(directory):
        print(f"Processing {len(files)} JavaScript files in {root}...")
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                minified_content = minify_js_file(file_path)
                if minified_content:  # Only append if minified_content is not an empty string
                    # Prepend a newline character to ensure proper spacing
                    combined_content += "\n" + minified_content
    
    # Prepend a simple JavaScript function declaration to avoid missing function errors
    combined_content = combined_content
    
    # Write the combined content to the output file
    with open(output_file, 'w') as file:
        file.write(combined_content)

    # Optionally, log the number of files processed
    print(f"Processed {len(files)} JavaScript files.")
    
def check_if_runable_js(output_file):
    with open(output_file, 'r') as file:
        content = file.read()
    if content.startswith("function") or content.startswith("const") or content.startswith("let") or content.startswith("var"):
        return True
    else:
        return False

# Specify the directory and output file
directory = './static/js'
output_file = './static/js/bundle.js'

# We will clear the output file before combining the JavaScript files
clear_output_file(output_file)

# Minify each JavaScript file and combine them
combine_js_files(directory, output_file)

# Check if the runnable JS condition is met
check_if_runable_js(output_file=output_file)

print(f"All JavaScript files in {directory} have been minified and combined into {output_file}.")
