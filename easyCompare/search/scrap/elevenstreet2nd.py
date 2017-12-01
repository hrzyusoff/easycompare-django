from bs4 import BeautifulSoup as soup
from django.shortcuts import render, get_object_or_404
from search import models
import requests


class estreetScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link

        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(my_url)
        page_soup = soup(page.text, "html.parser")

        #condition
        try:
            cond = page_soup.find("li", {"class": "product-status"})
            item.condition = cond.text
        except Exception as error:
            item.condition = 'Not available'

        item.save()

        # # seller rating - selenium
        # sellerContainer = page_soup.findAll("section", {"class": "aside-section-detail-seller-info"})
        # seller = page_soup.findAll("dl", {"class": "product-detail-seller"})
        # #item.rating = seller[0].dd.em.text

        #product detail
        try:
            info = ''
            prodspeccontainer = page_soup.findAll("div", {"class": "product-detail-info-block"})
            n = 0
            for container in prodspeccontainer:
                tag = container.findAll("p")
                length = len(tag)
                while n != length:
                    spec = tag[n].text.strip()
                    info = info + str(spec) + " \n"
                    n = n + 1

            item.detail = info
            item.save()
        except Exception:
            item.detail = 'No detail provided by seller of this product'
            item.save()


        return
