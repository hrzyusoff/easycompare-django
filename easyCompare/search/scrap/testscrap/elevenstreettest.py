from bs4 import BeautifulSoup as soup
import requests

#url of site to scrap
my_url = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd=xiaomi'
#to act like human that browse from browser
headers = {'User-Agent':'Mozilla/5.0'}
#do requesting to act like human not bot
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")

maincontainer = page_soup.findAll("div",{"class":"wrap_category"})

allestreetproduct = []

for container in maincontainer:
	n = 0
	productdiv = container.findAll("h3",{"class":"product-name tit_info"})
	pricediv = container.findAll("span",{"class":"rm_price old_price"})
	prodpic = container.findAll("div",{"class":"thumb"})
	limitloop = len(productdiv)
	while n != limitloop: 
		prodpiclist = prodpic[n].a.img["src"]
		linkdirect = prodpic[n].a["href"]
		direct_url = linkdirect
		productnamelist = productdiv[n].a.text.strip()
		pricetaglist = pricediv[n].text.strip()
		n = n + 1
		print(n, productnamelist, pricetaglist, prodpiclist, direct_url)