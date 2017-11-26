from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lelongScrapEngine:

    def scrapIt(self, link,pid):
        my_url = link

        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(my_url)
        page_soup = soup(page.text, "html.parser")

        pID = get_object_or_404(models.SearchItem, item_id=pid)

        #for shipping
        shipcontainer = page_soup.findAll("div",{"class":"paddingtop5 paddingbottom5"})
        for container in shipcontainer:
        	infoclasspen = container.div.findAll("div",{"class":"fontsize12"})
        	infoclasssl = container.div.findAll("div",{"class":"info-lt fontsize12"})
        	checker = len(infoclasspen)

        	if checker <= 3:
        		noship = "Free Shipping or Combine Shipping"
        		print(noship)
        	else:
        		infoshippen = infoclasspen[0].text.strip()
        		infoshipsl = infoclasssl[0].text.strip()
        		infoships = infoclasssl[1].text.strip()
        		print("Shipping info (PEN. MALAYSIA) : "+infoshippen+"\nShipping info (SABAH/LABUAN) : "+infoshipsl+"\nShipping info (SARAWAK) : "+infoships)

        #for supplier rating
        ratingcontainer = page_soup.findAll("div", {"class": "seller-info-wrap"})
        for container in ratingcontainer:
            count = 0
            inforating = container.findAll("div", {"class": "fontsize12"})
            print("Seller Rating : "+inforating[1].b.a.text)
            item_instance = models.Feedback.objects.create(item_id=pID,
                                                               rating=5,
                                                               comment=inforating,
                                                               seller_rate=3,
                                                               seller_comment='')
            count = count + 1
            if count == 5:
                break

        return


