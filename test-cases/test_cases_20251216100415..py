from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

# Initialize WebDriver
def initialize_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service("path/to/chromedriver")  # Replace with the actual path to chromedriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except WebDriverException as e:
        print(f"Error initializing WebDriver: {e}")
        return None

# Test Case: Access Login Page
def test_access_login_page(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert "OrangeHRM" in driver.title, "Login page title does not match."
        print("Test Case: Access Login Page - Passed")
    except AssertionError as e:
        print(f"Test Case: Access Login Page - Failed: {e}")
    except Exception as e:
        print(f"Test Case: Access Login Page - Error: {e}")

# Test Case: Successful Login
def test_successful_login(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit"]")
        
        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        login_button.click()
        
        time.sleep(3)  # Wait for the page to load
        assert "dashboard" in driver.current_url, "User not redirected to dashboard after login."
        print("Test Case: Successful Login - Passed")
    except NoSuchElementException as e:
        print(f"Test Case: Successful Login - Failed: Element not found - {e}")
    except AssertionError as e:
        print(f"Test Case: Successful Login - Failed: {e}")
    except Exception as e:
        print(f"Test Case: Successful Login - Error: {e}")

# Test Case: Input Validation
def test_input_validation(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit"]")
        login_button.click()
        
        time.sleep(1)  # Wait for validation messages
        username_error = driver.find_element(By.XPATH, "//span[contains(text(), 'Required')]")
        password_error = driver.find_element(By.XPATH, "//span[contains(text(), 'Required')]")
        
        assert username_error.is_displayed(), "Username validation error not displayed."
        assert password_error.is_displayed(), "Password validation error not displayed."
        print("Test Case: Input Validation - Passed")
    except NoSuchElementException as e:
        print(f"Test Case: Input Validation - Failed: Element not found - {e}")
    except AssertionError as e:
        print(f"Test Case: Input Validation - Failed: {e}")
    except Exception as e:
        print(f"Test Case: Input Validation - Error: {e}")

# Test Case: Password Masking
def test_password_masking(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        password_field = driver.find_element(By.NAME, "password")
        assert password_field.get_attribute("type") == "password", "Password field is not masked."
        print("Test Case: Password Masking - Passed")
    except NoSuchElementException as e:
        print(f"Test Case: Password Masking - Failed: Element not found - {e}")
    except AssertionError as e:
        print(f"Test Case: Password Masking - Failed: {e}")
    except Exception as e:
        print(f"Test Case: Password Masking - Error: {e}")

# Main Execution
if __name__ == "__main__":
    driver = initialize_driver()
    if driver:
        try:
            test_access_login_page(driver)
            test_successful_login(driver)
            test_input_validation(driver)
            test_password_masking(driver)
        finally:
            driver.quit()