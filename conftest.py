import pytest
import os
import tempfile
from selenium import webdriver

@pytest.fixture
def selenium(request):
    # Create a unique temporary directory for Chrome
    temp_dir = tempfile.mkdtemp()
    
    options = webdriver.ChromeOptions()
    # Essential for CI environments
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir={temp_dir}")
    # Disable shared memory usage which can cause issues in CI
    options.add_argument("--disable-features=VizDisplayCompositor")
    # Use a fixed port to avoid conflicts
    options.add_argument("--remote-debugging-port=9222")
    
    # Explicitly set browser binary location if needed (sometimes required in CI)
    # options.binary_location = "/usr/bin/google-chrome"
    
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    # Make sure we quit the driver
    try:
        driver.quit()
    except:
        pass
    
    # Clean up temp directory
    try:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
    except:
        pass