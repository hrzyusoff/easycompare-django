from django.shortcuts import render,get_object_or_404
from bs4 import BeautifulSoup as soup
from search import models
import requests

class carousellScrapEngine:

	def scrapIt(self, cconcatURL):
		my_url = cconcatURL
		#headers used to treat like human request 
		#not using urllib because  it is like treat of bot
		headers = {'User-Agent':'Mozilla/5.0'}
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		page = get_object_or_404(models.PageCrawl, pk=9)

		maincontainer = page_soup.findAll("div",{"class":"row card-row"})
		for container in maincontainer:
			prodname = container.findAll("h4",{"id":"productCardTitle"})
			prodprice = container.findAll("span",{"class":"n-n"})
			picdiv = container.findAll("a",{"class":"n-e"})
			limitloop = len(prodname)
			n = 0
			count = 0
			while n != limitloop:
				prodnamelist = prodname[n].text
				prodpricelist = prodprice[n]["title"]
				piclist = picdiv[n].img["src"]
				item_instance = models.SearchItem.objects.create(page=page,
														  price=pricetaglist,
														  title=productnamelist,
														  pic=piclist,
														  rating=0,
														  detail=' ',
														  item_link=' ',
														  condition='',
														  location='',
														  URLstrip=URLStrip)
				n = n+1
				count = count+1
				if count==10:
					break
		return