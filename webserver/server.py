import os
import tempfile
from flask import Flask, jsonify, render_template, request
import logging

app = Flask(__name__, template_folder='templates')
processing_emails = {}

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
    os.system(f'python static/python/index.py {email} {times} > {temp_file.name}')

    # Read the output from the temporary file
    with open(temp_file.name, 'r') as f:
        output = f.read()

    # Log the completion of the spamming process
    logging.info(f"Completed processing email: {email}")
    
    # Mark the email as no longer being processed
    processing_emails[email] = False
    
    # Return a success message along with the script output
    return jsonify({"status": "success", "message": f"Email {email} spamming completed.\n{output}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
