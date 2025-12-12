from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the main screen of the application
    driver.get("https://example.com")  # Replace with the actual URL of the application
    time.sleep(2)  # Wait for the page to load

    # Step 2: Locate and click the 'Login' button/link on the main screen
    login_button = driver.find_element(By.LINK_TEXT, "Login")  # Replace with the actual locator of the login button
    login_button.click()
    time.sleep(2)  # Wait for the login page to load

    # Expected Result: Verify that the user is navigated to the login page
    assert "Login" in driver.title  # Replace with the actual title or unique identifier of the login page
    print("Test Case TC001 Passed: User successfully navigated to the login page.")

except Exception as e:
    print(f"Test Case TC001 Failed: {str(e)}")

finally:
    # Close browser session
    driver.quit()