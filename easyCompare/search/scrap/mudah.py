from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from django.shortcuts import render,get_object_or_404
from search import models

class mudahScrapEngine:

	def scrapIt(self, mconcatURL):
		my_url = mconcatURL

		#opening up connection, grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		#html parsing
		page_soup = soup(page_html, "html.parser")

		maincontainers = page_soup.findAll("div",{"class":"footerline listing_right list_ads list_big_thumbnail"})

		page = get_object_or_404(models.PageCrawl, pk=7)
		count = 0
		for container in maincontainers:
			subcontainer = container.findAll("div",{"class":"top_params_col1"})
			brandnamelist = subcontainer[0].h2.a["title"]
			direct_url = subcontainer[0].h2.a["href"]
			brandprice = subcontainer[0].findAll("div",{"class":"ads_price"})
			brandpricelist = brandprice[0].text.strip()
			prodpic = container.findAll("div",{"class":"thumbnail_images"})
			prodpiclist = prodpic[0].a.img["src"]
			URLStrip = brandnamelist.strip().replace(" ", "-")
			item_instance = models.SearchItem.objects.create(page=page,
															 price=brandpricelist,
															 title=brandnamelist,
															 pic=prodpiclist,
															 rating=0,
															 detail=' ',
															 item_link=direct_url,
															 condition='',
															 location='',
															 URLstrip=URLStrip)
			count = count + 1
			if count == 3:
				break

		return
