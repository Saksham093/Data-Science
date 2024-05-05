# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:57:27 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

import json
import gzip
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
from seleniumwire.utils import decode as sw_decode

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Driver class for the browser
class Driver:
    def __init__(self) -> None:
        self.browser = None
        self.setup()

    # Setup the browser
    def setup(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.headless = True
        user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' + 
                      'Chrome/60.0.3112.50 Safari/537.36')  # Set the user agent
        chrome_opts.add_argument(f'user-agent={user_agent}')  # Add the user agent
        chrome_opts.add_argument('--no-sandbox')  # Disable sandbox
        chrome_opts.add_argument("--disable-extensions")  # Disable extensions
        chrome_opts.add_argument('--disable-dev-shm-usage')  # Disable shared memory

        # Set up ChromeDriver
        service_path = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service_path, options = chrome_opts)

    # Close the browser
    def tear_down(self):
        self.browser.quit()


# Class for the XHR requests and responses
class Scraper:
    #  initialize the scraper
    def __init__(self, driver: Driver, base_url) -> None:
        self.driver = driver  # initialize the driver
        self.base_url = base_url  # initialize the base url
        self.grab_internal_post_api = "https://portal.grab.com/foodweb/v2/search"  # initialize the grab-foods internal post api
        self._init_request()  # initialize the request

    def _init_request(self):
        self.driver.browser.get(self.base_url)
        # sleep(60)
    
        # CSS selector
        css_selector = ".footerNew___2PBRV.ant-layout"
        
        footer_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
        driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)


        last_height = self.driver.browser.execute_script("return document.body.scrollHeight")
        print(last_height)
        
# # Initialize the WebDriver instance
# driver = webdriver.Chrome()  # Adjust based on your preferred browser

# # Open the webpage
# driver.get("https://food.grab.com/sg/en/restaurants")

# # Adjust the CSS selector if needed, ensuring it matches exactly how it's defined in the webpage's HTML
# css_selector = ".footerNew___2PBRV.ant-layout"

# try:
#     last_height = driver.browser.execute_script("return document.body.scrollHeight")
#     print(last_height)
#     # Use WebDriverWait to wait for the footer element to be clickable or visible
#     # This approach ensures that the script waits until the element is fully loaded and interactable
#     footer_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)

#     # Optionally, add a short delay after scrolling to ensure any lazy-loaded elements become visible
#     time.sleep(60)

#     # Continue with your scraping tasks here

# finally:
#     # Close the driver after your job is done
#     driver.quit()










if __name__ == "__main__":
    base_url = "https://food.grab.com/sg/en/restaurants"
    driver_path = Service(ChromeDriverManager().install())
    driver = Driver()  # initialize the driver
    scraper = Scraper(driver, base_url)  # initialize the scrape
    # restaurants_data = scraper.scrape()  # scrape the restaurants data
    # scraper.save_data_as_gzip_ndjson(restaurants_data, 'grab_food_data.gz')
    # print(restaurants_data)
    # print(len(restaurants_data))
    driver.tear_down()


