from bs4 import BeautifulSoup as soup
from django.shortcuts import render,get_object_or_404
from search import models
import requests


class estreetScrapEngine:

	def scrapIt(self, item):
		#url of site to scrap
		my_url = item.item_link
		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}
		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		maincontainer = page_soup.findAll("div",{"class":"wrap_category"})

		PID = get_object_or_404(models.PageCrawl, item_id = item.item_id)

		#latest one
		#specs/detail of item
		itemspec = page_soup.findAll("ul",{"class":"display-table"})
		for container in itemspec:
		    print("Specs:"+container.text.strip())
		
		#rateitem
		rateitem = page_soup.findAll("div",{"class":"product-ranking-star sprites star5"})
		for container in rateitem:
		    rateitemval = container.span["content"]
		    print("Rate Item:"+rateitemval)
			
		#rateseller
		rateseller = page_soup.findAll("dl",{"class":"product-detail-seller"})
		print(len(rateseller))

		for container in maincontainer:
			n = 0
			count = 0
			productdiv = container.findAll("h3",{"class":"product-name tit_info"})
			pricediv = container.findAll("strong",{"class":"rm_price new_price"})
			prodpic = container.findAll("div",{"class":"thumb"})
			linkdirect = prodpic[n].a["href"]
			direct_url = linkdirect
			limitloop = len(productdiv)
			while n != limitloop:
				productnamelist = productdiv[n].a.text.strip()
				pricetaglist = pricediv[n].text.strip()
				prodpiclist = prodpic[n].a.img["src"]
				item_instance = models.Feedback.objects.create(item_id=PID,
																 rating="5",
																 comment="")
				n = n + 1
				count = count+1
				if count==5:
					break

		return