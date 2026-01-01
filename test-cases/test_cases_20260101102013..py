[
  {
    "TestCaseID": "TC001",
    "Title": "OTP Request with Valid Email",
    "Precondition": "User is on the OTP request page and has a registered email address in the system.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a valid registered email address in the input field.\n3. Select email as the communication channel.\n4. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system validates the email, generates a unique 6-digit OTP, sends it to the provided email, and displays a confirmation message on the screen."
  },
  {
    "TestCaseID": "TC002",
    "Title": "OTP Request with Valid Mobile Number",
    "Precondition": "User is on the OTP request page and has a registered mobile number in the system.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a valid registered mobile number in the input field.\n3. Select SMS as the communication channel.\n4. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system validates the mobile number, generates a unique 6-digit OTP, sends it via SMS to the mobile number, and displays a confirmation message on the screen."
  },
  {
    "TestCaseID": "TC003",
    "Title": "OTP Request with Invalid Email Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter an email address with an invalid format (e.g., 'userexample.com').\n3. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system displays a descriptive error message indicating the email format is invalid and does not proceed with generating or sending an OTP."
  },
  {
    "TestCaseID": "TC004",
    "Title": "OTP Request with Invalid Mobile Number Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a mobile number with an invalid format (e.g., too short or containing letters).\n3. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system displays a descriptive error message indicating the mobile number format is invalid and stops the OTP generation process."
  },
  {
    "TestCaseID": "TC005",
    "Title": "OTP Request for Non-Registered Contact Information",
    "Precondition": "User is on the OTP request page with contact details that are not registered in the system.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a well-formatted email or mobile number that is not linked to any existing user.\n3. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system identifies that the contact information is not associated with any user and displays an appropriate error message, preventing OTP generation."
  },
  {
    "TestCaseID": "TC006",
    "Title": "OTP Expiration Validation",
    "Precondition": "User successfully requests an OTP using valid contact information.",
    "Steps": "1. Request an OTP using valid contact information (email or mobile).\n2. Wait for the OTP to expire (simulate waiting period, e.g., 5 minutes).\n3. Attempt to use the expired OTP for verification.",
    "ExpectedResult": "The system rejects the OTP as expired and displays an error message indicating the OTP is no longer valid."
  },
  {
    "TestCaseID": "TC007",
    "Title": "OTP Request Exceeding Retry/Throttling Limit",
    "Precondition": "User is on the OTP request page and has reached the maximum number of OTP requests allowed within the specified timeframe.",
    "Steps": "1. Repeatedly request OTPs using valid contact information until the maximum allowed requests are made.\n2. Attempt to request an additional OTP once the limit has been reached.",
    "ExpectedResult": "The system prevents the additional OTP request and displays an error message indicating that the retry limit has been exceeded and throttling is in effect."
  },
  {
    "TestCaseID": "TC008",
    "Title": "Error Handling for Backend Failure in OTP Delivery (SMS/Email)",
    "Precondition": "Simulate a scenario where the SMS or email service fails (backend service error).",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter valid contact details (email or mobile).\n3. Simulate backend failure by causing the SMS/email service to be unavailable.\n4. Click on the 'Request OTP' button.",
    "ExpectedResult": "The system detects the backend failure, does not generate an OTP, and displays a graceful, descriptive error message to the user regarding the delivery issue."
  }
]