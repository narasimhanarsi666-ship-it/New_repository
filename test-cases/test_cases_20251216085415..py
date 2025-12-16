# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Test Case 1: Access Login Page from Main Screen
def test_access_login_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
        # Navigate to the main screen
        logging.info("Navigating to the main screen...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        # Verify the URL
        assert "auth/login" in driver.current_url, "Login page URL is incorrect."
        
        # Verify the presence of login form elements
        logging.info("Verifying the presence of login form elements...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        logging.info("Login page elements are displayed correctly.")
    except TimeoutException:
        logging.error("Login page elements are not loaded within the expected time.")
        raise
    finally:
        driver.quit()

# Test Case 2: Successful Login with Valid Credentials
def test_successful_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
        # Navigate to the login page
        logging.info("Navigating to the login page...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        # Enter valid credentials
        logging.info("Entering valid credentials...")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit'"]).click()
        
        # Verify redirection to the dashboard
        logging.info("Verifying redirection to the dashboard...")
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url, "Redirection to dashboard failed."
        logging.info("Login successful and user is redirected to the dashboard.")
    except TimeoutException:
        logging.error("Dashboard page is not loaded within the expected time.")
        raise
    finally:
        driver.quit()

# Test Case 3: Login Attempt with Invalid Credentials
def test_invalid_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
        # Navigate to the login page
        logging.info("Navigating to the login page...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        # Enter invalid credentials
        logging.info("Entering invalid credentials...")
        driver.find_element(By.NAME, "username").send_keys("InvalidUser")
        driver.find_element(By.NAME, "password").send_keys("wrongPass")
        driver.find_element(By.XPATH, "//button[@type='submit'"]).click()
        
        # Verify error message
        logging.info("Verifying error message for invalid credentials...")
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
        )
        assert "Invalid credentials" in error_message.text, "Error message is incorrect or not displayed."
        logging.info("Error message displayed correctly for invalid credentials.")
    except TimeoutException:
        logging.error("Error message is not displayed within the expected time.")
        raise
    finally:
        driver.quit()

# Additional test cases can be implemented following the same structure.

# Run tests
if __name__ == "__main__":
    pytest.main()