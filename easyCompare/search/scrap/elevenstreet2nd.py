from bs4 import BeautifulSoup as soup
from selenium import webdriver
from django.shortcuts import render, get_object_or_404
from search import models
import requests


class estreetScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link
        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)
        # headers = {'User-Agent': 'Mozilla/5.0'}
        # page = requests.get(my_url)
        # page_soup = soup(page.text, "html.parser")

        #url
        # webdriverpath = "D:/FYP/phantomjs-2.1.1-windows/bin/phantomjs.exe"
        #url yeh
        webdriverpath = "C:/webdriver/phantomjs.exe"
        driver = webdriver.PhantomJS(webdriverpath)
        driver.get(my_url)

        page = driver.page_source
        page_soup = soup(page, "html.parser")

        # seller rate
        try:
            sellerate = page_soup.find("dl", {"class", "product-detail-seller"})
            item.seller_rate = sellerate.em.text.strip()
        except Exception:
            item.seller_rate = "Not available"

        # ship info
        try:
            shipinfo = page_soup.find("dl", {"class", "detail-shipping-price-list"})
            item.shipping = shipinfo.text.strip()
        except Exception:
            item.shipping = "Free Shipping"

        # condition
        try:
            cond = page_soup.find("li", {"class": "product-status"})
            item.condition = cond.text
        except Exception as error:
            item.condition = 'Not available'

        item.save()

<<<<<<< HEAD
        commentlist = page_soup.findAll("p", {"class", "echo-item-description"})
        for eachcomment in commentlist:
            try:
                comment = eachcomment.text.strip().replace("Read more", "")
                # print(comment)
                item_instance = models.Feedback.objects.create(item_id=PID, comment=comment)
            except Exception as error:
                print(error)

=======
>>>>>>> 227ca167b668764b496ccf9c9e57301da3b414ab
        # product detail
        try:
            info = ''
            prodspeccontainer = page_soup.findAll("div", {"class": "product-detail-info-block"})
            n = 0
            for container in prodspeccontainer:
                tag = container.findAll(["p","li"])
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
