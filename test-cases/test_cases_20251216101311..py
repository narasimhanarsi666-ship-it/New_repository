# Initialize the WebDriver
driver = webdriver.Chrome()

# Test Case 1: Valid OTP Request
def test_valid_otp_request():
    try:
        driver.get("https://example.com/login")  # Replace with the actual URL
        time.sleep(2)

        # Enter valid phone number or email
        contact_field = driver.find_element(By.ID, "contact-input")  # Replace with actual element ID
        contact_field.send_keys("valid@example.com")  # Replace with valid contact info
        contact_field.send_keys(Keys.RETURN)

        # Wait for confirmation message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "confirmation-message"), "OTP sent successfully")
        )
        print("Test Case 1 Passed: Valid OTP request successful.")
    except Exception as e:
        print(f"Test Case 1 Failed: {e}")

# Test Case 2: Invalid Contact Format
def test_invalid_contact_format():
    try:
        driver.get("https://example.com/login")  # Replace with the actual URL
        time.sleep(2)

        # Enter invalid phone number or email
        contact_field = driver.find_element(By.ID, "contact-input")  # Replace with actual element ID
        contact_field.send_keys("invalid_contact")  # Replace with invalid contact info
        contact_field.send_keys(Keys.RETURN)

        # Wait for error message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "error-message"), "Invalid contact format")
        )
        print("Test Case 2 Passed: Invalid contact format handled correctly.")
    except Exception as e:
        print(f"Test Case 2 Failed: {e}")

# Test Case 3: Expired OTP
def test_expired_otp():
    try:
        driver.get("https://example.com/login")  # Replace with the actual URL
        time.sleep(2)

        # Simulate OTP expiration
        otp_field = driver.find_element(By.ID, "otp-input")  # Replace with actual element ID
        otp_field.send_keys("123456")  # Replace with expired OTP
        otp_field.send_keys(Keys.RETURN)

        # Wait for expiration message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "error-message"), "OTP expired")
        )
        print("Test Case 3 Passed: Expired OTP handled correctly.")
    except Exception as e:
        print(f"Test Case 3 Failed: {e}")

# Test Case 4: Retry Limit Exceeded
def test_retry_limit_exceeded():
    try:
        driver.get("https://example.com/login")  # Replace with the actual URL
        time.sleep(2)

        # Simulate retry limit exceeded
        contact_field = driver.find_element(By.ID, "contact-input")  # Replace with actual element ID
        contact_field.send_keys("valid@example.com")  # Replace with valid contact info
        for _ in range(5):  # Simulate multiple requests
            contact_field.send_keys(Keys.RETURN)
            time.sleep(1)

        # Wait for retry limit message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "error-message"), "Retry limit exceeded")
        )
        print("Test Case 4 Passed: Retry limit exceeded handled correctly.")
    except Exception as e:
        print(f"Test Case 4 Failed: {e}")

# Test Case 5: Backend Failure
def test_backend_failure():
    try:
        driver.get("https://example.com/login")  # Replace with the actual URL
        time.sleep(2)

        # Simulate backend failure
        contact_field = driver.find_element(By.ID, "contact-input")  # Replace with actual element ID
        contact_field.send_keys("valid@example.com")  # Replace with valid contact info
        contact_field.send_keys(Keys.RETURN)

        # Wait for backend failure message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "error-message"), "Service unavailable")
        )
        print("Test Case 5 Passed: Backend failure handled correctly.")
    except Exception as e:
        print(f"Test Case 5 Failed: {e}")

# Run all test cases
test_valid_otp_request()
test_invalid_contact_format()
test_expired_otp()
test_retry_limit_exceeded()
test_backend_failure()

# Close the WebDriver
driver.quit()
