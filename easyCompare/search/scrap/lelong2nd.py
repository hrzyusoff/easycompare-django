from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lelongScrapEngine:

    def scrapIt(self, item):
        my_url = item.item_link

        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(my_url)
        page_soup = soup(page.text, "html.parser")

        pID = get_object_or_404(models.SearchItem, item_id=item.item_id)

        #for shipping
        shipcontainer = page_soup.findAll("div",{"class":"paddingtop5 paddingbottom5"})
        for container in shipcontainer:
        	infoclasspen = container.div.findAll("div",{"class":"fontsize12"})
        	infoclasssl = container.div.findAll("div",{"class":"info-lt fontsize12"})
        	checker = len(infoclasspen)

        	if checker <= 3:
        		noship = "Free Shipping or Combine Shipping"
        	else:
        		infoshippen = infoclasspen[0].text.strip()
        		infoshipsl = infoclasssl[0].text.strip()
        		infoships = infoclasssl[1].text.strip()

        """ new scrap """ #NEW     
        #for conditions
        conditioncontainer = page_soup.findAll("div",{"class":"inline-block"})
        for container in conditioncontainer:
            itemspec = container.findAll("div",{"class":"fontsize12 pull-left paddingleft15"})
            itemlist = itemspec[2].text #masuk model here
            print(itemlist)

        #for specs or details of product
        speccontainer = page_soup.findAll("table",{"id":"desc-tbl"})
        for container in speccontainer:
            speclist = container.findAll("tr")
            n = 0
            limitloop = len(speclist)
            while n != limitloop:
                speclistfinal = speclist[n].text.strip()
                print(speclistfinal) #masuk model here
                n = n + 1
        """ end of new scrap """

        #for supplier rating
        ratingcontainer = page_soup.findAll("div", {"class": "seller-info-wrap"})
        for container in ratingcontainer:
            count = 0
            inforating = container.findAll("div", {"class": "fontsize12"})
            rateinfo = inforating[1].b.a.text
            item_instance = models.Feedback.objects.create(item_id=pID,
                                                           rating=5,
                                                           comment=inforating)

            count = count + 1
            if count == 5:
                break

        return
