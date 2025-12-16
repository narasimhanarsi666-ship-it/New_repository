[
  {
    "TestCaseID": "TC001",
    "Title": "Valid OTP Request using Registered Mobile Number",
    "Precondition": "User is on the OTP request page; mobile number is registered.",
    "Steps": "1. Enter a valid, registered mobile number.\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "A unique 6-digit numeric OTP is generated and sent via SMS; a confirmation message is displayed."
  },
  {
    "TestCaseID": "TC002",
    "Title": "Valid OTP Request using Registered Email Address",
    "Precondition": "User is on the OTP request page; email is registered.",
    "Steps": "1. Enter a valid, registered email address.\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "A unique 6-digit numeric OTP is generated and sent to the email; a confirmation message is displayed."
  },
  {
    "TestCaseID": "TC003",
    "Title": "OTP Request with Unregistered Mobile Number",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter an unregistered mobile number.\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "Error message indicates that the mobile number is not associated with an existing account."
  },
  {
    "TestCaseID": "TC004",
    "Title": "OTP Request with Unregistered Email Address",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter an unregistered email address.\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "Error message indicates that the email address is not associated with an existing account."
  },
  {
    "TestCaseID": "TC005",
    "Title": "Invalid Input: Malformed Mobile Number Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter a mobile number with an incorrect format (e.g., missing digits or including letters).\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "Error message indicating invalid mobile number format is displayed."
  },
  {
    "TestCaseID": "TC006",
    "Title": "Invalid Input: Malformed Email Address Format",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Enter an email address with an incorrect format (e.g., missing '@' symbol or domain).\n2. Click on the 'Request OTP' button.",
    "ExpectedResult": "Error message indicating invalid email address format is displayed."
  },
  {
    "TestCaseID": "TC007",
    "Title": "OTP Generation Uniqueness",
    "Precondition": "User is on the OTP request page and is using a registered contact.",
    "Steps": "1. Request an OTP and note the generated OTP.\n2. After a short interval, request another OTP using the same contact information.",
    "ExpectedResult": "Two uniquely generated 6-digit numeric OTPs are produced; the OTPs should not be identical even if requested within the expiration period."
  },
  {
    "TestCaseID": "TC008",
    "Title": "OTP Expiration Verification",
    "Precondition": "User has received an OTP that is valid for 5 minutes.",
    "Steps": "1. Use the OTP within 5 minutes to perform an authentication or verification action (simulate successful use).\n2. Wait for 5 minutes and then attempt to use the same OTP.",
    "ExpectedResult": "OTP is accepted and processed when used within 5 minutes; after 5 minutes, the OTP is rejected as expired."
  },
  {
    "TestCaseID": "TC009",
    "Title": "Expired OTP Non-Reusability",
    "Precondition": "User has an OTP that has expired.",
    "Steps": "1. Attempt to reuse the expired OTP for authentication or any verification attempt.",
    "ExpectedResult": "System rejects the OTP, displaying an error that the OTP has expired and cannot be reused."
  },
  {
    "TestCaseID": "TC010",
    "Title": "Enforcement of OTP Request Retry Limits",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Request OTP repeatedly (simulate reaching the maximum allowed number, e.g., 3 attempts) in a short period.\n2. Attempt one more OTP request beyond the allowed limit.",
    "ExpectedResult": "System prevents further OTP requests and displays an error message indicating that the retry limit has been exceeded."
  },
  {
    "TestCaseID": "TC011",
    "Title": "Handling Backend Failure for SMS Delivery",
    "Precondition": "User is on the OTP request page with a valid registered mobile number; simulate SMS gateway failure.",
    "Steps": "1. Enter a valid, registered mobile number.\n2. Click on the 'Request OTP' button with SMS backend service simulated to fail.",
    "ExpectedResult": "System displays a descriptive error message about the failure in OTP delivery due to backend issues without crashing."
  },
  {
    "TestCaseID": "TC012",
    "Title": "Handling Backend Failure for Email Delivery",
    "Precondition": "User is on the OTP request page with a valid registered email; simulate email service failure.",
    "Steps": "1. Enter a valid, registered email address.\n2. Click on the 'Request OTP' button with email backend service simulated to fail.",
    "ExpectedResult": "System displays a descriptive error message about the failure in OTP delivery due to backend issues without crashing."
  },
  {
    "TestCaseID": "TC013",
    "Title": "Throttle OTP Requests to Prevent Abuse",
    "Precondition": "User is on the OTP request page.",
    "Steps": "1. Rapidly request OTPs several times within a few seconds to trigger throttling mechanisms.",
    "ExpectedResult": "System temporarily blocks additional OTP requests and displays an error message indicating that too many requests have been made, enforcing throttling."
  }
]