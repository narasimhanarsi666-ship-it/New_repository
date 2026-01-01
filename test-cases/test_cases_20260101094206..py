from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Test Case TC001: Successful OTP request using valid phone number
    driver.get("https://example.com/otp-request")  # Replace with actual URL
    phone_input = driver.find_element(By.ID, "phone")  # Replace with actual ID
    phone_input.send_keys("1234567890")  # Replace with a valid registered phone number
    request_otp_button = driver.find_element(By.ID, "requestOtp")  # Replace with actual ID
    request_otp_button.click()
    time.sleep(2)  # Wait for confirmation message
    confirmation_message = driver.find_element(By.ID, "confirmationMessage")  # Replace with actual ID
    assert "OTP sent successfully" in confirmation_message.text

    # Test Case TC002: Successful OTP request using valid email address
    driver.get("https://example.com/otp-request")  # Replace with actual URL
    email_input = driver.find_element(By.ID, "email")  # Replace with actual ID
    email_input.send_keys("user@example.com")  # Replace with a valid registered email address
    request_otp_button = driver.find_element(By.ID, "requestOtp")  # Replace with actual ID
    request_otp_button.click()
    time.sleep(2)  # Wait for confirmation message
    confirmation_message = driver.find_element(By.ID, "confirmationMessage")  # Replace with actual ID
    assert "OTP sent successfully" in confirmation_message.text

    # Test Case TC003: OTP generation adheres to format rules
    driver.get("https://example.com/otp-request")  # Replace with actual URL
    phone_input = driver.find_element(By.ID, "phone")  # Replace with actual ID
    phone_input.send_keys("1234567890")  # Replace with a valid registered phone number
    request_otp_button = driver.find_element(By.ID, "requestOtp")  # Replace with actual ID
    request_otp_button.click()
    time.sleep(2)  # Wait for OTP generation
    otp_element = driver.find_element(By.ID, "otpCode")  # Replace with actual ID
    otp_code = otp_element.text
    assert len(otp_code) == 6 and otp_code.isdigit()

    # Test Case TC004: OTP expiration verification
    driver.get("https://example.com/otp-request")  # Replace with actual URL
    phone_input = driver.find_element(By.ID, "phone")  # Replace with actual ID
    phone_input.send_keys("1234567890")  # Replace with a valid registered phone number
    request_otp_button = driver.find_element(By.ID, "requestOtp")  # Replace with actual ID
    request_otp_button.click()
    time.sleep(300)  # Simulate wait time for OTP expiration
    expired_otp_input = driver.find_element(By.ID, "otpCode")  # Replace with actual ID
    expired_otp_input.send_keys("123456")  # Replace with expired OTP
    submit_button = driver.find_element(By.ID, "submitOtp")  # Replace with actual ID
    submit_button.click()
    error_message = driver.find_element(By.ID, "errorMessage")  # Replace with actual ID
    assert "OTP has expired" in error_message.text

finally:
    # Close browser session
    driver.quit()