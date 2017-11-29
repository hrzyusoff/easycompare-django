from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
from django.shortcuts import render, get_object_or_404
from search import models


class lazadaScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link

        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)
        chromepath = "C:/webdriver/chromedriver.exe"

        driver = webdriver.Chrome(chromepath)

        driver.get(my_url)

        page = driver.page_source
        page_soup = soup(page, "html.parser")
        hidelist = page_soup.findAll("div", {"class", "c-review__comment"})
        limitloop = len(hidelist)

        for hide in hidelist:
            commentar = hide.text.strip()
            if commentar == '':
                commentar = 'No preview given'
            item_instance = models.Feedback.objects.create(item_id=PID,
                                                           rating="5",
                                                           comment=commentar)

        driver.close()
        return
