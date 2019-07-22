import urllib.request
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver

driver = webdriver.Chrome()
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

query = "kittens"
url = "https://www.google.com/search?q="+query+"&tbm=isch&source=lnms"
driver.get(url)
driver.maximize_window()

soup = make_soup(url)
i=0
while i < 10:
    for img in soup.findAll('img'):
        temp=img.get('src')
        image = temp
        filename = i
        imagefile = open(filename + ".jpeg",'wb')
        imagefile.write(urllib.request.urlopen(image).read)
        imagefile.close()
        i+=1


