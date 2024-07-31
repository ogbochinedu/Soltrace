from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Automate:
    def start(self):
        # Set up Chrome options (if needed)
        chrome_options = Options()
        # Uncomment if you want to run Chrome in headless mode
        # chrome_options.add_argument("--headless")

        try:
            # Create a Service object with the path to the ChromeDriver
            service = Service('/Users/macbook/Documents/chromedriver_mac64/chromedriver')

            # Initialize the WebDriver with service and options
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Open the Python website
            driver.get("https://www.python.org")
            print(driver.title)

            # Close the browser
            driver.quit()
            return "ok"

        except Exception as e:
            print(f"An error occurred: {e}")
            return "error"



