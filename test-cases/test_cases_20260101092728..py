[
  {
    "TestCaseID": "TC001",
    "Title": "Error Displayed for Non-Existent Issue Key",
    "Precondition": "The user is on the issue lookup page of the Jira instance.",
    "Steps": "1. Enter a non-existent issue key (e.g., 'KAN-2') into the search field.\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "The system displays the error: 'Error: The issue with the key 'KAN-2' could not be found. Please verify the issue key and ensure it exists in the specified Jira instance.'"
  },
  {
    "TestCaseID": "TC002",
    "Title": "No Error for Valid Issue Key",
    "Precondition": "The user is on the issue lookup page and a valid issue key exists in the system.",
    "Steps": "1. Enter a valid issue key that exists in Jira into the search field.\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "The system successfully retrieves and displays the details of the issue without showing any error message."
  },
  {
    "TestCaseID": "TC003",
    "Title": "Error When Issue Key Field is Empty",
    "Precondition": "The user is on the issue lookup page.",
    "Steps": "1. Leave the issue key input field empty.\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "An appropriate validation message is displayed indicating that the issue key field cannot be empty. Alternatively, if the system proceeds, it should display an error that no valid issue key was provided."
  },
  {
    "TestCaseID": "TC004",
    "Title": "Error Displayed for Improperly Formatted Issue Key",
    "Precondition": "The user is on the issue lookup page.",
    "Steps": "1. Enter an improperly formatted issue key (e.g., 'KAN2' without the hyphen or 'kan-2' using the wrong letter case).\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "The system displays a clear fault message indicating that the issue key format is incorrect, or defaults to a not found error message as per system design."
  },
  {
    "TestCaseID": "TC005",
    "Title": "Error Handling for Excessively Long Issue Key",
    "Precondition": "The user is on the issue lookup page.",
    "Steps": "1. Enter an excessively long string as the issue key (e.g., 'KAN-12345678901234567890').\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "The system either validates the issue key length with an appropriate error message or displays the standard error indicating that the issue could not be found."
  },
  {
    "TestCaseID": "TC006",
    "Title": "Error Displayed for Issue Key with Special Characters",
    "Precondition": "The user is on the issue lookup page.",
    "Steps": "1. Enter an issue key containing special characters (e.g., 'KAN-@#').\n2. Click the 'Search' or 'Lookup' button.",
    "ExpectedResult": "The system displays an error message indicating that the issue key is invalid due to the presence of special characters, or displays the standard not found error if it does not match any valid issue."
  }
]