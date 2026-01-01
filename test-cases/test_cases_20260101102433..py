from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Test Case TC001: Access Login Page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert "OrangeHRM" in driver.title
    print("TC001: Login page accessed successfully.")

    # Test Case TC002: Successful Login with Valid Credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    login_button.click()
    
    time.sleep(2)  # Wait for redirection
    assert "dashboard" in driver.current_url
    print("TC002: Successfully logged in and redirected to dashboard.")

    # Test Case TC003: Login Attempt with Missing Username Field
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    password_field.send_keys("admin123")
    login_button.click()
    
    error_message = driver.find_element(By.XPATH, "//span[contains(text(),'Required')]").text
    assert "Required" in error_message
    print("TC003: Error message displayed for missing username.")

    # Test Case TC004: Login Attempt with Missing Password Field
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field = driver.find_element(By.NAME, "username")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_field.send_keys("Admin")
    login_button.click()
    
    error_message = driver.find_element(By.XPATH, "//span[contains(text(),'Required')]").text
    assert "Required" in error_message
    print("TC004: Error message displayed for missing password.")

    # Test Case TC005: Login Attempt with Invalid Credentials
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_field.send_keys("InvalidUser")
    password_field.send_keys("InvalidPass")
    login_button.click()
    
    error_message = driver.find_element(By.XPATH, "//span[contains(text(),'Invalid')]").text
    assert "Invalid username or password" in error_message
    print("TC005: Error message displayed for invalid credentials.")

    # Test Case TC006: Password Field Masking
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    
    assert password_field.get_attribute("type") == "password"
    print("TC006: Password field is masked.")

    # Test Case TC007: Secure Transmission (HTTPS) Verification
    assert "https://" in driver.current_url
    print("TC007: Secure HTTPS connection verified.")

    # Test Case TC012: Account Lockout After Multiple Unsuccessful Login Attempts
    for attempt in range(5):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        username_field.send_keys("InvalidUser")
        password_field.send_keys("InvalidPass")
        login_button.click()
        time.sleep(1)
    
    lockout_message = driver.find_element(By.XPATH, "//span[contains(text(),'locked')]").text
    assert "locked" in lockout_message
    print("TC012: Account lockout verified after multiple failed login attempts.")

finally:
    # Close browser session
    driver.quit()
