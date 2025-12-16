from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH
driver.maximize_window()

# Define constants
BASE_URL = "https://example.com"  # Replace with the actual URL of the application
LOGIN_PAGE_URL = f"{BASE_URL}/login"
USERNAME = "testuser@example.com"  # Replace with valid test credentials
PASSWORD = "password123"  # Replace with valid test credentials

def access_login_page():
    """
    Test Case: Access the login page from the main screen.
    """
    try:
        driver.get(BASE_URL)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_button.click()
        assert driver.current_url == LOGIN_PAGE_URL, "Failed to navigate to the login page."
        print("Access Login Page: Passed")
    except (TimeoutException, AssertionError) as e:
        print(f"Access Login Page: Failed - {e}")

def validate_input_fields():
    """
    Test Case: Validate input fields for email/username and password.
    """
    try:
        driver.get(LOGIN_PAGE_URL)
        email_field = driver.find_element(By.ID, "email")  # Replace with the actual ID
        password_field = driver.find_element(By.ID, "password")  # Replace with the actual ID
        
        # Check if fields are displayed
        assert email_field.is_displayed(), "Email field is not displayed."
        assert password_field.is_displayed(), "Password field is not displayed."
        
        # Check required field validation
        login_button = driver.find_element(By.ID, "loginButton")  # Replace with the actual ID
        login_button.click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message")  # Replace with the actual class
        assert "required" in error_message.text.lower(), "Required field validation failed."
        print("Validate Input Fields: Passed")
    except (NoSuchElementException, AssertionError) as e:
        print(f"Validate Input Fields: Failed - {e}")

def test_successful_login():
    """
    Test Case: Log in with valid credentials.
    """
    try:
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(By.ID, "email