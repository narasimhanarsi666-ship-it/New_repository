### Test Cases and Scripts

#### Test Cases

1. **TestCaseID:** TC001
   **Title:** Access Login Page from Main Screen
   **Precondition:** User has internet connection and access to the application URL.
   **Steps:**
      1. Open a web browser.
      2. Navigate to the URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
      3. Observe the login page elements.
   **ExpectedResult:** Login page is loaded successfully with visible fields for username/email and password, along with 'Forgot Password' and 'Remember Me' options.

2. **TestCaseID:** TC002
   **Title:** Successful Login with Valid Credentials
   **Precondition:** User is on the login page and the credentials (Username: Admin, Password: admin123) are valid.
   **Steps:**
      1. Enter 'Admin' in the username/email field.
      2. Enter 'admin123' in the password field.
      3. Click on the 'Login' button.
   **ExpectedResult:** User is authenticated and redirected to the dashboard/home page displaying personalized information.

3. **TestCaseID:** TC003
   **Title:** Login Attempt with Blank Username
   **Precondition:** User is on the login page.
   **Steps:**
      1. Leave the username/email field blank.
      2. Enter 'admin123' in the password field.
      3. Click on the 'Login' button.
   **ExpectedResult:** Login fails with an error message indicating that the username/email field is required.

4. **TestCaseID:** TC004
   **Title:** Login Attempt with Blank Password
   **Precondition:** User is on the login page.
   **Steps:**
      1. Enter 'Admin' in the username/email field.
      2. Leave the password field blank.
      3. Click on the 'Login' button.
   **ExpectedResult:** Login fails with an error message indicating that the password field is required.

5. **TestCaseID:** TC005
   **Title:** Login Attempt with Incorrect Credentials
   **Precondition:** User is on the login page with an account available.
   **Steps:**
      1. Enter an incorrect username/email (e.g., 'Admin1').
      2. Enter an incorrect password (e.g., 'wrongpass').
      3. Click on the 'Login' button.
   **ExpectedResult:** Login fails with a clear error message emphasizing that the login attempt was unsuccessful due to incorrect credentials.

#### Python Selenium Scripts

```python
# Python Selenium Script for Test Case TC001: Access Login Page from Main Screen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open a web browser and navigate to the URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Step 2: Verify the login page elements
    assert "OrangeHRM" in driver.title, "Login page title does not match."
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
    remember_me_checkbox = driver.find_element(By.NAME, "remember")
    
    # Step 3: Validate the presence of required elements
    assert username_field.is_displayed(), "Username field is not visible."
    assert password_field.is_displayed(), "Password field is not visible."
    assert forgot_password_link.is_displayed(), "Forgot Password link is not visible."
    assert remember_me_checkbox.is_displayed(), "Remember Me checkbox is not visible."

    print("Test Case TC001 Passed: Login page loaded successfully with all required elements.")
    
finally:
    # Close the browser session
    driver.quit()
```

```python
# Python Selenium Script for Test Case TC002: Successful Login with Valid Credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Step 2: Enter valid credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    login_button.click()
    
    # Step 3: Validate successful login
    time.sleep(3)  # Wait for redirection
    assert "dashboard" in driver.current_url, "User is not redirected to the dashboard after login."
    print("Test Case TC002 Passed: User logged in successfully and redirected to the dashboard.")
    
finally:
    # Close the browser session
    driver.quit()
```

... (Other scripts follow the same format for TC003, TC004, TC005, etc.)