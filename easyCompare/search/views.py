from django.http import HttpResponse
from .models import PageCrawl, SearchItem, Feedback
from django.shortcuts import render, get_object_or_404
from .scrap import lazada, lazada2nd
from .scrap import lelong, lelong2nd
from .scrap import elevenstreet
from django.http import Http404


#index page
def home(request):
    Feedback.objects.all().delete()
    SearchItem.objects.all().delete()
    page = PageCrawl.objects.all()
    return render(request, 'page/index.html', {'page': page})


#search main page
def result(request):
    search_input = request.POST.get('userkeyword', None)
    userkeyword = search_input

    # lazada
    lazadaMainURL = 'https://www.lazada.com.my/catalog/?q='
    lconcatURL = lazadaMainURL + userkeyword

    # elevenstreet
    elevenstreetMainURL = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd='
    esconcatURL = elevenstreetMainURL + userkeyword

    # lelong
    lelongMainURL = 'https://www.lelong.com.my/catalog/all/list?TheKeyword='
    llconcatURL = lelongMainURL + userkeyword

    # scrapMudahResult = mudah.mudahScrapEngine()
    # scrapMudahResult.scrapIt(mconcatURL)

    # scraping from each website
    scrapLazadaResult = lazada.lazadaScrapEngine()
    scrapLazadaResult.scrapIt(lconcatURL)
    scrapLelongResult = lelong.lelongScrapEngine()
    scrapLelongResult.scrapIt(llconcatURL)
    scrapElevenstreetResult = elevenstreet.estreetScrapEngine()
    scrapElevenstreetResult.scrapIt(esconcatURL)

    page = PageCrawl.objects.all()
    return render(request, 'page/search_page.html', {'all_page': page})


# page for one product only
def details(request, item_id):
    item = get_object_or_404(SearchItem, item_id=item_id)
    link = item.item_link
    pid = item.item_id

    scrapLazada = lazada2nd.lazadaScrapEngine()
    scrapLazada.scrapIt(link, pid)
    scraplelong = lelong2nd.lelongScrapEngine()
    scraplelong.scrapIt(link, pid)
    return render(request, 'page/product_detail.html', {'item': item})


#page for product comparison
def specs(request):
    compare_item = request.POST.getlist("compare")
    item = SearchItem.objects.filter(item_id__in=compare_item)
    return render(request, 'page/products_compare.html', {'item1': item})

