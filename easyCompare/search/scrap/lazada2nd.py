from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
from django.shortcuts import render, get_object_or_404
from search import models


class lazadaScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link

        PID = get_object_or_404(models.SearchItem,
                                item_id=item.item_id)  # driver=webdriver.Chrome("C:/Users/HRZ/Downloads/Compressed/chromedriver/chromedriver.exe")
        chromepath = "C:/Users/HRZ/Downloads/Compressed/chromedriver/chromedriver.exe"
        driver = webdriver.Chrome(chromepath)

        driver.get(my_url)

        page = driver.page_source
        page_soup = soup(page, "lxml")

        hidelist = page_soup.findAll("div", {"class", "c-review__comment"})
        limitloop = len(hidelist)
        commentars = ""
        for hide in hidelist:
            n = 0
            commentar = hide.text.strip()
            commentars = commentars + commentar
            print(commentar)

        item_instance = models.Feedback.objects.create(item=PID,
                                                       rating="5",
                                                       comment=commentars)

        driver.close()
        return
