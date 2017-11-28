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

        itemspec = page_soup.findAll("ul", {"class": "display-table"})
        for container in itemspec:
            item.detail = container.text.strip()
            print(item.detail)

        rateitem = page_soup.findAll("div", {"class": "product-ranking-star sprites star5"})
        for container in rateitem:
            rateitemval = container.span["content"]
            print("Rate Item:" + rateitemval)
        return
