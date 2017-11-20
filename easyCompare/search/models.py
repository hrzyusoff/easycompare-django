from django.db import models


class PageCrawl(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_url = models.CharField(max_length=250)
    info = models.CharField(max_length=200)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.info


class SearchItem(models.Model):
    page = models.ForeignKey(PageCrawl,on_delete=models.CASCADE) #lazada, shoppe, mudah.my
    price = models.CharField(max_length=200)
    title = models.CharField(max_length=200) #title of the ads
    pic = models.CharField(max_length=250)  #link of the pic provided by seller
    rating = models.IntegerField(default=0)
    detail = models.CharField(max_length=500)
    item_link = models.CharField(max_length=250)
    condition = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    URLstrip = models.CharField(max_length=250)

    def __str__(self):
        return self.title