import time
import re
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

start = time.time()


# function to scrape a single page
def scrape_page(page):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    page_url = "https://www.greens.com.mt/products?cat=all&loc=GZ&pg=" + str(page) + "&sort=Position&sortd=Asc"
    driver.get(page_url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    products = soup.find_all("div", {"class": "product"})

    # initialize an empty list to hold the data for this page
    page_data = []

    for product in products:
        product_title = product.find("a", {"class": "title product-title"})
        if product_title:
            product_name = product_title.text.strip()
        else:
            product_name = ""

        prev_price_id = [x for x in product.find_all("div") if x.get("id") and x.get("id").startswith("divPrevQuick")]
        if prev_price_id:
            prev_price = prev_price_id[0].text.strip()
        else:
            prev_price = "NA"

        curr_price_id = [x for x in product.find_all("div") if
                         x.get("id") and x.get("id").startswith("divCurrentQuick")]
        if curr_price_id:
            curr_price = curr_price_id[0].text.strip()
        else:
            curr_price = ""

        discount = product.find("div", {"class": "special-offer-text"})
        if discount:
            special_offer = discount.text.strip()
        else:
            special_offer = "NA"

        image_tag = product.find("img", {"class": "product-image-img"})
        if image_tag:
            image_url = "https://www.greens.com.mt" + image_tag["src"]
        else:
            image_url = ""

        category_ = product.find("a", {"class": "tag"})
        category_href = category_.get('href')
        category_href = re.search(r'(?<=cat=)\w+', category_href).group(0)
        if category_href:
            category = category_href.capitalize()
        else:
            category = ""

        sub_category = product.find("a", {"class": "tag"})
        if sub_category:
            sub_category_value = sub_category.text.strip()
        else:
            sub_category_value = ""

        page_data.append([product_name, prev_price, curr_price, special_offer, image_url, category, sub_category_value])

    driver.quit()

    return page_data


# initialize an empty list to hold the data for all pages
element_list = []

# create a thread pool with workers
with ThreadPoolExecutor(max_workers=10) as executor:
    # submit tasks for scraping each page
    futures = [executor.submit(scrape_page, page) for page in range(1, 5)]

    # iterate through the futures as they complete and add the data to the final list
    for future in futures:
        page_data = future.result()
        element_list.extend(page_data)

df = pd.DataFrame(element_list,
                  columns=["product_name", "prev_price", "curr_price", "special_offer", "image_url", "category",
                           "sub-category"])

df.to_csv("greens_data_gz.csv", index=True, encoding="utf-8")
end = time.time()
print(end - start)
