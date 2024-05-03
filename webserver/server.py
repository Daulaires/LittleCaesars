# 
# This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
# This was made for educational purposes only.
# Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
# Date: 2024-05-02
# 
import json
import os
import tempfile
from flask import Flask, jsonify, render_template, request, abort
import logging

app = Flask(__name__, template_folder='templates')
processing_emails = {}
accounts = {}

# include the global_spam_count.json file
global_spam_count_file = 'static/data/global_spam_count.json'

# make it a app.route
@app.route('/get_global_spam_count', methods=['GET'])
def get_global_spam_count():
    logging.info("Received GET request to get global spam count")
    with open(global_spam_count_file, 'r') as file:
        global_spam_count = json.load(file)
    return jsonify(global_spam_count), 200

@app.route('/')
def index():
    logging.info("Index page accessed")
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    logging.info("Received POST request to send spam")
    data = request.get_json()
    email = data.get('email')
    times = data.get('times')
    if email in processing_emails and processing_emails[email]:
        logging.info(f"Skipping email {email} as it's already being processed.")
        return jsonify({"status": "skip", "message": f"Email {email} is already being processed."}), 200
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
    # Load the current global spam count
    with open(global_spam_count_file, 'r') as file:
        global_spam_count = json.load(file)
    # Convert times to an integer before incrementing the global spam count
    times = int(times) # Convert times to an integer
    # Increment the global spam count
    global_spam_count['total_spam_count'] += times
    # Save the updated global spam count
    with open(global_spam_count_file, 'w') as file:
        json.dump(global_spam_count, file, indent=4)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    os.system(f'python static/python/LCSpammer.py spam {email} {times} > {temp_file.name}')
    os.system(f'ipconfig /flushdns')
    logging.info(f"Completed processing email: {email}")
    processing_emails[email] = False
    return jsonify({"status": "success", "message": f"Email {email} spamming completed. Emails Sent: {times}"}), 200

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
    os.system(f'python static/python/LCSpammer.py create_account {email} {password}')
    # For demonstration, we'll just add it to a dictionary
    accounts[email] = {"password": password}  # Storing password in plain text is insecure in real applications
    logging.info(f"Account created for email: {email}")
    return jsonify({"status": "success", "message": f"Account created for email: {email}."}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=999,debug=True)
