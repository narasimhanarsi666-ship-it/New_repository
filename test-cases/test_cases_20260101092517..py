[
  {
    "TestCaseID": "TC001",
    "Title": "Fetch issue description with a valid issue key",
    "Precondition": "There exists a valid issue key with a corresponding description in the system.",
    "Steps": "1. Navigate to the issue search or description fetch page.\n2. Enter a valid issue key (e.g., KAN-1) in the input field.\n3. Click the 'Fetch Description' button.",
    "ExpectedResult": "The system displays the correct description for the provided valid issue key."
  },
  {
    "TestCaseID": "TC002",
    "Title": "Fetch issue description with an invalid/non-existing issue key",
    "Precondition": "The provided issue key does not exist in the system.",
    "Steps": "1. Navigate to the issue search or description fetch page.\n2. Enter an invalid/non-existing issue key (e.g., KAN-9999) in the input field.\n3. Click the 'Fetch Description' button.",
    "ExpectedResult": "The system shows the error message: 'Error: Unable to fetch the description. The issue key might not exist or there is an issue with the provided details.'"
  },
  {
    "TestCaseID": "TC003",
    "Title": "Error handling for empty issue key input",
    "Precondition": "User is on the issue description fetch page.",
    "Steps": "1. Leave the issue key input field blank.\n2. Click the 'Fetch Description' button.",
    "ExpectedResult": "The system prompts the user to enter a valid issue key or displays an appropriate error message indicating the input is required."
  },
  {
    "TestCaseID": "TC004",
    "Title": "System behavior with partial/incomplete issue key input",
    "Precondition": "User is on the issue description fetch page.",
    "Steps": "1. Enter a partially complete issue key (e.g., 'KAN-') in the input field.\n2. Click the 'Fetch Description' button.",
    "ExpectedResult": "The system displays a validation error message indicating that the issue key format is incomplete and prompting the user to complete the key."
  },
  {
    "TestCaseID": "TC005",
    "Title": "Handling service unavailability when fetching issue description",
    "Precondition": "The backend service for fetching issue descriptions is unavailable or down.",
    "Steps": "1. Attempt to fetch a description by entering any issue key (valid or invalid) on the issue fetch page.\n2. Click the 'Fetch Description' button.",
    "ExpectedResult": "The system displays a clear error message indicating that the service is currently unavailable, possibly along with suggestions to try again later."
  }
]