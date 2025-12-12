# Python Selenium Script for Test Case TC001: Access Login Page from Main Screen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the main screen (replace 'https://example.com' with the actual URL)
    driver.get("https://example.com")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Locate and click on the 'Login' button/link
    login_button = driver.find_element(By.LINK_TEXT, "Login")  # Adjust locator as needed
    login_button.click()
    time.sleep(2)  # Wait for the login page to load

    # Step 3: Verify that the login page is displayed
    assert "Login" in driver.title  # Adjust assertion as needed
    print("Test Case TC001 Passed: Login page is displayed.")

finally:
    # Close the browser session
    driver.quit()

# Python Selenium Script for Test Case TC002: Input Validation - Empty Fields
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page (replace 'https://example.com/login' with the actual URL)
    driver.get("https://example.com/login")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Leave the email/username and password fields empty and click the 'Login' button
    login_button = driver.find_element(By.ID, "loginButton")  # Adjust locator as needed
    login_button.click()
    time.sleep(2)  # Wait for validation messages to appear

    # Step 3: Verify validation messages are displayed
    email_error = driver.find_element(By.ID, "emailError")  # Adjust locator as needed
    password_error = driver.find_element(By.ID, "passwordError")  # Adjust locator as needed
    assert email_error.is_displayed() and password_error.is_displayed()
    print("Test Case TC002 Passed: Validation messages are displayed for empty fields.")

finally:
    # Close the browser session
    driver.quit()

# Python Selenium Script for Test Case TC003: Successful Login with Valid Credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page (replace 'https://example.com/login' with the actual URL)
    driver.get("https://example.com/login")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Enter valid email/username and password
    email_field = driver.find_element(By.ID, "email")  # Adjust locator as needed
    password_field = driver.find_element(By.ID, "password")  # Adjust locator as needed
    email_field.send_keys("valid_user@example.com")  # Replace with valid credentials
    password_field.send_keys("valid_password")  # Replace with valid credentials

    # Step 3: Click the 'Login' button
    login_button = driver.find_element(By.ID, "loginButton")  # Adjust locator as needed
    login_button.click()
    time.sleep(2)  # Wait for redirection to the dashboard/home page

    # Step 4: Verify redirection to the dashboard/home page
    assert "Dashboard" in driver.title  # Adjust assertion as needed
    print("Test Case TC003 Passed: User successfully logged in and redirected to the dashboard.")

finally:
    # Close the browser session
    driver.quit()

# Python Selenium Script for Test Case TC004: Login Attempt with Invalid Credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page (replace 'https://example.com/login' with the actual URL)
    driver.get("https://example.com/login")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Enter invalid email/username or password
    email_field = driver.find_element(By.ID, "email")  # Adjust locator as needed
    password_field = driver.find_element(By.ID, "password")  # Adjust locator as needed
    email_field.send_keys("invalid_user@example.com")  # Replace with invalid credentials
    password_field.send_keys("invalid_password")  # Replace with invalid credentials

    # Step 3: Click the 'Login' button
    login_button = driver.find_element(By.ID, "loginButton")  # Adjust locator as needed
    login_button.click()
    time.sleep(2)  # Wait for the error message to appear

    # Step 4: Verify the error message is displayed
    error_message = driver.find_element(By.ID, "loginError")  # Adjust locator as needed
    assert error_message.is_displayed()
    print("Test Case TC004 Passed: Error message displayed for invalid credentials.")

finally:
    # Close the browser session
    driver.quit()