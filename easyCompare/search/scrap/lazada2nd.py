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

        # for rate of item in their respective page
        rateproddiv = page_soup.find("div", {"class", "c-rating-total__text-rating-average"})
        rateprodval = rateproddiv.em.text


        # for comment of item in their respective page
        commentdiv = page_soup.findAll("div", {"class", "c-review__comment"})
        limitloop = len(commentdiv)
        for container in commentdiv:
            commentlist = container.text.strip()
            if commentlist == '':
                commentlist = 'No preview given'
            item_instance = models.Feedback.objects.create(item_id=PID,
                                                           rating=rateprodval,
                                                           comment=commentlist)

        driver.close()
        return
