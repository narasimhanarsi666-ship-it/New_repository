from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("path/to/chromedriver")  # Replace with the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Application URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

try:
    # Test Case 1: Accessing the Login Page
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
    print("Login page accessed successfully.")

    # Test Case 2: Successful Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
    print("Login successful. Dashboard accessed.")

    # Test Case 3: Invalid Login Attempt
    driver.get(url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("InvalidUser")
    password.send_keys("InvalidPass")
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")))
    print(f"Invalid login attempt error message: {error_message.text}")

    # Test Case 4: Password Masking
    driver.get(url)
    password = driver.find_element(By.NAME, "password")
    if password.get_attribute("type") == "password":
        print("Password field is masked.")
    else:
        print("Password field is not masked.")

    # Test Case 5: 'Forgot Password' Link Functionality
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
    forgot_password_link.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "forgotPasswordForm")))
    print("Forgot Password page accessed successfully.")

    # Test Case 6: 'Remember Me' Option Functionality
    driver.get(url)
    remember_me_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox"]")
    remember_me_checkbox.click()
    if remember_me_checkbox.is_selected():
        print("Remember Me option selected successfully.")
    else:
        print("Failed to select Remember Me option.")

    # Test Case 7: Account Lockout After Repeated Failed Attempts
    for attempt in range(5):  # Assuming 5 attempts trigger lockout
        driver.get(url)
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("Admin")
        password.send_keys("WrongPassword")
        login_button.click()
        time.sleep(2)  # Adding delay between attempts

    lockout_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")))
    print(f"Account lockout message: {lockout_message.text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()