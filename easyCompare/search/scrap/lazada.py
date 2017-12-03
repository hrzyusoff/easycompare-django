from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render, get_object_or_404
from search import models


class lazadaScrapEngine:
    def scrapIt(self, lconcatURL):
        # url of site to scrap
        my_url = lconcatURL
        # to act like human that browse from browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        # do requesting to act like human not bot
        page = requests.get(my_url)

        # html parsing
        page_soup = soup(page.text, "html.parser")

        # main container including header
        mainbigcontainer = page_soup.findAll("div", {"class": "catalog__main__content"})

        page = get_object_or_404(models.PageCrawl, pk=6)

        for container in mainbigcontainer:
            n = 0
            count = 0
            productdiv = container.findAll("div", {"class": "c-product-card__description"})
            pricediv = container.findAll("div", {"class": "c-product-card__price"})
            propicdiv = container.findAll("div", {"class": "c-product-card__img-placeholder"})
            itemsddiv = container.findAll("ul", {"class": "c-product-card__attributes"})  # sd refer to spec and detail
            limitloop = len(productdiv)
            while n != limitloop:
                productnamelist = productdiv[n].a.text.strip()
                pricetaglist = pricediv[n].span.text.strip()
                piclist = propicdiv[n].a.span["data-js-component-params"]
                directlink = propicdiv[n].a["href"]
                itemsdli = itemsddiv[n].findAll("li")
                item_detail = " "
                for container1 in itemsdli:
                    specdetail = container1.text.strip()
                    item_detail = item_detail + specdetail

                detail_url = 'https://www.lazada.com.my' + directlink
                lcurlyr = piclist.replace("{", "")
                rcurlyr = lcurlyr.replace("}", "")
                srcr = rcurlyr.replace('"src"', "")
                twodotr = srcr.replace(': "', "")
                allr = twodotr.replace('"', "").strip()
                item_instance = models.SearchItem.objects.create(page=page,
                                                                 price=pricetaglist,
                                                                 title=productnamelist,
                                                                 pic=allr,
                                                                 rating='',
                                                                 detail=item_detail,
                                                                 item_link=detail_url,
                                                                 condition='-',
                                                                 seller_rate='',
                                                                 shipping='')
                n = n + 1
                count = count + 1
                if count == 5:
                    break


        return

