from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from random import randint
import csv

# Chrome Driver Path
chrome_mac_driver_path = "Driver/chromedriver_mac64"
chrome_mac_m1_driver_path = "Driver/chromedriver_mac_m1"
chrome_linux_driver_path = "Driver/chromedriver_linux64"
chrome_windows_driver_path = "Driver/chromedriver.exe"

# Other Variables
main_url = 'https://www.tokopedia.com/p/handphone-tablet/handphone?page='
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def fetch_urls(chrome_driver_path, main_url):
    urls = []
    i = 1
    while (len(urls) < 100):
        # Set up the driver and fetch the page
        driver = webdriver.Chrome(chrome_driver_path) 
        driver.get(main_url + str(i))
        # Scroll down to load another products
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Sleep to wait all loads up
        sleep(randint(5,30))
        # Convert the page source to beautiful soap
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Fetch all the product hrefs
        for url in soup.find_all('a', class_='css-89jnbj', href=True):
            urls.append(url['href'])
        # Close the driver
        driver.close()

        # remove all invalid urls
        urls = [url for url in urls if not url.startswith("https://ta.tokopedia.com/promo")]
        i+=1
    
    return urls

def save_to_csv(product_names, descriptions, image_links, prices, ratings, store_names):
    with open('tokopedia-100-handphone.csv', 'w') as file:
        # create a "writer" object
        writer = csv.writer(file, delimiter=',')
        # use "writer" obj to write 
        # you should give a "list"
        writer.writerow(["Name of Product", "Description", "Image Link", "Price", "Rating", "Store/Merchant Name",])
        for i in range(len(product_names)):
            writer.writerow([
            product_names[i], 
            descriptions[i], 
            image_links[i], 
            prices[i], 
            ratings[i], 
            store_names[i]
        ])

def scrape_product_details(chrome_driver_path, urls):
    product_names = []
    descriptions = []
    image_links = []
    prices = []
    ratings = []
    store_names = []
    # Looping through the urls
    for url in urls:
        try:
            # Setup driver for each url
            driver = webdriver.Chrome(chrome_driver_path) 
            driver.get(url)
            product_soup = BeautifulSoup(driver.page_source, 'html.parser')
            sleep(randint(5,15))

            # Fetch Product Name
            for product_name in product_soup.find_all('h1', class_='css-1320e6c'):
                try:
                    product_names.append(product_name.string.strip())
                except:
                    product_names.append("No Product Names Found, url: " + url)

            # Fetch Description
            desc_temp = []
            for description in product_soup.find('div', attrs={'data-testid': 'lblPDPDescriptionProduk'}):
                try:
                    desc_temp.append(description)
                except:
                    desc_temp.append("- url: " + url)
            # Append multiple array values into one list
            descriptions.append(list(desc_temp))

            # Fetch Price
            for price in product_soup.find_all('div', class_='price'):
                try:
                    prices.append(price.string.strip())
                except:
                    prices.append("- url: " + url)
            
            # Fetch Rating
            for rating in product_soup.find('span', attrs={'data-testid': 'lblPDPDetailProductRatingNumber'}):
                try:
                    ratings.append(rating.string.strip())
                except:
                    ratings.append("- url: " + url)

            # Fetch Image Link
            for image_link in product_soup.find_all('img', attrs={'data-testid': 'PDPMainImage'}):
                try:
                    image_links.append(image_link['src'])
                except:
                    image_links.append("- url: " + url)
            
            # Fetch Store Name
            for store_name in product_soup.select(".css-t234af h2"):
                try:
                    store_names.append(store_name.string.strip())
                except:
                    store_names.append("- url: " + url)
        except:
            print("err: " + url)
    
    return product_names, descriptions, image_links, prices, ratings, store_names

"""
Please change chrome_mac_driver_path to chrome_linux_driver_path,
in case you are using linux, or
change to chrome_windows_driver_path when you are using windows, or
change to chrome_mac_m1_driver_path when you are using mac m1 devices
"""
urls = fetch_urls(chrome_mac_driver_path, main_url)
# Take only first 100 urls
urls = urls[:100]
product_names, descriptions, image_links, prices, ratings, store_names = scrape_product_details(chrome_mac_driver_path, urls)
save_to_csv(product_names, descriptions, image_links, prices, ratings, store_names)