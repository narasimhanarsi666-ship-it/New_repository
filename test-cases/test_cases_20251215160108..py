[
  {
    "TestCaseID": "TC001",
    "Title": "Access Login Page",
    "Precondition": "User is on the main screen",
    "Steps": "1. Click the 'Login' button/link on the main screen",
    "ExpectedResult": "User is redirected to the login page"
  },
  {
    "TestCaseID": "TC002",
    "Title": "Successful Login with Valid Credentials",
    "Precondition": "User is a registered user and is on the login page",
    "Steps": "1. Enter a valid email/username\n2. Enter a valid password\n3. Click the 'Login' button",
    "ExpectedResult": "User is logged in and redirected to the dashboard/home page"
  },
  {
    "TestCaseID": "TC003",
    "Title": "Login Attempt with Invalid Credentials",
    "Precondition": "User is on the login page",
    "Steps": "1. Enter an invalid email/username or incorrect password\n2. Click the 'Login' button",
    "ExpectedResult": "Error message indicating 'Invalid credentials' is displayed; user remains on the login page"
  },
  {
    "TestCaseID": "TC004",
    "Title": "Mandatory Field Validation on Login Page",
    "Precondition": "User is on the login page",
    "Steps": "1. Leave the email/username and password fields blank\n2. Click the 'Login' button",
    "ExpectedResult": "Validation messages are shown for both fields indicating they are required"
  },
  {
    "TestCaseID": "TC005",
    "Title": "Password Field Masking",
    "Precondition": "User is on the login page",
    "Steps": "1. Click on the password field\n2. Type any text into the password field",
    "ExpectedResult": "Entered text appears masked (e.g., displayed as \u2022\u2022\u2022\u2022\u2022)"
  },
  {
    "TestCaseID": "TC006",
    "Title": "Secure Connection Check for Login Page",
    "Precondition": "User has internet access and opens the login page URL",
    "Steps": "1. Open the login page URL\n2. Check the browser's address bar for a secure lock icon",
    "ExpectedResult": "The login page loads over HTTPS with a secure connection (lock icon visible)"
  },
  {
    "TestCaseID": "TC007",
    "Title": "Forgot Password Link Functionality",
    "Precondition": "User is on the login page",
    "Steps": "1. Click the 'Forgot Password' link\n2. On the reset password page, enter a registered email address\n3. Click the 'Submit' button",
    "ExpectedResult": "User receives instructions to reset the password via email"
  },
  {
    "TestCaseID": "TC008",
    "Title": "Remember Me Option Functionality",
    "Precondition": "User is on the login page",
    "Steps": "1. Enter valid email/username and password\n2. Check the 'Remember Me' checkbox\n3. Click the 'Login' button\n4. Close and reopen the browser",
    "ExpectedResult": "User remains logged in or finds the email/username pre-populated, confirming credentials are remembered"
  },
  {
    "TestCaseID": "TC009",
    "Title": "Account Lockout after Repeated Failed Login Attempts",
    "Precondition": "User is on the login page",
    "Steps": "1. Attempt to log in with incorrect credentials repeatedly (e.g., 5 consecutive failed attempts)\n2. Wait for or trigger the account lockout mechanism\n3. Attempt to log in with valid credentials after lockout",
    "ExpectedResult": "User account is locked, and even with the correct credentials, login is denied with an appropriate account lockout message"
  }
]