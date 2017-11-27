from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lazadaScrapEngine:
	
	def scrapIt(self, item):
		#url of site to scrap
		my_url =item.item_link

		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}

		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		#main container including header
		mainbigcontainer = page_soup.findAll("div",{"class":"c-review-list_js_inited"})

		pID = get_object_or_404(models.SearchItem, item_id=item.item_id)

		""" new scrap
		#specs
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
		"""

		for container in mainbigcontainer:
			n = 0
			comment = container.findAll("div",{"class":"c-review__comment"})
			pricediv = container.findAll("div",{"class":"c-product-card__price"})
			propicdiv = container.findAll("div",{"class":"c-product-card__img-placeholder"})
			limitloop = len(comment)
			while n!= limitloop:
				item_instance = models.Feedback.objects.create(item_id=pID,
																 rating=5,
																 comment=comment)
		
		return