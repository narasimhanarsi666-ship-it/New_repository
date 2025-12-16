{
  "TestCases": [
    {
      "TestCaseID": "TC001",
      "Title": "Request OTP using valid mobile number",
      "Precondition": "User is registered and is on the OTP request page with a valid mobile number input field.",
      "Steps": "1. Navigate to the OTP request screen.\n2. Enter a valid, registered mobile number.\n3. Submit the OTP request.",
      "ExpectedResult": "A unique 6-digit OTP is generated and sent via SMS to the entered mobile number. A confirmation message is displayed on screen."
    },
    {
      "TestCaseID": "TC002",
      "Title": "Request OTP using valid email address",
      "Precondition": "User is registered and is on the OTP request page with a valid email input field.",
      "Steps": "1. Navigate to the OTP request screen.\n2. Enter a valid, registered email address.\n3. Submit the OTP request.",
      "ExpectedResult": "A unique 6-digit OTP is generated and sent via email to the entered email address. A confirmation message is displayed on screen."
    },
    {
      "TestCaseID": "TC003",
      "Title": "Request OTP with unregistered mobile number/email",
      "Precondition": "User attempts to request an OTP with a mobile/email that is not registered.",
      "Steps": "1. Navigate to the OTP request screen.\n2. Enter an unregistered mobile number or email address.\n3. Submit the OTP request.",
      "ExpectedResult": "System validates that the contact is unregistered and displays an error message indicating that the provided contact is not associated with any user."
    },
    {
      "TestCaseID": "TC004",
      "Title": "OTP generation uniqueness validation",
      "Precondition": "User is registered and has an active session on the OTP request page.",
      "Steps": "1. Request OTP using a valid mobile number or email address.\n2. Note the generated OTP.\n3. Request OTP again immediately with the same contact information.\n4. Compare the newly generated OTP with the previous one.",
      "ExpectedResult": "A different unique OTP is generated for each request, ensuring that the OTPs do not repeat."
    },
    {
      "TestCaseID": "TC005",
      "Title": "OTP format and length validation",
      "Precondition": "User is registered and is on the OTP request page.",
      "Steps": "1. Request OTP using a valid mobile/email.\n2. Inspect the generated OTP for format and length.",
      "ExpectedResult": "The generated OTP must be 6 digits long and numeric only, adhering to system rules."
    },
    {
      "TestCaseID": "TC006",
      "Title": "OTP expiration after predefined period",
      "Precondition": "User has received a valid OTP that is time-bound (e.g., 5 minutes).",
      "Steps": "1. Request OTP using valid credentials.\n2. Wait for the OTP expiration duration to pass (simulate 5 minutes).\n3. Attempt to use the expired OTP for verification.",
      "ExpectedResult": "The system rejects the OTP and displays an error message stating that the OTP has expired."
    },
    {
      "TestCaseID": "TC007",
      "Title": "Exceeding OTP retry limit within defined timeframe",
      "Precondition": "User is registered and has requested OTP several times already.",
      "Steps": "1. Request OTP using valid mobile/email repeatedly, exceeding the allowed number of requests (as per system-defined throttle limits).\n2. Observe system behaviour after the limit is reached.",
      "ExpectedResult": "System displays an error message indicating the retry limit is exceeded and prevents further OTP requests until the timeframe resets."
    },
    {
      "TestCaseID": "TC008",
      "Title": "Invalid mobile number/email format error handling",
      "Precondition": "User is on the OTP request page.",
      "Steps": "1. Enter an improperly formatted mobile number (e.g., missing digits) or email (e.g., no @ symbol).\n2. Submit the OTP request.",
      "ExpectedResult": "System immediately validates the format and displays an error message specifying that the format is invalid without making an OTP generation attempt."
    },
    {
      "TestCaseID": "TC009",
      "Title": "Backend failure handling during SMS/email delivery",
      "Precondition": "Simulate backend failure (e.g., SMS/email service outage) while processing OTP request.",
      "Steps": "1. Request OTP using a valid mobile/email under simulated backend failure conditions.\n2. Monitor the system response.",
      "ExpectedResult": "System handles the failure gracefully by displaying a descriptive error message to the user, and no OTP is accepted or generated."
    },
    {
      "TestCaseID": "TC010",
      "Title": "Boundary condition: OTP request at the exact time of expiration",
      "Precondition": "User receives a valid OTP that is about to expire (simulate nearing the 5-minute limit).",
      "Steps": "1. Request OTP using valid credentials.\n2. Wait until just before the OTP expiration time (simulate e.g. 4 minutes and 55 seconds).\n3. Attempt to use the OTP immediately.",
      "ExpectedResult": "The OTP should remain valid if used just before the expiration time; if used after, it should be rejected."
    }
  ]
}