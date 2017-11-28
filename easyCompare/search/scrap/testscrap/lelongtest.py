from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.lelong.com.my/catalog/all/list?TheKeyword=corsair'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)
page_soup = soup(page.text, "html.parser")

allLellongProduct = []

bigcontainer = page_soup.findAll("div",{"class":"item"})

n = 1

for container in bigcontainer:
	productpic  = container.findAll("div",{"class":"pic-box"})
	productname = container.findAll("div",{"class":"summary"})
	pricetag = container.findAll("span",{"class":"price pull-right"})
	productnamelist = productname[0].a.text.strip()
	pricetaglist = pricetag[0].b.text.strip()
	piclist = productpic[0].a.span.img["data-original"]
	linkdirect = productname[0].a["href"]
	direct_url = linkdirect.replace("//","")
	print(n, productnamelist, pricetaglist, piclist, direct_url)
	n = n + 1

