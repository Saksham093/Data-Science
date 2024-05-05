# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:19:46 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    # Set up ChromeDriver (ensure it's added to PATH or specify the path directly)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    print(service)
    
    # Open a website to verify it's working
    driver.get("http://www.google.com")
    
    # If the above line runs without errors, Chromedriver is working
    print("Chromedriver is working!")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Make sure to close the browser window
    driver.quit()
