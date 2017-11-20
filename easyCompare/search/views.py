from django.http import HttpResponse
from .models import PageCrawl, SearchItem
from django.shortcuts import render,get_object_or_404
from .scrap import lazada
from .scrap import lelong
from .scrap import mudah
from .scrap import elevenstreet
# from .scrap import carousell
from django.http import Http404


#index page
def home(request):
    page = PageCrawl.objects.all()
    return render(request,'page/index.html',{'page':page,})


#search main page
def result(request):
    search_input = request.POST.get('userkeyword', None)
    SearchItem.objects.all().delete()
    userkeyword = search_input

    # lazada
    lazadaMainURL = 'https://www.lazada.com.my/catalog/?q='
    lconcatURL = lazadaMainURL + userkeyword
    # lazadaMainURL = 'http://www.lazada.com.my/'
    # lazadaLastURL = '/?itemperpage=60&sc=MS0F&searchredirect='
    # lconcatURL = lazadaMainURL + userkeyword + lazadaLastURL + userkeyword

    # mudah
    mudahMainURL = 'https://www.mudah.my/malaysia/'
    mudahMiddleURL = '-for-sale'
    mudahfLastURL = '?lst=0&fs=1&w=3&cg=0&q='
    mudahsLastURL = '&so=1&st=s'
    mconcatURL = mudahMainURL + userkeyword + mudahMiddleURL + mudahfLastURL + userkeyword + mudahsLastURL

    # elevenstreet
    elevenstreetMainURL = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd='
    esconcatURL = elevenstreetMainURL + userkeyword

    # lelong
    lelongMainURL = 'https://www.lelong.com.my/catalog/all/list?TheKeyword='
    llconcatURL = lelongMainURL + userkeyword

    #carousell
    # carousellMainURL = 'https://carousell.com/search/products/?query='
    # cconcatURL = carousellMainURL + userkeyword

    #scraping from each website
    scrapMudahResult = mudah.mudahScrapEngine()
    scrapMudahResult.scrapIt(mconcatURL)
    scrapLazadaResult = lazada.lazadaScrapEngine()
    scrapLazadaResult.scrapIt(lconcatURL)
    scrapLelongResult = lelong.lelongScrapEngine()
    scrapLelongResult.scrapIt(llconcatURL)
    scrapElevenstreetResult = elevenstreet.estreetScrapEngine()
    scrapElevenstreetResult.scrapIt(esconcatURL)
    # scrapCarousellResult = carousell.carousellScrapEngine()
    # scrapCarousellResult.scrapIt(cconcatURL)

    page = PageCrawl.objects.all()
    return render(request, 'page/search_page.html', {'all_page': page})


#page for product comparison
def specs(request):
    compare_item = request.POST.get('compare')
    print(compare_item)
    item = get_object_or_404(SearchItem, compare_item)
    return render(request, 'page/products_compare.html', {'item': item})


# page for one product only
def details(request, URLstrip):
    item = get_object_or_404(SearchItem, URLstrip=URLstrip)
    return render(request, 'page/product_detail.html', {'item': item })

#Http404 example - replace with getObjectOr404
    #try:
    #    webpage = PageCrawl.objects.get(page_id=page_id)
    #except PageCrawl.DoesNotExist:
    #    raise Http404('This page does not exists')

#dynamic page example - replace with template.render
# print(all_page)
#    html = ''
#    for pageCrawl in all_page:
#        url = '/search/'+str(pageCrawl.page_id)+'/'
#        html += '<a href ="' + url + '"> '+str(pageCrawl.info)+' </a> <br> '
#    return HttpResponse(html)
