from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Test Case 1: Accessing the Login Page
def test_access_login_page():
    try:
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")
        assert "Login" in driver.title
        print("Test Case 1 Passed: Login page accessed successfully.")
    except Exception as e:
        print(f"Test Case 1 Failed: {e}")
    finally:
        driver.quit()

# Test Case 2: Successful Login with Valid Credentials
def test_successful_login():
    try:
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")
        
        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("valid_user")
        
        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("valid_password")
        
        # Click login button
        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()
        
        # Wait for successful login indication
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "welcomeMessage"))
        )
        print("Test Case 2 Passed: Successfully logged in with valid credentials.")
    except Exception as e:
        print(f"Test Case 2 Failed: {e}")
    finally:
        driver.quit()

# Test Case 3: Login Attempt with Invalid Credentials
def test_invalid_login():
    try:
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")
        
        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("invalid_user")
        
        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("invalid_password")
        
        # Click login button
        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()
        
        # Wait for error message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        print("Test Case 3 Passed: Error message displayed for invalid credentials.")
    except Exception as e:
        print(f"Test Case 3 Failed: {e}")
    finally:
        driver.quit()

# Main execution
if __name__ == "__main__":
    test_access_login_page()
    test_successful_login()
    test_invalid_login()