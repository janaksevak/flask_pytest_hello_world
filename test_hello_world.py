import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import tempfile

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

def test_toggle_world_text(browser):
    # Make sure Flask app is running at this URL
    # browser.get("http://localhost:5000") 
    browser.get("http://127.0.0.1:5000") 

    # Add a wait to ensure the page loads
    browser.implicitly_wait(10)

    # Find elements by their IDs
    text = browser.find_element(By.ID, "myText")
    button = browser.find_element(By.ID, "myButton")

    # Initial state check
    assert text.text == "Hello Current World"
    assert button.text == "Go to New World"

    # Click the button to toggle text
    button.click()
    time.sleep(0.5)  # Wait for JavaScript to update the DOM

    # Check updated content
    assert text.text == "Hello New World"
    assert button.text == "Go to Old World"
