## Test Case 1: Successful OTP Request using Valid Phone Number
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to OTP request page
    driver.get("https://example.com/otp-request")

    # Enter a valid, registered mobile number
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys("1234567890")

    # Click the 'Request OTP' button
    request_otp_button = driver.find_element(By.ID, "request-otp")
    request_otp_button.click()

    # Validate expected outcome
    confirmation_message = driver.find_element(By.ID, "confirmation-message")
    assert "OTP has been sent to your mobile number" in confirmation_message.text

finally:
    # Close browser session
    driver.quit()
```

## Test Case 2: Successful OTP Request using Valid Email Address
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to OTP request page
    driver.get("https://example.com/otp-request")

    # Enter a valid, registered email address
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("user@example.com")

    # Click the 'Request OTP' button
    request_otp_button = driver.find_element(By.ID, "request-otp")
    request_otp_button.click()

    # Validate expected outcome
    confirmation_message = driver.find_element(By.ID, "confirmation-message")
    assert "OTP has been sent to your email address" in confirmation_message.text

finally:
    # Close browser session
    driver.quit()
```

## Test Case 3: OTP Request with Invalid Mobile Number Format
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to OTP request page
    driver.get("https://example.com/otp-request")

    # Enter an invalid mobile number format
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys("invalid_number")

    # Click the 'Request OTP' button
    request_otp_button = driver.find_element(By.ID, "request-otp")
    request_otp_button.click()

    # Validate expected outcome
    error_message = driver.find_element(By.ID, "error-message")
    assert "Invalid mobile number format" in error_message.text

finally:
    # Close browser session
    driver.quit()
```

## Test Case 4: OTP Request with Invalid Email Format
```python
from selenium import webdriver
from selenium.webdriver.common.by