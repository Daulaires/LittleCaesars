# 
# This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
# This was made for educational purposes only.
# Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
# Date: 2024-05-02
# 
import hashlib
import json
import os
import subprocess
import tempfile
from flask import Flask, jsonify, render_template, request, abort
import logging
import re

app = Flask(__name__, template_folder='templates', static_folder='static')
processing_emails = {}
accounts = {}

# include the global_spam_count.json file
global_spam_count_file = 'static/data/global_spam_count.json'
accounts_created_file = 'static/data/accounts_created_count.json'

def validate_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(pattern, email))

def sanitize_password(password):
    # Remove special characters
    sanitized_password = ''.join(e for e in password if e.isalnum())
    # Hash the password for storage (for demonstration purposes)
    hashed_password = hashlib.sha256(sanitized_password.encode()).hexdigest()
    return hashed_password

def load_accounts_created_count():
    if not os.path.exists(accounts_created_file):
        with open(accounts_created_file, 'w') as file:
            json.dump({"total_accounts_created": 0}, file)
    with open(accounts_created_file, 'r') as file:
        return json.load(file)

def validate_positive_integer(value):
    try:
        num = int(value)
        if num > 0:
            return True
        else:
            return False
    except ValueError:
        return False

@app.route('/')
def index():
    logging.info("Index page accessed")
    return render_template('index.html')

@app.route('/v1/get_accounts_created_count', methods=['GET'])
def get_accounts_created_count():
    logging.info("Received GET request to get accounts created count")
    accounts_data = load_accounts_created_count()
    return jsonify(accounts_data), 200

@app.route('/v1/get_global_spam_count', methods=['GET'])
def get_global_spam_count():
    logging.info("Received GET request to get global spam count")
    with open(global_spam_count_file, 'r') as file:
        global_spam_count = json.load(file)
    return jsonify(global_spam_count), 200

@app.route('/v1/spam', methods=['POST'])
def send_spam():
    logging.info("Received POST request to send spam")
    
    data = request.get_json()
    email = data.get('email')
    times = data.get('times')
    
    # Validate and sanitize email
    if not validate_email(email):
        abort(400, description="Invalid email format")
    
    # Validate and sanitize times
    if not validate_positive_integer(times):
        abort(400, description="Invalid number of times")
    
    if email in processing_emails and processing_emails[email]:
        logging.info(f"Skipping email {email} as it's already being processed.")
        return jsonify({"status": "skip", "data": f"Email {email} is already being processed."}), 200
    
    processing_emails[email] = True
    logging.info(f"Processing email: {email}, times: {times}")
    
    # Check if the global spam count file exists and create it if not
    global_spam_count_file = 'static/data/global_spam_count.json'
    if not os.path.exists(global_spam_count_file):
        try:
            with open(global_spam_count_file, 'x') as file:
                file.write(json.dumps({"total_spam_count": 0}))
        except FileExistsError:
            # Handle the rare case where the file was created by another process after the check
            pass
        
    # Load the current global spam count
    with open(global_spam_count_file, 'r') as file:
        global_spam_count = json.load(file)
    
    # Convert times to an integer before incrementing the global spam count
    times = int(times) # Convert times to an integer
    
    # Increment the global spam count
    global_spam_count['total_spam_count'] += times * 2

    # Save the updated global spam count
    with open(global_spam_count_file, 'w') as file:
        json.dump(global_spam_count, file, indent=4)
    
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    
    # Create a temporary file for each spammer script
    temp_file_LC = tempfile.NamedTemporaryFile(delete=False)
    temp_file_WSS = tempfile.NamedTemporaryFile(delete=False)
    
    # Start processes for each spammer script
    process_LC = subprocess.Popen(['python', 'static/python/LCSpammer.py', 'spam', email, str(times)], stdout=open(temp_file_LC.name, 'w'))
    process_WSS = subprocess.Popen(['python', 'static/python/WSSpammer.py', 'spam', email, str(times)], stdout=open(temp_file_WSS.name, 'w'))
    
    # Wait for both processes to complete
    process_LC.wait()
    process_WSS.wait()

    os.system(f'ipconfig /flushdns')
    
    logging.info(f"Completed processing email: {email}")
    
    processing_emails[email] = False
    return jsonify({"status": "OK", "data": f"Email {email} spamming completed. Emails Sent: {times}"}), 200

@app.route('/v1/create', methods=['POST'])
def create_account():
    logging.info("Received POST request to create account")
    
    # Extract data from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password') # Assuming you have a password field for account creation
    
    if not validate_email(email):
        abort(400, description="Invalid email format")
        
    if not password:
        abort(400, description="Missing password")
    
    # Check if the email is already registered
    if email in accounts:
        abort(400, description=f"Email {email} is already registered.")
        
    os.system(f'python static/python/LCSpammer.py create_account {email} {password}')
    os.system(f'python static/python/WSSpammer.py create_account {email} Adfsdf Sdfsdf {password} 1')
    
    # For demonstration, we'll just add it to a dictionary
    accounts[email] = {"password": password} # Storing password in plain text is insecure in real applications
    logging.info(f"Account created for email: {email}")
    
    # Increment and save the total accounts created count
    accounts_data = load_accounts_created_count()
    accounts_data["total_accounts_created"] += 1
    with open(accounts_created_file, 'w') as file:
        json.dump(accounts_data, file)
    
    return jsonify({"status": "OK", "data": f"{email}"}), 200


@app.route('/v1/create_account_with_random_data', methods=['GET'])
def create_account_with_random_data():
    logging.info("Received POST request to create account with random data")
    
    # Create a temporary file for the output
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    
    # Start the process
    process = subprocess.Popen(['python', 'static/python/WSSpammer.py', 'create_account_with_random_data', '1'], stdout=open(temp_file.name, 'w'))

    # Wait for the process to complete
    process.wait()
    
    # Read the output
    with open(temp_file.name, 'r') as file:
        output = file.read()
    print(output)
    logging.info("Account created with random data")
    
    # Increment and save the total accounts created count
    accounts_data = load_accounts_created_count()
    accounts_data["total_accounts_created"] += 1
    with open(accounts_created_file, 'w') as file:
        json.dump(accounts_data, file)
    
    return jsonify({"status": "OK", "data": f"{output.replace('\n','').replace('[+] ','')}"}), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=999,debug=True)
