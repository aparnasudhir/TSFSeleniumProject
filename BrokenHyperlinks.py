import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

driver=webdriver.Chrome(chrome_options=options, executable_path="C:\Windows\Chromedriver.exe")

driver.get('https://google.co.in/')
links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)
