from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
from django.shortcuts import render, get_object_or_404
from search import models


class lazadaScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link
        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)

        webdriverpath = "C:/webdriver/phantomjs.exe"
        driver = webdriver.PhantomJS(webdriverpath)
        driver.get(my_url)

        page = driver.page_source
        page_soup = soup(page, "html.parser")

        #shipping
        try:
            shipinfo = page_soup.find("div", {"class": "c-delivery-option__price"})
            item.shipping = shipinfo.text
        except Exception:
            item.shipping = "No shipping info"

        #seller rating
        try:
            seller = page_soup.find("div", {"class", "c-positive-seller-ratings c-positive-seller-ratings_state_high"})
            seller = seller.text
            item.seller_rate = str(seller).replace(" ", "").strip()
            item.seller_rate = item.seller_rate.replace('"', "") + "%"
            item.save()
        except Exception:
            item.seller_rate = 'No Seller rating'
            item.save()

        # for rate of item in their respective page
        try:
            rateprodval = page_soup.find("div", {"class", "c-rating-total__text-rating-average"})
            item.rating = str(rateprodval.em.text) + "/5"
        except Exception:
            item.rating = "No rating"

        # for comment of item in their respective page
        commentdiv = page_soup.findAll("div", {"class", "c-review__comment"})
        count = 0
        for container in commentdiv:
            commentlist = container.text.strip()
            if commentlist == '':
                commentlist = 'No review given'
            item_instance = models.Feedback.objects.create(item_id=PID,
                                                           comment=commentlist)
            count = count + 1
            if count == 5:
                break

        driver.close()
        return
