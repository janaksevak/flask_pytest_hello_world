import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import tempfile

# BROWSER_URL = "http://127.0.0.1:5000" #Local Testing
BROWSER_URL = "http://localhost:5000" #CI/CD Environment Testing

@pytest.fixture
def browser():
    user_data_dir = tempfile.mkdtemp()

    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")   # Prevent shared memory crashes
    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

    # Start Chrome with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver  # This gives the test access to the browser (driver)
    
    # After the test, quit the driver (close the browser)
    driver.quit()

# Creating multiple separate test cases
def test_page_text_change(browser):
    # Make sure Flask app is running at this URL
    browser.get(BROWSER_URL) 

    # Add a wait to ensure the page loads
    browser.implicitly_wait(10)

    # Find elements by their IDs
    text = browser.find_element(By.ID, "myText")
    button = browser.find_element(By.ID, "myButton")

    # Initial state check
    assert text.text == "Hello Current World"

    # Click the button to toggle text
    button.click()
    time.sleep(0.5)  # Wait for JavaScript to update the DOM

    # Check updated content
    assert text.text == "Hello New World"

    # Click the button to toggle text
    button.click()
    time.sleep(0.5)  # Wait for JavaScript to update the DOM

    # Check updated content
    assert text.text == "Hello Current World"

# Creating multiple separate test cases
def test_button_text_change(browser):
    # Make sure Flask app is running at this URL
    browser.get(BROWSER_URL) 

    # Add a wait to ensure the page loads
    browser.implicitly_wait(10)

    # Find elements by their IDs
    button = browser.find_element(By.ID, "myButton")

    # Initial state check
    assert button.text == "Go to New World"

    # Click the button to toggle text
    button.click()
    time.sleep(0.5)  # Wait for JavaScript to update the DOM

    # Check updated content
    assert button.text == "Go to Old World"

    # Click the button to toggle text
    button.click()
    time.sleep(0.5)  # Wait for JavaScript to update the DOM

    # Check updated content
    assert button.text == "Go to New World"    

def test_mock_1():
    assert (2+3) == 5

def test_mock_2():
    assert len("Test") == 4
