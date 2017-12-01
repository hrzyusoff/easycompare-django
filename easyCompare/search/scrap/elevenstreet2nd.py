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

        prodspeccontainer = page_soup.findAll("ul", {"class": "display-table"})
        for container in prodspeccontainer:
            item.detail = container.text.strip()
            print(item.detail)
            item.save()

        return
