# Tokopedia Product Scraper

## Description
The purpose of this scraper is to extract the top 100 mobile phones product from tokopedia and save it to csv file.
The data includes:
<li>Name of Products</li>
<li>Descriptions</li>
<li>Image Links</li>
<li>Price</li>
<li>Ratings</li>
<li>Store / Merchant Name</li>

## How does this scraper work?
1. The driver will access the main url first, which is the link to Tokopedia Mobile Phone Product Page.
2. Fetching top 100 product urls.
3. After all the urls have been collected, driver will go through each url one by one, to collect the data we need.
4. After all the data have been collected, save it into csv file.
## Tech Stack & Dependencies being used
<li>Python 3.8</li>
<li>Selenium</li>
<li>BeautifulSoup4</li>
<li>ChromeDriver v103</li>

## How to run
1. Activate virtualenv
> source venv/bin/activate
2. Inside venv terminal
> python3 scraper.py

###### Notes: 
Please change `chrome_mac_driver_path` to `chrome_linux_driver_path`, in case you are using linux, or change to `chrome_windows_driver_path` when you are using windows, or change to `chrome_mac_m1_driver_path` when you are using mac m1 devices

## What is Web Scraping
Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user. Be it a spreadsheet or an API. Although web scraping can be done manually, in most cases, automated tools are preferred when scraping web data as they can be less costly and work at a faster rate.

## How this can be implemented for e-commerce website
1. It can be used to populate their product database, where in this case they get to act as the agent of those products when someone find the listings on their sites.
2. It can be used to analyzed the data, for example we can analyze it to measure what kind of products are currently popular now.
3. It can be used to compare the product data and price between each e-commerce sites with our e-commerce sites.

## References
<li>https://itnext.io/lets-build-a-web-scraper-with-python-beautifulsoup4-2b550d10438</li>
<li>https://www.parsehub.com/blog/what-is-web-scraping/</li>