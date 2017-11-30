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
        shipcontainer = page_soup.findAll("div", {"class":"paddingtop5 paddingbottom5"})
        shipcost = ''
        infoshippen=''
        infoshipsl=''
        infoships=''
        for container in shipcontainer:
            infoclasspen = container.div.findAll("div",{"class":"fontsize12"})
            infoclasssl = container.div.findAll("div",{"class":"info-lt fontsize12"})
            checker = len(infoclasspen)

            if checker <= 3:
                shipcost = "Free Shipping or Combine Shipping"
            else:
                infoshippen = infoclasspen[0].text.strip()
                infoshipsl = infoclasssl[0].text.strip()
                infoships = infoclasssl[1].text.strip()
                shipcost = infoshippen+" "+infoshipsl+" "+infoships

        item.shipping = shipcost

        # for supplier rating
        ratingcontainer = page_soup.findAll("div", {"class": "seller-info-wrap"})
        for container in ratingcontainer:
            inforating = container.findAll("div", {"class": "fontsize12"})
            try:
                item.seller_rate = inforating[1].b.a.text
            except Exception:
                item.seller_rate = 'Not Available'


        #for conditions
        conditioncontainer = page_soup.findAll("div", {"class":"inline-block"})
        for container in conditioncontainer:
            itemspec = container.findAll("div", {"class": "fontsize12 pull-left paddingleft15"})

            try:
                try:
                    try:
                        itemlist = itemspec[2].text
                    except Exception:
                        itemlist = itemspec[1].text
                except Exception:
                    itemlist = itemspec[0].text
            except IndexError:
                itemlist = 'Not available'

            item.condition = itemlist


        #for specs or details of product
        speccontainer = page_soup.findAll("table", {"id":"desc-tbl"})
        for container in speccontainer:
            speclist = container.findAll("tr")
            n = 0
            limitloop = len(speclist)
            while n != limitloop:
                speclistfinal = speclist[n].text.strip()
                item.detail = speclistfinal
                n = n + 1

            item.save()

        #for feedback
        ratingcontainer = page_soup.findAll("div", {"class": "ui-box-body"})
        for container in ratingcontainer:
            count = 0
            #error - no value scraped
            inforating = container.findAll("div", {"class": "fontsize12"})
            try:
                rateinfo = inforating[1].b.a.text
            except IndexError:
                rateinfo = 'No review yet'

            item_instance = models.Feedback.objects.create(item_id=pID,
                                                           rating="5",
                                                           comment=rateinfo)
            item.save()

            count = count + 1
            if count == 5:
                break

        return
