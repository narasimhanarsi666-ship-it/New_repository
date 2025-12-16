{
  "TestCases": [
    {
      "TestCaseID": "TC001",
      "Title": "Successful Registration with Valid Inputs",
      "Precondition": "User is on the registration page and no account exists for the provided email.",
      "Steps": "1. Navigate to the registration page.\n2. Enter a valid email address.\n3. Enter a valid password meeting the strength requirements.\n4. Fill in all other mandatory fields (e.g., first name, last name).\n5. Click the 'Register' button.",
      "ExpectedResult": "Account is successfully created, a confirmation email is sent, and the user is redirected to the welcome dashboard."
    },
    {
      "TestCaseID": "TC002",
      "Title": "Registration Attempt with Existing Email",
      "Precondition": "An account already exists with the email address that will be used in the test.",
      "Steps": "1. Navigate to the registration page.\n2. Enter the already registered email address.\n3. Enter a valid password and fill in other mandatory fields.\n4. Click the 'Register' button.",
      "ExpectedResult": "An error message stating 'Email already in use' is displayed and the registration process is halted."
    },
    {
      "TestCaseID": "TC003",
      "Title": "Registration Attempt with Invalid Email Format",
      "Precondition": "User is on the registration page.",
      "Steps": "1. Navigate to the registration page.\n2. Enter an invalid email address (e.g., 'userexample.com' missing the '@' symbol).\n3. Fill in the valid password and other mandatory fields.\n4. Click the 'Register' button.",
      "ExpectedResult": "An error message indicating 'Invalid email format' is displayed, and the user is prompted to correct the email field."
    },
    {
      "TestCaseID": "TC004",
      "Title": "Registration Attempt with Missing Password",
      "Precondition": "User is on the registration page.",
      "Steps": "1. Navigate to the registration page.\n2. Enter a valid email address.\n3. Leave the password field empty.\n4. Fill in other mandatory fields.\n5. Click the 'Register' button.",
      "ExpectedResult": "An error message stating 'Password is required' is displayed, preventing the registration from proceeding."
    },
    {
      "TestCaseID": "TC005",
      "Title": "Boundary Test for Password Length Requirement",
      "Precondition": "User is on the registration page; assume the minimum password length requirement is 8 characters.",
      "Steps": "1. Navigate to the registration page.\n2. Enter a valid email address.\n3. Enter a password with exactly 8 characters.\n4. Fill in the remaining mandatory fields.\n5. Click the 'Register' button.",
      "ExpectedResult": "Registration is successful, with the system accepting the password that meets the minimum length requirement."
    }
  ]
}