# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url='https://www.makemytrip.com/flight/search?itinerary=BOM-CCU-18/08/2024&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
driver.get(url)
fares=driver.find_element(By.CLASS_NAME,'listingCard')

data = fares.get_attribute('outerHTML')
with open('I:/Programming/Python/Jupyter/venv/flights/yatra.html','w',encoding='utf-8') as f:
    f.write(data)
            
sleep(40)
driver.close()