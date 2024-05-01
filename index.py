from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def test(driver):
    # Select the div with the class 'css-1fpjypo'
    try:
        div = driver.find_element(By.CSS_SELECTOR, '.css-1fpjypo')

        # Find the first button within this div and click it
        button = div.find_element(By.TAG_NAME, 'button')
        button.click()
        return True  # Indicate success
    except NoSuchElementException:
        return False  # Indicate failure

def click_forgot_password_link(driver):
    # Attempt to click the "Forgot Password?" link
    try:
        forgot_password_link = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="login-form__forgot-password-link"]')
        forgot_password_link.click()
        print("Clicked on Forgot Password link.")
    except NoSuchElementException:
        print("Forgot Password link not found.")

def enter_email(driver, email):
    # Locate the input field by its class name and enter the email
    try:
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="forgotPassword__email"]')
        email_input.clear()  # Clear any existing text
        email_input.send_keys(email)  # Enter the email
        print(f"Entered email: {email}")
    except NoSuchElementException:
        print("Email input field not found.")

# Setup Chrome options
options = webdriver.ChromeOptions()

# Specify the path to your ChromeDriver executable
driver = webdriver.Chrome(options=options)

# Navigate to the page
driver.get('https://littlecaesars.com/en-us/login/')

# Ask the user for the email address
time.sleep(15)  # Wait for 1 second
given_email = input("Please enter your email address: ")

# Automate the clicks
for i in range(100):
    if test(driver):
        # Enter the given email
        enter_email(driver, given_email)
        time.sleep(1)  # Wait for 1 second
    else:
        click_forgot_password_link(driver)
        time.sleep(1)  # Wait for 1 second between actions

driver.quit()
