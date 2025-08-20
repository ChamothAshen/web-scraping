from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tempfile  # Import tempfile for creating a unique directory

class LinkedInScraper:
    def __init__(self, email, password, headless=True):
        self.email = email
        self.password = password

        # --- Chrome options ---
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # runs Chrome in background
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")       # suppress most Chrome logs
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-webgl")  # Disable WebGL
        options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
        options.add_argument("--disable-logging")  # Suppress logging
        options.add_argument("--disable-in-process-stack-traces")  # Suppress stack traces

        # Set a unique temporary user data directory
        self.temp_user_data_dir = tempfile.TemporaryDirectory()
        options.add_argument(f"--user-data-dir={self.temp_user_data_dir.name}")

        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        self.driver.find_element(By.ID, "username").send_keys(self.email)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
        time.sleep(3)

    def scrape_profile(self, profile_url):
        self.driver.get(profile_url)
        time.sleep(3)

        try:
            name = self.driver.find_element(By.CSS_SELECTOR, "h1").text.strip()
        except:
            name = "N/A"

        try:
            job_title = self.driver.find_element(By.CSS_SELECTOR, ".text-body-medium").text.strip()
        except:
            job_title = "N/A"

        try:
            location = self.driver.find_element(By.CSS_SELECTOR, ".text-body-small").text.strip()
        except:
            location = "N/A"

        return {
            "name": name,
            "job_title": job_title,
            "location": location
        }

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None  # Ensure the driver is fully closed
        if self.temp_user_data_dir:
            try:
                self.temp_user_data_dir.cleanup()  # Clean up the temporary directory
            except PermissionError as e:
                print(f"Warning: Failed to clean up temporary directory: {e}")
