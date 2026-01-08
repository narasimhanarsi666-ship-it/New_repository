from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Test Case 1: Access Login Page
def test_access_login_page():
    # Setup WebDriver with Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Navigate to the login page URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Validate the login page is displayed
        assert "OrangeHRM" in driver.title, "Login page title does not match."
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        assert username_field.is_displayed(), "Username field is not displayed."
        assert password_field.is_displayed(), "Password field is not displayed."

        print("Test Case 1 Passed: Access Login Page")
    finally:
        # Close the browser
        driver.quit()

# Test Case 2: Successful Login with Valid Credentials
def test_successful_login():
    # Setup WebDriver with Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Navigate to the login page URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Step 2: Enter valid username and password
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")

        # Step 3: Click the 'Login' button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Validate successful login by checking the dashboard page
        time.sleep(3)  # Wait for redirection
        assert "dashboard" in driver.current_url.lower(), "User was not redirected to the dashboard."

        print("Test Case 2 Passed: Successful Login with Valid Credentials")
    finally:
        # Close the browser
        driver.quit()

# Test Case 3: Login Attempt with Empty Username and Password
def test_empty_login_fields():
    # Setup WebDriver with Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Navigate to the login page URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Step 2: Leave username and password fields empty and click 'Login'
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Validate error message
        error_message = driver.find_element(By.XPATH, "//span[contains(text(),'Required')]")
        assert error_message.is_displayed(), "Error message for empty fields is not displayed."

        print("Test Case 3 Passed: Login Attempt with Empty Username and Password")
    finally:
        # Close the browser
        driver.quit()

# Test Case 4: Login Attempt with Invalid Credentials
def test_invalid_login():
    # Setup WebDriver with Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Navigate to the login page URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Step 2: Enter invalid username and password
        driver.find_element(By.NAME, "username").send_keys("InvalidUser")
        driver.find_element(By.NAME, "password").send_keys("InvalidPass")

        # Step 3: Click the 'Login' button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Validate error message
        error_message = driver.find_element(By.XPATH, "//p[contains(text(),'Invalid credentials')]")
        assert error_message.is_displayed(), "Error message for invalid credentials is not displayed."

        print("Test Case 4 Passed: Login Attempt with Invalid Credentials")
    finally:
        # Close the browser
        driver.quit()

# Run the test cases
if __name__ == "__main__":
    test_access_login_page()
    test_successful_login()
    test_empty_login_fields()
    test_invalid_login()