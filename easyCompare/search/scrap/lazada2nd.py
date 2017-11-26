from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lazadaScrapEngine:
	
	def scrapIt(self, link,pid):
		#url of site to scrap
		my_url =link
		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}
		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		#main container including header
		mainbigcontainer = page_soup.findAll("div",{"class":"c-review-list_js_inited"})

		pID = get_object_or_404(models.SearchItem, item_id=pid)

		for container in mainbigcontainer:
			n = 0
			comment = container.findAll("div",{"class":"c-review__comment"})
			pricediv = container.findAll("div",{"class":"c-product-card__price"})
			propicdiv = container.findAll("div",{"class":"c-product-card__img-placeholder"})
			limitloop = len(comment)
			while n!= limitloop:
				productnamelist = comment[n].a.text.strip()
				pricetaglist = pricediv[n].span.text.strip()
				piclist = propicdiv[n].a.span["data-js-component-params"]
				directlink = propicdiv[n].a["href"]
				detail_url = 'https://www.lazada.com.my' + directlink
				lcurlyr = piclist.replace("{","")
				rcurlyr = lcurlyr.replace("}","")
				srcr = rcurlyr.replace('"src"',"")
				twodotr = srcr.replace(': "',"")
				allr = twodotr.replace('"',"").strip()
				item_instance = models.Feedback.objects.create(item_id=pID,
																 rating=5,
																 comment=comment,
																 seller_rate=3,
																 seller_comment=pricetaglist)
		
		return