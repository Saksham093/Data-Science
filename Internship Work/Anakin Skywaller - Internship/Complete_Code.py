# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:11:50 2024

@Author: M.SAKSHAM
@GitHub: Saksham093
"""

import re
import json
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def read_urls_from_excel(file_path, sheet_name=0):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    urls = df.iloc[:, 0].tolist()
    return urls


def clean_urls(urls):
    cleaned_urls = []
    for url in urls:
        # Check if the input starts with "http" to determine if it's a URL...
        if url.startswith("http"):
            # Use regular expression to match the base URL part up to ".com/"...
            match = re.search(r'(https?://[^/]*\.com/)', url)
            if match:
                # Append the matched base URL to the cleaned_urls list...
                cleaned_urls.append(match.group(1))
            else:
                # If no match is found within the expected pattern, ignore this input...
                continue
        else:
            # If the input doesn't start with "http", ignore it as well...
            continue
    return cleaned_urls


def collect_stakes_data(url, user_name, driver):
    stakes_data = {url: {}}
    tables = driver.find_elements(By.CSS_SELECTOR, "table.tbl")
    for table in tables:
        if 'Stakes' in table.find_element(By.TAG_NAME, "thead").text:
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
            stake_count = 1
            for row in rows:
                data_cells = row.find_elements(By.TAG_NAME, "td")
                if len(data_cells) >= 3:
                    picks = data_cells[1].text.strip()
                    profit = data_cells[2].text.strip()
                    if user_name not in stakes_data[url]:
                        stakes_data[url][user_name] = {}
                    stakes_data[url][user_name][f'Stake {stake_count}'] = {'Picks': picks, 'Profit': profit}
                    stake_count += 1
    return stakes_data


def visit_and_process_url(url):
    if not url:
        print("No URLs found.")
        return {}

    driver = webdriver.Chrome()
    driver.get(url)

    collected_data = {url: {}}
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))
        username_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.enable-tooltip"))
        )
        username_text = username_element.text
        user_name = username_text.split("Hi, I'm ")[-1].replace('!', '').strip()
        
        blog_menu_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "currentTab")))
        blog_menu_element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'PICKS ARCHIVE')]"))).click()

        time.sleep(10)

        try:
            clear_filters_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-group margin-bottom-10']//button[contains(@onclick, 'clearAllFilters();')]"))
            )
            clear_filters_button.click()
            print("Filters cleared.")
            time.sleep(5)
        except Exception as e:
            print("Clear filters button not found, proceeding with data collection.")

        collected_data.update(collect_stakes_data(url, user_name, driver))

    except Exception as e:
        print(f"An error occurred: {e}")
        collected_data[url] = {}
    finally:
        driver.quit()
    return collected_data


if __name__ == "__main__":
    # file_path = "./blogabet links.xlsx"
    # sheet_name = "Sheet1"
    # urls = read_urls_from_excel(file_path, sheet_name)

    urls = ['https://slavstips.blogabet.com/',
            'https://dogoman.blogabet.com/',
            'https://m2picks.blogabet.com/',
            'https://gellero94.blogabet.com/']

    # Clean the URLs...
    cleaned_urls = clean_urls(urls)

    all_data = {}
    for url in cleaned_urls:
        dt = visit_and_process_url(url)
        all_data.update(dt)

    # Save all collected data to a single JSON file...
    json_filename = "all_stakes_data.json"
    with open(json_filename, 'w') as f:
        json.dump(all_data, f, indent=4)
    print(f"Data saved : {json_filename}")

    # Load JSON data...
    with open('all_stakes_data.json') as f:
        data = json.load(f)

    # Prepare data for DataFrame...
    rows = []
    
    # Determine the maximum number of stakes for the column headers...
    max_stakes = max((len(stakes) for stakes_info in data.values() for stakes in stakes_info.values()), default=0)

    for url, stakes_info in data.items():
        for user_name, stakes in stakes_info.items():
            row = {"Links": url, "User_Name": user_name}
    
            # Generate dynamic columns for stakes...
            for stake_num in range(1, max_stakes + 1):
                stake_key = f"Stake {stake_num}"
                if stake_key in stakes:
                    row[f'{stake_key} Picks'] = stakes[stake_key].get("Picks", '')
                    row[f'{stake_key} Profit'] = stakes[stake_key].get("Profit", '')
                else:
                    row[f'{stake_key} Picks'] = ''
                    row[f'{stake_key} Profit'] = ''

            rows.append(row)

    # Determine the maximum number of stakes for the column headers...
    column_order = ["Links", "User_Name"] + [f"Stake {i} {detail}" for i in range(1, max_stakes + 1) for detail in ["Picks", "Profit"]]
    
    # Create DataFrame with the specified column order...
    df = pd.DataFrame(rows, columns=column_order)
    
    # Export DataFrame to Excel...
    excel_path = 'Final_Data_S.xlsx'
    df.to_excel(excel_path, index=False)
    
    # Returning the path for downloading...
    excel_path
