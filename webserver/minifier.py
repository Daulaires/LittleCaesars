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
    
    # Prepend a self-executing anonymous function to disable console usage
    combined_content = combined_content.replace("console.log", "").replace("console.error", "")
    
    # Replace long variable names with shorter ones / "obfuscation"
    variable_replacements = {
        "url": "U",
        "message": "m",
        "fullUrl": "fU",
        "response": "r",
        "showMenu": "sM",
        "hideMenu": "hM",
        "updateData": "uD",
        "postHeaders": "pH",
        "handleError": "hE",
        "requestBody": "rB",
        "handleSubmit": "hS",
        "toggleButton": "tB",
        "menuContainer": "mC",
        "handleResponse": "hR",
        "accountsCreated": "aC",
        "showNotification": "sN",
        "_notification_": "N",
        "_NotificationContainer_": "nC",
        "sendPostRequest": "sPR",
        "SpamFormElement": "sFE",
        "prefersDarkMode": "pDM",
        "menuToggleButton": "mTB",
        "updateButtonText": "uBT",
        "handleMenuToggle": "hMT",
        "randomAccountBody": "rAB",
        "createRequestBody": "cRB",
        "RandomAccountButton": "RAB",
        "createAccountSubmit": "cAS",
        "toggleSpamFormButton": "tSFB",
        "GetGlobalTimesCounter": "gGTC",
        "globalTimesCounter": "gTC",
        "createAccountFormElement": "cAFE",
        "toggleCreateAccountFormButton": "tCAFB"
    }

    for variable, replacement in variable_replacements.items():
        combined_content = combined_content.replace(variable, replacement)
    
    combined_content = f"(function(){{\n{combined_content}\n}})();"
    
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
