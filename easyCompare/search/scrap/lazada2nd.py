from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
from django.shortcuts import render, get_object_or_404
from search import models


class lazadaScrapEngine:
    def scrapIt(self, item):
        my_url = item.item_link
<<<<<<< HEAD

        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)
        chromepath = "C:/Users/HRZ/Downloads/Compressed/chromedriver/chromedriver.exe"
=======
        PID = get_object_or_404(models.SearchItem, item_id=item.item_id)
        chromepath = "C:/webdriver/chromedriver.exe"
>>>>>>> 009e4486f67d8dce6f3366ce548697682ec537a5
        driver = webdriver.Chrome(chromepath)

        driver.get(my_url)

        page = driver.page_source
        page_soup = soup(page, "html.parser")
        hidelist = page_soup.findAll("div", {"class", "c-review__comment"})
        limitloop = len(hidelist)
<<<<<<< HEAD
        commentars = ""
        # print("Natang")
        for hide in hidelist:
            print("Natang")
            n = 0
            commentar = hide.text.strip()
            commentars = commentars + commentar
            print(commentar)

        item_instance = models.Feedback.objects.create(item=PID,
                                                       rating="5",
                                                       comment="Natang brekmok")

=======
        for hide in hidelist:
            commentar = hide.text.strip()
            item_instance = models.Feedback.objects.create(item_id=PID,
                                                           rating="5",
                                                           comment=commentar)
>>>>>>> 009e4486f67d8dce6f3366ce548697682ec537a5
        driver.close()
        return
