from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lazadaScrapEngine:
<<<<<<< HEAD

    def scrapIt(self, item):
        my_url = item.item_link

        headers = {'User-Agent':'Mozilla/5.0'}

        page = requests.get(my_url)

        page_soup = soup(page.text, "html.parser")

        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)

        mainbigcontainer = page_soup.findAll("div", {"class":"c-review-list_js_inited"})

        # spec/detail of product
        itemspec = page.soup.findAll("ul", {"class": "display-table"})
        for container in itemspec:
            print("spec:" + container.text.strip())

        rateitem = page_soup.findAll("div", {"class": "product-ranking-star sprites star5"})
        for container in rateitem:
            rateitemval = container.span["content"]
            print("Rate item:" + rateitemval)

        rateseller = page_soup.findAll("dl", {"class": "product-detail-seller"})
        print(len(rateseller))

        for container in mainbigcontainer:
            n = 0
            count = 0
            comment = container.findAll("div", {"class": "c-review__comment"})
            limitloop = len(comment)
            while n!= limitloop:
                item_instance = models.SearchItem.objects.create(item=PID,
                                                                 rating="5",
                                                                 comment=comment)

                count = count+1
                if count == 5:
                    break

        return
=======
	
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
>>>>>>> c9451aa556d0f06310416f6cbeb86926579c93d0
