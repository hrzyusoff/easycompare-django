from django.contrib import admin
from .models import PageCrawl, SearchItem, Feedback

admin.site.register(PageCrawl)
admin.site.register(SearchItem)
admin.site.register(Feedback)
