# 
# This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
# This was made for educational purposes only.
# Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
# Date: 2024-05-02
# 

import os
import tempfile
from flask import Flask, jsonify, render_template, request, abort
import logging

app = Flask(__name__, template_folder='templates')
processing_emails = {}
accounts = {}

@app.route('/')
def index():
    logging.info("Index page accessed")
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    logging.info("Received POST request to send spam")
    
    # Extract data from the request
    data = request.get_json()
    email = data.get('email')
    times = data.get('times')

    # Check if the email is already being processed
    if email in processing_emails and processing_emails[email]:
        logging.info(f"Skipping email {email} as it's already being processed.")
        return jsonify({"status": "skip", "message": f"Email {email} is already being processed."}), 200

    # Mark the email as being processed
    processing_emails[email] = True
    logging.info(f"Processing email: {email}, times: {times}")
    
    # Create a temporary file to store the output of the script
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()

    # Run the python script and redirect its output to the temporary file
    os.system(f'python static/python/index.py spam {email} {times} > {temp_file.name}')

    # Read the output from the temporary file
    with open(temp_file.name, 'r') as f:
        output = f.read()

    # Log the completion of the spamming process
    logging.info(f"Completed processing email: {email}")
    
    # Mark the email as no longer being processed
    processing_emails[email] = False
    
    # Return a success message along with the script output
    return jsonify({"status": "success", "message": f"Email {email} spamming completed.\n{output}"}), 200

@app.route('/create_account', methods=['POST'])
def create_account():
    logging.info("Received POST request to create account")
    
    # Extract data from the request
    data = request.get_json()
    print(data)
    email = data.get('email')
    password = data.get('password')  # Assuming you have a password field for account creation

    # Basic validation
    if not email or not password:
        abort(400, description="Missing email or password")

    # Check if the email is already registered
    if email in accounts:
        abort(400, description=f"Email {email} is already registered.")

    # Here you would typically store the account details in a database
    # For demonstration, we'll just add it to a dictionary
    accounts[email] = {"password": password}  # Storing password in plain text is insecure in real applications

    logging.info(f"Account created for email: {email}")
    
    return jsonify({"status": "success", "message": f"Account created for email: {email}."}), 201

if __name__ == '__main__':
    app.run(debug=True)
