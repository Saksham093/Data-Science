# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:50:40 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

import json
from time import sleep

import gzip

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
from seleniumwire.utils import decode as sw_decode

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver: 
    def __init__(self) -> None:
        self.browser = None
        self.setup()

    def setup(self): # Setup the browser
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.headless = True  # In headless mode, it’s possible to run large scale web application tests, navigate from page to page without human intervention
        user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' + 
                      'Chrome/60.0.3112.50 Safari/537.36') # Set the user agent
        chrome_opts.add_argument(f'user-agent={user_agent}') # Add the user agent
        chrome_opts.add_argument('--no-sandbox') # Disable sandbox
        chrome_opts.add_argument("--disable-extensions") # Disable extensions
        chrome_opts.add_argument('--disable-dev-shm-usage') # Disable shared memory

        options = { # Set the options for the browser to use the chrome driver and the options
            'exclude_hosts': [
                'google-analytics.com',
                'analytics.google.com',
                'google.com',
                'facebook.com',
                'stats.g.doubleclick.net',
            ],
        }
        #A list of addresses for which Selenium Wire should be bypassed entirely. Note that if you have configured an upstream proxy then requests to excluded hosts will also bypass that proxy.
        
        # Set up ChromeDriver (ensure it's added to PATH or specify the path directly)
        service_path = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service_path)  # Create the browser and open the url in it and wait for the page to load completely

    def tear_down(self):  # Close the browser
        self.browser.quit()


# Above is the driver class for the browser and the below is the class for the XHR requests and responses  


class Scraper:  
    """
    Given a base_url, capture all restaurants (based on user's submitted location, e.g., sg) latitude & longitude
    by intercepting grab-foods internal POST request.
    self.grab_internal_post_api is found by manually inspecting all XHR made my grab-foods, using chrome dev tools.
    """

    def __init__(self, driver: Driver, base_url: str = "https://food.grab.com/sg/en/restaurants") -> None:  #  initialize the scraper
        self.driver = driver # initialize the driver
        self.base_url = base_url # initialize the base url
        self.grab_internal_post_api = "https://portal.grab.com/foodweb/v2/search"  # initialize the grab-foods internal post api
        self._init_request() # initialize the request

    def _init_request(self):
        self.driver.browser.get(self.base_url)
        sleep(60)

    def load_more(self):  # clicking load more button to load more restaurants in the list
        del self.driver.browser.requests # to clear previously captured requests and HAR entries, use del

        condition = EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "ant-btn ant-btn-block")]')) # find element in Document Object Model (DOM)

        # more_results_button = WebDriverWait(self.driver.browser, 60, poll_frequency=1).until(condition) # wait for 10 seconds for the load more button to be present and deafult poll freqency is 0.5 second
        # print('more_results_button: ', more_results_button, '\n') # print the load more button
        # more_results_button.click() # click on the load more button
        # sleep(60)

        # page_num = 1
        # while more_results_button: # while the load more button is present in the page
        #     try:
        #         print('page_num: ', page_num)
        #         more_results_button.click() # click the load more button
        #         more_results_button = WebDriverWait(self.driver.browser, 60, poll_frequency=1).until(condition) # wait for the load more button to appear
        #         page_num += 1 # increment the page number
        #         sleep(60)
        #     except TimeoutException:
        #         print("No more LOAD MORE RESULTS button to be clicked!!!\n") # if no more load more button to be clicked, break the loop
        #         break
            
        try:
            last_height = self.driver.browser.execute_script("return document.body.scrollHeight")
            max_scrolls=2
            scrolls = 0
            while True:
                # Scroll down to the bottom of the page
                self.driver.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                # Wait for new data to load
                WebDriverWait(self.driver.browser, 60, poll_frequency=1).until(
                    lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height)
                
                new_height = self.driver.browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break  # If the scroll height hasn't changed, assume we've hit the bottom
                last_height = new_height
                scrolls += 1
                
                # Optionally, you can wait a fixed time or for a specific condition after each scroll
                sleep(60)  # Adjust sleep time as needed
                
        except TimeoutException:
            print("No more content to load or page took too long to respond.\n")

    # Your additional methods here


    def capture_post_response(self):  # capture the post response from grab-foods
        post_data = []
        for r in self.driver.browser.iter_requests(): # Returns an iterator over captured requests. Useful when dealing with a large number of requests.
            if r.method == 'POST' and r.url == self.grab_internal_post_api:  # capture the post response
                # print(f"r.response.status_code: {r.response.status_code}, r.response.reason: {r.response.reason}")

                data_1 = sw_decode(r.response.body, r.response.headers.get('Content-Encoding', 'identity'))  # decode the response
                data_1 = data_1.decode("utf8") # decode the response

                data = json.loads(data_1) # convert the response to json
                post_data.append(data)
                # print(post_data)
        return post_data

    def get_restaurant_latlng(self, post_data):
        # expalin above function to understand the code 
        d = {}
        for p in post_data: # get the restaurants latlng from the post response and save it in a dictionary
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

                except Exception as err: # if the chainID is not present in the dictionary
                    # d[rst['address']['name']] = {'chainName': rst['address']['name'], 'latlng': rst['latlng']} # address is the key for the dictionary
                    print(rst)
                    # print(type(err), err)
        return d

    def scrape(self):
        self.load_more()  # load more restaurants in the list
        post_data = self.capture_post_response()  # capture the post response  from grab-foods (list of restaurants)
        restaurants_latlng = self.get_restaurant_latlng(post_data)  # get the restaurants latlng from the post response and save it in a dictionary
        return restaurants_latlng

    # def save(self, restaurants_latlng, file: str = 'grab_restaurants_latlng.json'):  # save the dictionary to a json file
    #     with open(file, 'w') as f:  # save the dictionary to a json file
    #         json.dump(restaurants_latlng, f, indent=4) # indent=4 is for pretty printing the json file
            
    def save_data_as_gzip_ndjson(data, file_name):
        with gzip.open(file_name, 'wt', encoding='UTF-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')


if __name__ == "__main__":
    # driver_path = 'C:/Users/M.SAKSHAM/Desktop/Anakin/chromedriver_win32'  # path to the chromedriver
    base_url = "https://food.grab.com/sg/en/restaurants"  # base url of the website
    # Set up ChromeDriver (ensure it's added to PATH or specify the path directly)
    driver_path = Service(ChromeDriverManager().install())
    driver = Driver()  # initialize the driver
    scraper = Scraper(driver, base_url)  # initialize the scraper
    restaurants_data = scraper.scrape() # scrape the restaurants latlng
    # scraper.save(restaurants_data)  # save the restaurants latlng to a json file
    scraper.save_data_as_gzip_ndjson(restaurants_data, 'grab_food_data.gz')
    driver.tear_down() # tear down the driver