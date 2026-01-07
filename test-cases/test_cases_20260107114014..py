from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test Case: TC001 - Access the Login Page
# Description: Verify that the user can access the login page from the main screen.

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the main screen of the application
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Verify that the URL corresponds to the login page
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    assert driver.current_url == expected_url, f"URL mismatch! Expected: {expected_url}, Found: {driver.current_url}"

    # Step 3: Verify the presence of necessary fields and elements
    assert driver.find_element(By.NAME, "username"), "Username field is missing!"
    assert driver.find_element(By.NAME, "password"), "Password field is missing!"
    assert driver.find_element(By.LINK_TEXT, "Forgot your password?"), "Forgot Password link is missing!"
    assert driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='remember']"), "Remember Me checkbox is missing!"

    print("Test Case TC001 Passed: Login page is displayed correctly with all necessary fields and elements.")

finally:
    # Close browser session
    driver.quit()