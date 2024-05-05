# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:45:45 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import json

class Driver:
    def __init__(self) -> None:
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.headless = True
        chrome_opts.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36')
        chrome_opts.add_argument('--no-sandbox')
        chrome_opts.add_argument('--disable-extensions')
        chrome_opts.add_argument('--disable-dev-shm-usage')
        
        service_path = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service_path, options=chrome_opts)

    def tear_down(self) -> None:
        if self.browser is not None:
            self.browser.quit()

class Scraper:
    def __init__(self, driver, base_url="https://food.grab.com/sg/en/restaurants"):
        self.driver = driver
        self.base_url = base_url
        self.grab_internal_post_api = "https://portal.grab.com/foodweb/v2/search"
        self.driver.browser.get(self.base_url)
        time.sleep(5)  # Adjust based on the initial load time

    def scroll_and_wait(self):
        last_height = self.driver.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)  # Adjust based on your network speed and server response time

            new_height = self.driver.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def capture_post_response(self):
        post_data = []
        for request in self.driver.browser.requests:
            if request.method == 'POST' and request.url == self.grab_internal_post_api:
                data = json.loads(request.response.body.decode("utf-8"))
                post_data.append(data)
        return post_data

    def get_restaurant_latlng(self, post_data):
        d = {}
        for p in post_data:
            for rst in p['searchResult']['searchMerchants']:
                key = rst.get('chainID', rst['address']['name'])
                d[key] = {'chainName': rst['chainName'], 'latlng': rst['latlng']}
        return d

    def scrape(self):
        self.scroll_and_wait()
        post_data = self.capture_post_response()
        return self.get_restaurant_latlng(post_data)

    def save(self, data, file='grab_restaurants_latlng.json'):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    driver = Driver()  # Assuming Driver is properly initialized and configured
    scraper = Scraper(driver)
    restaurants_latlng = scraper.scrape()
    scraper.save(restaurants_latlng)
    driver.tear_down()
