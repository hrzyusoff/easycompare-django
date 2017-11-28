from django.http import HttpResponse
from .models import PageCrawl, SearchItem, Feedback
from django.shortcuts import render, get_object_or_404
from .scrap import lazada, lazada2nd
from .scrap import lelong, lelong2nd
from .scrap import elevenstreet, elevenstreet2nd
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
    page = item.page
    page = str(page).strip()
    print(page)

    if page == "11street":
        scrap11street = elevenstreet2nd.estreetScrapEngine()
        scrap11street.scrapIt(item)
    elif page == "Lazada Malaysia":
        scrapLazada = lazada2nd.lazadaScrapEngine()
        scrapLazada.scrapIt(item)
    else:
        scraplelong = lelong2nd.lelongScrapEngine()
        scraplelong.scrapIt(item)

    return render(request, 'page/product_detail.html', {'item': item})


#page for product comparison
def specs(request):
    compare_item = request.POST.getlist("compare")
    item = SearchItem.objects.filter(item_id__in=compare_item)

    for thing in item:
        page = thing.page
        page = str(page).strip()
        item_obj = thing

        if page == '11street':
            #add isEmpty here
            scrap11street = elevenstreet2nd.estreetScrapEngine()
            scrap11street.scrapIt(item_obj)
        elif page == 'Lazada Malaysia':
            scrapLazada = lazada2nd.lazadaScrapEngine()
            scrapLazada.scrapIt(item_obj)
        else:
            scraplelong = lelong2nd.lelongScrapEngine()
            scraplelong.scrapIt(item_obj)

    return render(request, 'page/products_compare.html', {'item1': item})

