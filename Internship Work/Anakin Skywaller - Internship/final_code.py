# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:50:35 2024

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
        self.browser = webdriver.Chrome(service=service_path, chrome_options = chrome_opts)

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
        sleep(60)

    def load_more(self):
        del self.driver.browser.requests  # to clear previously captured requests

        # try:
        #     last_height = self.driver.browser.execute_script("return document.body.scrollHeight")

        #     while True:
        #         # Scroll down to the bottom of the page
        #         self.driver.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
        #         # Wait for new data to load
        #         WebDriverWait(self.driver.browser, 60, poll_frequency=1).until(
        #             lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height)
                
        #         new_height = self.driver.browser.execute_script("return document.body.scrollHeight")
        #         if new_height == last_height:
        #             break
        #         last_height = new_height

        #         sleep(60)

        # except TimeoutException:
        #     print("No more content to load or page took too long to respond.\n")
        
        # CSS selector
        css_selector = ".footerNew___2PBRV.ant-layout"

        try:
            footer_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )

            last_height = self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
            while True:
                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                footer_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)


                # Wait for the page to load and new content to appear
                WebDriverWait(self.driver, 10, poll_frequency=1).until(
                    lambda d: d.execute_script("arguments[0].scrollIntoView(true);", footer_element) > last_height
                )

                # Verify if new content has loaded or if we're at the end
                new_height = self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
                if new_height == last_height:
                    # Scroll a bit up and down to trigger loading just in case, then break if no new height
                    # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
                    footer_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)

                    sleep(2)  # Short delay before trying to trigger load one last time
                    footer_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)

                    sleep(5)  # Wait a bit to see if this last attempt triggered any new data loading
                    
                    new_height = self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
                    if new_height == last_height:
                        print("Reached the bottom of the page.")
                        break

                last_height = new_height

        except TimeoutException:
            print("No more content to load or page took too long to respond.\n")



    def capture_post_response(self):  # capture the post response
        post_data = []

        for r in self.driver.browser.iter_requests():
            if r.method == 'POST' and r.url == self.grab_internal_post_api:  # capture the post response

                data_1 = sw_decode(r.response.body, r.response.headers.get('Content-Encoding', 'identity'))  # decode the response
                data_1 = data_1.decode("utf8")

                data = json.loads(data_1) # convert the response to json
                post_data.append(data)
                # print(post_data)
        return post_data

    def get_restaurant_data(self, post_data):
        d = {}

        for p in post_data: # get the restaurants data
            l = p['searchResult']['searchMerchants']  # list of restaurants
            for rst in l: # for each restaurant
                try:
                    d[rst['id']] = {'restaurantName': rst['address']['name'],
                                         'restaurantCuisine': rst['merchantBrief']['cuisine'],
                                         'restaurantRating': rst['merchantBrief']['rating'],
                                         'estimateDeliveryTime': rst['estimatedDeliveryTime'],
                                         'distanceFromLocation': rst['merchantBrief']['distanceInKm'],
                                         'promotionalOffers': rst['merchantBrief']['promo']['description'],
                                         'noticeIfVisible': rst['merchantBrief']['closingSoonText'],
                                         'imageLink': rst['merchantBrief']['photoHref'],
                                         'isPromoAvailable': rst['merchantBrief']['promo']['hasPromo'],
                                         'restaurantID': rst['id'],
                                         'latlng': rst['latlng'],
                                         'estimateDeliveryFee': rst['estimatedDeliveryFee']['priceDisplay']},

                except Exception:
                    print(rst)
        return d

    def scrape(self):
        self.load_more()  # load more restaurants in the list
        post_data = self.capture_post_response()  # capture the post response
        restaurants_data_ = self.get_restaurant_data(post_data)  # get the restaurants data
        return restaurants_data_

    # save data as gzip of ndjson
    def save_data_as_gzip_ndjson(data, file_name):
        with gzip.open(file_name, 'wt', encoding='UTF-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')


if __name__ == "__main__":
    base_url = "https://food.grab.com/sg/en/restaurants"
    driver_path = Service(ChromeDriverManager().install())
    driver = Driver()  # initialize the driver
    scraper = Scraper(driver, base_url)  # initialize the scrape
    restaurants_data = scraper.scrape()  # scrape the restaurants data
    # scraper.save_data_as_gzip_ndjson(restaurants_data, 'grab_food_data.gz')
    print(restaurants_data)
    print(len(restaurants_data))
    driver.tear_down()
