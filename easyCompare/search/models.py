from django.db import models


class PageCrawl(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_url = models.CharField(max_length=250)
    info = models.CharField(max_length=200)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.info


class SearchItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(PageCrawl, on_delete=models.CASCADE) #lazada, shoppe, mudah.my
    price = models.CharField(max_length=200)
    title = models.CharField(max_length=200) #title of the ads
    pic = models.CharField(max_length=250)  #link of the pic provided by seller
    rating = models.CharField(max_length=10)
    detail = models.CharField(max_length=2000)
    item_link = models.CharField(max_length=250)
    condition = models.CharField(max_length=20)
    seller_rate = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    item_id = models.ForeignKey(SearchItem, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment