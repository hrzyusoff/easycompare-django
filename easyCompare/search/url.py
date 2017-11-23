from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.result, name='result'),

    url(r'^(?P<item_id>[0-9]+)/$', views.details, name='spec'),

    url('^compare$', views.specs, name='specs'),

#url(r'^(?P<page_id>[0-9]+)/$', views.details, name='details'),
#url(r'^(?P<URLstrip>[-+\w+\d+]+)/$', views.details, name='spec'),
#url(r'^(?P<URLstrip>[^~,]+)/$', views.details, name='spec'),

]
