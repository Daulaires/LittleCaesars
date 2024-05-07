import time
import requests
import argparse
import random
import string

def sendSpam(email,times):
    url = "http://127.0.0.1:999/v1/spam"

    # Build the headers and request body
    data = {
            "email": f"{email}",
            "times": f"{times}"
           }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'http://127.0.0.1:999',
        'Referer': 'http://127.0.0.1:999/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # Create a session
    session = requests.Session()

    # Make the POST request
    response = session.post(url, json=data, headers=headers)

    # Check the response
    if response.status_code == 200:
        # make it green 
        print("\033[92m" + data['email'] + "\033[0m " + "\033[92m" + data['times'] + "\033[0m" + f" Status: {response.status_code}")
    else:
        print("\033[91m" + "Request failed." + "\033[0m")
        print(response.text)
        
def createAccount(email,password):
    url = "http://127.0.0.1:999/v1/create"

    # Build the headers and request body
    data = {
            "email": f"{email}",
            "password": f"{password}"
           }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'http://127.0.0.1:999',
        'Referer': 'http://127.0.0.1:999/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # Create a session
    session = requests.Session()

    # Make the POST request
    response = session.post(url, json=data, headers=headers)

    # Check the response
    if response.status_code == 200:
        # print the response if it is successful
        responseText = response.text.replace('\n', '')
        for (key, value) in data.items():
            responseText = responseText.replace(value, "\033[92m" + value + "\033[0m")
            
        print(responseText)
    else:
        print("\033[91m" + response.json()['data'].replace('\n', '') + "\033[0m")

def GetRandomAccountRequest():
    # /v1/create_account_with_random_data
    url = "http://127.0.0.1:999/v1/create_account_with_random_data"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("\033[92m" + "Request successful." + "\033[0m")
        print(response.text)
    else:
        print("\033[91m" + "Request failed." + "\033[0m")
        print(response.text)

def random_account_custom():
    email_base = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = email_base + '@gmail.com'
    
    # Generate a list of characters for the password that does not include any characters from the email
    password_chars = list(string.ascii_lowercase + string.digits)
    for char in email_base:
        if char in password_chars:
            password_chars.remove(char)
    
    # Shuffle the list of characters for the password
    random.shuffle(password_chars)
    
    # Select the first 7 characters from the shuffled list to form the password
    password = ''.join(password_chars[:7])
    
    # Add a capital letter to the password to ensure it meets the criteria
    password += random.choice(string.ascii_uppercase)
    password = password[:1].upper() + password[1:] # Ensure the first character is uppercase
    # add in 2 capital letters
    password += ''.join(random.choices(string.ascii_uppercase, k=2))
    # Now, password is guaranteed to be 8 characters long, have at least one capital letter, and not contain the same characters as the email
    createAccount(email, password)
        
parser = argparse.ArgumentParser(description="Test 'Hack' to post request to webserver.")
subparsers = parser.add_subparsers(dest="command")

spam_parser = subparsers.add_parser('spam', help='Spam the email.')
spam_parser.add_argument('email', type=str, help='The email to spam.')
spam_parser.add_argument('times', type=int, help='The number of times to spam the email.', default=1)

create_account_parser = subparsers.add_parser('create_account', help='Create an account.')
create_account_parser.add_argument('email', type=str, help='The email to create an account for.')
create_account_parser.add_argument('password', type=str, help='The password for the account.')

random_account_parser = subparsers.add_parser('random_account_custom', help='Create a random account.')
random_account_parser.add_argument('times',type=int, default=1)

random_account_parser_request = subparsers.add_parser('random_account_request', help='Create a random account via Get Requests.')
random_account_parser_request.add_argument('times',type=int, default=1)

# python rawPostToWebserver.py spam email times

args = parser.parse_args()

if args.command == "spam":
    sendSpam(args.email, args.times)
elif args.command == "create_account":
    createAccount(args.email, args.password)
elif args.command == "random_account_custom":
    for i in range(args.times):
        random_account_custom()
elif args.command == "random_account_request":
    for i in range(args.times):
        # make it sleep for 4 seconds
        time.sleep(4)
        GetRandomAccountRequest()
elif args.times == None:
    print("[!] python index.py email times")
else:
    print("No command given.")
