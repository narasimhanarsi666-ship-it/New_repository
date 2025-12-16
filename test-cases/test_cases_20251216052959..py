{
  "TestCases": [
    {
      "TestCaseID": "TC001",
      "Title": "Fetch description for a valid Jira issue",
      "Precondition": "User has valid credentials and a valid Jira issue ID is provided.",
      "Steps": "1. Provide a valid Jira issue ID (e.g., 'JIRA-1234') as input.\n2. Invoke the Jira Issue Description Fetcher tool.\n3. Wait for the response.",
      "ExpectedResult": "The tool returns the full description of the issue, including any relevant details as stored in Jira."
    },
    {
      "TestCaseID": "TC002",
      "Title": "Handling non-existing Jira issue",
      "Precondition": "User has valid credentials, but the provided Jira issue ID does not exist.",
      "Steps": "1. Provide a non-existing Jira issue ID (e.g., 'JIRA-9999') as input.\n2. Invoke the Jira Issue Description Fetcher tool.\n3. Monitor error handling process.",
      "ExpectedResult": "The tool returns an error message indicating that the issue could not be found, without crashing the application."
    },
    {
      "TestCaseID": "TC003",
      "Title": "Handling empty Jira issue ID input",
      "Precondition": "User has valid credentials.",
      "Steps": "1. Leave the Jira issue ID field blank.\n2. Trigger the tool to fetch the issue description.\n3. Monitor the response.",
      "ExpectedResult": "The tool validates the input and returns an appropriate error message stating that the issue ID is required."
    },
    {
      "TestCaseID": "TC004",
      "Title": "Network error during Jira description fetch",
      "Precondition": "User is on a system with valid credentials but there is a deliberate network interruption or fault.",
      "Steps": "1. Provide a valid Jira issue ID as input.\n2. Simulate a network failure (e.g., disconnect the network) before invoking the tool.\n3. Invoke the Jira Issue Description Fetcher tool immediately after simulating the failure.",
      "ExpectedResult": "The tool detects the network issue and returns a meaningful error message indicating a connection problem, without crashing."
    },
    {
      "TestCaseID": "TC005",
      "Title": "Authentication failure during Jira description fetch",
      "Precondition": "User credentials are invalid or expired.",
      "Steps": "1. Provide a valid Jira issue ID with invalid or expired credentials in the context.\n2. Invoke the Jira Issue Description Fetcher tool.\n3. Monitor the interactions with the authentication module.",
      "ExpectedResult": "The tool returns an error message indicating authentication failure and does not provide any issue details."
    },
    {
      "TestCaseID": "TC006",
      "Title": "Internal module error: Handling 'AVASecret.getKey' attribute error",
      "Precondition": "The system is configured with the current version where AVASecret module is misconfigured/missing the getKey attribute.",
      "Steps": "1. Provide any valid Jira issue ID as input.\n2. Invoke the Jira Issue Description Fetcher tool.\n3. Monitor system logs and tool output for error handling related to the AVASecret attribute error.",
      "ExpectedResult": "The tool catches the error from the missing 'getKey' attribute in the AVASecret module, logs an appropriate error message, and returns a user-friendly error message indicating an internal system error without exposing sensitive information."
    }
  ]
}