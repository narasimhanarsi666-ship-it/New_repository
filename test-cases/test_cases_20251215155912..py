[
  {
    "TestCaseID": "TC001",
    "Title": "Access Login Page",
    "Precondition": "User is on the main screen of the application.",
    "Steps": "1. Click on the 'Login' button or link on the main screen.",
    "ExpectedResult": "The login page is displayed with fields for email/username and password. The page is loaded over HTTPS."
  },
  {
    "TestCaseID": "TC002",
    "Title": "Input Validation for Empty Fields",
    "Precondition": "User is on the login page.",
    "Steps": "1. Leave the email/username field empty.\n2. Leave the password field empty.\n3. Click on the 'Login' button.",
    "ExpectedResult": "Validation errors are displayed indicating that both email/username and password fields are required."
  },
  {
    "TestCaseID": "TC003",
    "Title": "Successful Login with Valid Credentials",
    "Precondition": "User has a valid registered account and is on the login page.",
    "Steps": "1. Enter a valid email/username in the email field.\n2. Enter the correct password in the password field.\n3. Click on the 'Login' button.",
    "ExpectedResult": "User is authenticated, redirected to the dashboard/home page, and session is initiated securely."
  },
  {
    "TestCaseID": "TC004",
    "Title": "Login Attempt with Invalid Credentials",
    "Precondition": "User is on the login page.",
    "Steps": "1. Enter an invalid or unregistered email/username.\n2. Enter an incorrect password.\n3. Click on the 'Login' button.",
    "ExpectedResult": "An error message is displayed stating that the credentials are incorrect. The user is not logged in."
  },
  {
    "TestCaseID": "TC005",
    "Title": "Required Field Validation - Email/Username",
    "Precondition": "User is on the login page.",
    "Steps": "1. Leave the email/username field empty.\n2. Enter a valid password in the password field.\n3. Click on the 'Login' button.",
    "ExpectedResult": "A validation error message is displayed indicating that the email/username field cannot be empty."
  },
  {
    "TestCaseID": "TC006",
    "Title": "Required Field Validation - Password",
    "Precondition": "User is on the login page.",
    "Steps": "1. Enter a valid email/username in the email field.\n2. Leave the password field empty.\n3. Click on the 'Login' button.",
    "ExpectedResult": "A validation error message is displayed indicating that the password field cannot be empty."
  },
  {
    "TestCaseID": "TC007",
    "Title": "Password Field Masking",
    "Precondition": "User is on the login page.",
    "Steps": "1. Enter any value in the password field.",
    "ExpectedResult": "The password characters are masked (e.g., appear as asterisks or dots)."
  },
  {
    "TestCaseID": "TC008",
    "Title": "Forgot Password Link Functionality",
    "Precondition": "User is on the login page.",
    "Steps": "1. Verify that the 'Forgot Password' link is visible on the login page.\n2. Click on the 'Forgot Password' link.",
    "ExpectedResult": "User is redirected to the 'Forgot Password' page where they can initiate the password reset process."
  },
  {
    "TestCaseID": "TC009",
    "Title": "Remember Me Option Functionality",
    "Precondition": "User is on the login page and has a valid account.",
    "Steps": "1. Enter valid email/username and password.\n2. Select the 'Remember Me' checkbox.\n3. Click on the 'Login' button.\n4. Log out and then reopen the application.",
    "ExpectedResult": "User remains logged in or the login fields are pre-populated, depending on the defined behavior for the 'Remember Me' option."
  },
  {
    "TestCaseID": "TC010",
    "Title": "Account Lockout after Repeated Failed Attempts",
    "Precondition": "User is on the login page with an existing account that is not locked.",
    "Steps": "1. Enter an invalid password multiple times (e.g., 5 consecutive failed login attempts) using a valid email/username.\n2. Attempt to log in after the threshold is reached.",
    "ExpectedResult": "The account is locked temporarily, and a message is displayed indicating that the account is locked due to multiple unsuccessful attempts."
  },
  {
    "TestCaseID": "TC011",
    "Title": "Input Validation for Invalid Email Format",
    "Precondition": "User is on the login page.",
    "Steps": "1. Enter an incorrectly formatted email address (e.g., missing '@' or domain) in the email field.\n2. Enter a valid password.\n3. Click on the 'Login' button.",
    "ExpectedResult": "A validation error message is displayed indicating that the email format is invalid. The login should not proceed."
  }
]