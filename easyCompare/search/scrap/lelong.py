from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lelongScrapEngine:

	def scrapIt(self, llconcatURL):
		my_url = llconcatURL
		headers = {'User-Agent':'Mozilla/5.0'}
		page = requests.get(my_url)
		page_soup = soup(page.text, "html.parser")

		page = get_object_or_404(models.PageCrawl, pk=10)

		bigcontainer = page_soup.findAll("div",{"class":"item"})
		
		count = 0
		for container in bigcontainer:
			productname = container.findAll("div",{"class":"summary"})
			pricetag = container.findAll("span",{"class":"price pull-right"})
			productpic  = container.findAll("div",{"class":"pic-box"})
			productnamelist = productname[0].a.text.strip()
			pricetaglist = pricetag[0].b.text.strip()
			piclist = productpic[0].a.span.img["data-original"]
			linkdirect = productname[0].a["href"]
			direct_url = linkdirect.replace("//","http://")
			item_instance = models.SearchItem.objects.create(page=page,
															 price=pricetaglist,
															 title=productnamelist,
															 pic=piclist,
															 rating=0,
															 detail=' ',
															 item_link=direct_url,
															 condition='',
															 seller_rate='',
															 shipping='')
			count = count + 1
			if count == 5:
				break

		return
