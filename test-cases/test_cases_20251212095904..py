from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the Jira user story fetch page
    driver.get("https://jira-fetch-page.example.com")

    # Step 1: Enter a valid issue key in the input field
    issue_key_input = driver.find_element(By.ID, "issueKeyInput")
    issue_key_input.send_keys("VALID-1234")

    # Step 2: Click the 'Fetch Story' button
    fetch_button = driver.find_element(By.ID, "fetchStoryButton")
    fetch_button.click()

    # Step 3: Wait for the system to retrieve the user story details
    time.sleep(5)  # Adjust the wait time as necessary

    # Validate the expected outcome
    story_details = driver.find_element(By.ID, "storyDetails")
    assert "VALID-1234" in story_details.text, "User story details not displayed as expected."

finally:
    # Close browser session
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the Jira user story fetch page
    driver.get("https://jira-fetch-page.example.com")

    # Step 1: Enter an invalid or non-existent issue key in the input field
    issue_key_input = driver.find_element(By.ID, "issueKeyInput")
    issue_key_input.send_keys("INVALID-0000")

    # Step 2: Click the 'Fetch Story' button
    fetch_button = driver.find_element(By.ID, "fetchStoryButton")
    fetch_button.click()

    # Validate the expected outcome
    time.sleep(5)  # Adjust the wait time as necessary
    error_message = driver.find_element(By.ID, "errorMessage")
    assert "An unexpected error occurred while fetching the Jira user story. Please verify the issue key and try again." in error_message.text, "Error message not displayed as expected."

finally:
    # Close browser session
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the Jira user story fetch page
    driver.get("https://jira-fetch-page.example.com")

    # Step 1: Simulate network disconnection (this step may require additional tools or configurations)
    print("Simulate network disconnection here.")

    # Step 2: Enter a valid issue key in the input field
    issue_key_input = driver.find_element(By.ID, "issueKeyInput")
    issue_key_input.send_keys("VALID-1234")

    # Step 3: Click the 'Fetch Story' button
    fetch_button = driver.find_element(By.ID, "fetchStoryButton")
    fetch_button.click()

    # Validate the expected outcome
    time.sleep(5)  # Adjust the wait time as necessary
    error_message = driver.find_element(By.ID, "errorMessage")
    assert "network issue" in error_message.text.lower(), "Network error message not displayed as expected."

finally:
    # Close browser session
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the Jira user story fetch page
    driver.get("https://jira-fetch-page.example.com")

    # Step 1: Simulate an error by entering an invalid issue key
    issue_key_input = driver.find_element(By.ID, "issueKeyInput")
    issue_key_input.send_keys("INVALID-0000")
    fetch_button = driver.find_element(By.ID, "fetchStoryButton")
    fetch_button.click()

    # Validate the error message
    time.sleep(5)  # Adjust the wait time as necessary
    error_message = driver.find_element(By.ID, "errorMessage")
    assert "An unexpected error occurred while fetching the Jira user story." in error_message.text, "Error message not displayed as expected."

    # Step 2: Retry with a valid issue key
    retry_button = driver.find_element(By.ID, "retryButton")
    retry_button.click()

    # Step 3: Enter a valid issue key and click 'Fetch Story' again
    issue_key_input.clear()
    issue_key_input.send_keys("VALID-1234")
    fetch_button.click()

    # Validate the expected outcome
    time.sleep(5)  # Adjust the wait time as necessary
    story_details = driver.find_element(By.ID, "storyDetails")
    assert "VALID-1234" in story_details.text, "User story details not displayed as expected after retry."

finally:
    # Close browser session
    driver.quit()