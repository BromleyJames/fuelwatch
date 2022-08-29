import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


# Base URL - in future, import from the TOML file

url_base = "https://www.fuelwatch.wa.gov.au/"
historic_data_uri = "retail/historic"
request_header = {
    "User-Agent" :
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

earliest_data = "2001-01"
#Calculate the last calendar month from today's date
latest_data  = None

page = requests.get(url_base, headers=request_header)
print(page.text)

service = Service() # Ensure that chromedriver is on your path, if using Chrome
driver = webdriver.Chrome(service=service) # currently Chrome is the only supported browser and is hard-coded
