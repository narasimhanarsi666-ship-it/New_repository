[
  {
    "TestCaseID": "TC001",
    "Title": "Successful OTP Request with Valid Email",
    "Precondition": "User is on the OTP request page and has a registered email address.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a valid registered email address.\n3. Click the 'Request OTP' button.",
    "ExpectedResult": "OTP is generated following the predefined rules (6-digit numeric), sent to the entered email address, and a confirmation message is displayed on screen."
  },
  {
    "TestCaseID": "TC002",
    "Title": "Successful OTP Request with Valid Phone Number",
    "Precondition": "User is on the OTP request page and has a registered phone number.",
    "Steps": "1. Navigate to the OTP request page.\n2. Enter a valid registered mobile number.\n3. Click the 'Request OTP' button.",
    "ExpectedResult": "OTP is generated following the predefined rules (6-digit numeric), sent via SMS to the entered phone number, and a confirmation message is displayed on screen."
  },
  {
    "TestCaseID": "TC003",
    "Title": "OTP Generation - Unique and Correct Format",
    "Precondition": "User is on the OTP request page with valid registered contact details.",
    "Steps": "1. Request an OTP using a valid registered email or phone number.\n2. Check that the OTP generated is 6 characters long and numeric.\n3. Request another OTP and compare both OTPs for uniqueness.",
    "ExpectedResult": "Each OTP generated is unique (different from the previous OTP) and conforms to the 6-digit numeric format."
  },
  {
    "TestCaseID": "TC004",
    "Title": "OTP Delivery - Correct Channel Validation",
    "Precondition": "User with registered contact details (email or phone) is on the OTP request page.",
    "Steps": "1. Request an OTP using the registered email address.\n2. Verify that the email inbox receives the OTP.\n3. Request an OTP using the registered phone number.\n4. Verify that the SMS message contains the OTP.",
    "ExpectedResult": "OTP is sent to the correct channel (email or SMS) corresponding to the user's registered contact detail."
  },
  {
    "TestCaseID": "TC005",
    "Title": "Display of Confirmation Message after OTP Request",
    "Precondition": "User has initiated an OTP request with valid contact detail.",
    "Steps": "1. Submit a valid OTP request (via email or phone).\n2. Observe the on-screen message post request.",
    "ExpectedResult": "A confirmation message is displayed confirming that the OTP has been sent to the provided contact detail."
  },
  {
    "TestCaseID": "TC006",
    "Title": "OTP Expiration after Predefined Duration",
    "Precondition": "User has successfully received an OTP.",
    "Steps": "1. Request an OTP using a valid contact method.\n2. Wait for a duration exceeding the expiration time (e.g., 6 minutes if expiration is set to 5 minutes).\n3. Attempt to use the expired OTP for verification.",
    "ExpectedResult": "The OTP is rejected as expired, and the system displays an error or requests a new OTP."
  },
  {
    "TestCaseID": "TC007",
    "Title": "Retry and Throttling Limits for OTP Requests",
    "Precondition": "User is on the OTP request page with a registered contact detail.",
    "Steps": "1. Request an OTP repeatedly within a short time frame to exceed the allowed retry/limit threshold.\n2. Attempt another OTP request after reaching the limit.",
    "ExpectedResult": "The system prevents further OTP requests and displays an error message indicating that the retry limit has been exceeded or throttling is in effect."
  },
  {
    "TestCaseID": "TC008",
    "Title": "Error Handling for Invalid Mobile Number Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter an invalid mobile number (e.g., incorrect format, too short or contains alphabets).\n2. Click the 'Request OTP' button.",
    "ExpectedResult": "The system displays a descriptive error message indicating that the mobile number format is invalid."
  },
  {
    "TestCaseID": "TC009",
    "Title": "Error Handling for Invalid Email Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter an invalid email format (e.g., missing '@', missing domain).\n2. Click the 'Request OTP' button.",
    "ExpectedResult": "The system displays a descriptive error message indicating that the email format is invalid."
  },
  {
    "TestCaseID": "TC010",
    "Title": "Graceful Handling of Backend Failures (SMS/Email service issues)",
    "Precondition": "Simulate a backend failure (e.g., disable SMS or Email service) while on the OTP request page.",
    "Steps": "1. Request an OTP using a valid registered mobile number or email address while the backend service is down.\n2. Check the on-screen response.",
    "ExpectedResult": "The system handles the backend failure gracefully by showing a descriptive error message to the user and suggesting a retry or alternative action."
  }
]