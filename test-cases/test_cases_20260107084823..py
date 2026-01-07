from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Initialize the WebDriver
service = Service('path_to_chromedriver')  # Replace with the path to your chromedriver
driver = webdriver.Chrome(service=service)

# Test Case: Login Functionality
try:
    # Step 1: Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("Navigated to the login page.")

    # Step 2: Input validation - Enter username and password
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    print("Entered username and password.")

    # Step 3: Click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    print("Clicked the login button.")

    # Step 4: Verify successful login
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
        print("Login successful. Dashboard is displayed.")
    except TimeoutException:
        print("Login failed. Dashboard not displayed.")

    # Step 5: Optional Features - Verify "Forgot Password" link
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
    if forgot_password_link.is_displayed():
        print('"Forgot Password" link is visible and functional.')

    # Step 6: Security - Verify password masking
    if password_field.get_attribute("type") == "password":
        print("Password field is masked.")

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except TimeoutException as e:
    print(f"Timeout occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
    print("Test completed and browser closed.")