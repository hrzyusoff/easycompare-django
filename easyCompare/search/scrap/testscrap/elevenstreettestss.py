from bs4 import BeautifulSoup as soup
import requests

my_url = "http://www.11street.my/productdetail/apple-iphone-6-32gb-gold-official-malaysia-apple-1-50627677#product-detail-info"

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(my_url)
page_soup = soup(page.text, "html.parser")

# seller rating
# sellerContainer = page_soup.findAll("section", {"class": "aside-section-detail-seller-info"})

seller = page_soup.find("div", {"class": "aside-section-content"})
# for container in seller:
# rating = seller[0].dd.em.text
print(seller)

#item rate 
# rateitem = page_soup.findAll("div",{"class":"product-ranking-star sprites star5"})
# for container in rateitem:
# 	rateitemval = container.span["content"]
# 	print("Rate Item:"+rateitemval)


info = ''
prodspeccontainer = page_soup.findAll("div", {"class": "product-detail-info-block"})
n = 0
for container in prodspeccontainer:
    tag = container.findAll("p")
    length = len(tag)
    print(length)
    while n != length:
        spec = tag[n].text.strip()
        info = info + str(spec)
        n = n+1

print(info)