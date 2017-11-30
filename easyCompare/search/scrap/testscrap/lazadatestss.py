from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests

#selenium
chromepath = "C:/Users/HRZ/Downloads/Compressed/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromepath)
driver.get("https://www.lazada.com.my/whiskas-mackerel-12kg-17473990.html")

page = driver.page_source
page_soup = soup(page,"html.parser")

maincontainer = page_soup.findAll("div",{"class":"product-description__block"})
productrate = page_soup.find("div",{"class","c-rating-total__text-rating-average"})
print(productrate.em.text)
for container in maincontainer:
	custcomment = container.findAll("div",{"class","c-review__comment"})

	limitloop = len(custcomment)
	n = 0
	while n!= limitloop:
		commentlist = custcomment[n].text.strip()
		print(n, commentlist)
		n=n+1

driver.close()