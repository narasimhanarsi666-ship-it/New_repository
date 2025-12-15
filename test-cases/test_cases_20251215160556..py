from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Parameterized values for flexibility
URL = "https://example.com/login"
USERNAME = "your_username"
PASSWORD = "your_password"

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(URL)

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Locate username field and enter username
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys(USERNAME)

    # Locate password field and enter password
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(PASSWORD)

    # Locate and click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # Optional: Verify login success (example: check for a specific element)
    success_element = wait.until(EC.presence_of_element_located((By.ID, "success-element")))
    print("Login successful!")

except NoSuchElementException as e:
    print(f"Error: Element not found - {e}")
except TimeoutException as e:
    print(f"Error: Timeout occurred - {e}")
except Exception as e:
    print(f"An unexpected error occurred - {e}")
finally:
    # Ensure the browser session is closed
    driver.quit()