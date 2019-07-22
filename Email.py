import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
emailElem = driver.find_element_by_id('identifierId')
emailElem.send_keys('<Your Email ID>')
driver.find_element_by_id('identifierNext').click()

time.sleep(2)

passwordElem = driver.find_element_by_name('password')
passwordElem.send_keys('<Enter your password here>')
driver.find_element_by_id('passwordNext').click()

time.sleep(5)
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")

time.sleep(15)
toElem = driver.find_element_by_name("to")
toElem.send_keys("<Recipient Email ID>")
time.sleep(5)

subjElem = driver.find_element_by_name('subjectbox')
subjElem.send_keys('Automation Testing (TSF Task 2)')

time.sleep(2)

bodyElem = driver.find_element_by_css_selector('#\:kg')
bodyElem.send_keys('A test email with selenium')

time.sleep(2)

driver.find_element_by_css_selector('#\:ir').click()
