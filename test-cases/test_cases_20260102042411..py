from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
driver.maximize_window()

# Test Case TC001: Access Login Page
def test_access_login_page():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert "OrangeHRM" in driver.title
        print("TC001: Login page accessed successfully.")
    except Exception as e:
        print(f"TC001: Failed to access login page. Error: {e}")

# Test Case TC002: Input Validation
def test_input_validation():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        
        # Check if fields are present
        assert username_field.is_displayed()
        assert password_field.is_displayed()
        
        # Enter valid credentials
        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        print("TC002: Input validation passed.")
    except NoSuchElementException as e:
        print(f"TC002: Input validation failed. Element not found: {e}")
    except Exception as e:
        print(f"TC002: Input validation failed. Error: {e}")

# Test Case TC003: Authentication
def test_authentication():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Enter valid credentials and login
        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        login_button.click()
        
        # Wait for dashboard to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        print("TC003: Authentication successful.")
    except TimeoutException:
        print("TC003: Authentication failed. Dashboard did not load.")
    except Exception as e:
        print(f"TC003: Authentication failed. Error: {e}")

# Test Case TC004: Security
def test_security():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        password_field = driver.find_element(By.NAME, "password")
        
        # Check if password is masked
        assert password_field.get_attribute("type") == "password"
        print("TC004: Password field is masked.")
    except NoSuchElementException as e:
        print(f"TC004: Security test failed. Element not found: {e}")
    except Exception as e:
        print(f"TC004: Security test failed. Error: {e}")

# Test Case TC005: Error Handling
def test_error_handling():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Enter invalid credentials and login
        username_field.send_keys("InvalidUser")
        password_field.send_keys("InvalidPass")
        login_button.click()
        
        # Wait for error message
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'error-message')]")
        )
        assert "Invalid credentials" in error_message.text
        print("TC005: Error handling passed.")
    except TimeoutException:
        print("TC005: Error handling failed. Error message did not appear.")
    except Exception as e:
        print(f"TC005: Error handling failed. Error: {e}")

# Execute Test Cases
test_access_login_page()
test_input_validation()
test_authentication()
test_security()
test_error_handling()

# Close WebDriver
driver.quit()