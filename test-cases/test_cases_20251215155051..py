import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WebDriver setup
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')

# Specify the path to the ChromeDriver executable
webdriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

# Test case: Accessing the login page
url = 'https://example.com/login'
driver.get(url)
time.sleep(2)

# Test case: Validating input fields
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
assert username_field.is_displayed(), 'Username field is not displayed'
assert password_field.is_displayed(), 'Password field is not displayed'

# Test case: Successful login
username_field.send_keys('test_user')
password_field.send_keys('secure_password')
login_button = driver.find_element(By.ID, 'loginButton')
login_button.click()
time.sleep(2)
assert 'Dashboard' in driver.title, 'Login failed or Dashboard not loaded'

# Test case: Error handling
username_field.clear()
password_field.clear()
username_field.send_keys('wrong_user')
password_field.send_keys('wrong_password')
login_button.click()
time.sleep(2)
error_message = driver.find_element(By.ID, 'errorMessage')
assert error_message.is_displayed(), 'Error message not displayed for invalid credentials'

# Test case: Security checks
cookies = driver.get_cookies()
assert len(cookies) > 0, 'No cookies found after login'

# Close the browser
driver.quit()