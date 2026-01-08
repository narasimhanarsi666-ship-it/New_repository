### Script 1: Access Login Page (access_login_page.py)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def access_login_page():
    driver = webdriver.Chrome(service=ChromeService())
    driver.maximize_window()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "divLoginPanel")))
        print("Access Login Page Test: PASS")
    except Exception as e:
        print(f"Access Login Page Test: FAIL - {e}")
    finally:
        driver.quit()

access_login_page()
```

### Script 2: Successful Login with Valid Credentials (valid_login.py)
```python
from selenium import webdriver
from selenium.webdriver.common.by