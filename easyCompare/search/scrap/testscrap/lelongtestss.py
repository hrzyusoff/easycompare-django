from bs4 import BeautifulSoup as soup
import requests

# my_url = 'https://www.lelong.com.my/cooler-master-masterliquid-lite-120-aio-cpu-liquid-cooler-am4-ready-netstorecommy-192231419-2018-05-Sale-P.htm'
# my_url = 'https://www.lelong.com.my/apple-iphone-x-64gb-rom-256gb-rom-original-apple-malaysia-set-mobile2go-I5795234-2007-01-Sale-I.htm'
my_url = 'https://www.lelong.com.my/msi-geforce-gtx-1080-ti-lightning-x-1080ti-graphics-card-netstorecommy-198163646-2018-11-Sale-P.htm?list_type=sfi'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(my_url)
page_soup = soup(page.text, "html.parser")

# for shipping
# shipcontainer = page_soup.findAll("div", {"class": "paddingtop5 paddingbottom5"})
# for container in shipcontainer:
#     infoclasspen = container.div.findAll("div", {"class": "fontsize12"})
#     infoclasssl = container.div.findAll("div", {"class": "info-lt fontsize12"})
#     checker = len(infoclasspen)
#
#     if checker <= 3:
#         noship = "Free Shipping or Combine Shipping"
#         print(noship)
#     else:
#         infoshippen = infoclasspen[0].text.strip()
#         infoshipsl = infoclasssl[0].text.strip()
#         infoships = infoclasssl[1].text.strip()
#         print(
#             "Shipping info (PEN. MALAYSIA) : " + infoshippen + "\nShipping info (SABAH/LABUAN) : " + infoshipsl + "\nShipping info (SARAWAK) : " + infoships)

# for supplier rating
# ratingcontainer = page_soup.findAll("div", {"class": "seller-info-wrap"})
# for container in ratingcontainer:
#     inforating = container.findAll("div", {"class": "fontsize12"})
#     print("Seller Rating : " + inforating[1].b.a.text)

# for conditions
# conditioncontainer = page_soup.findAll("div", {"class": "inline-block"})
# for container in conditioncontainer:
#     itemspec = container.findAll("div", {"class": "fontsize12 pull-left paddingleft15"})
#     itemlist = itemspec[2].text
#     print(len(itemlist))

# for specs or details of product
# speccontainer = page_soup.findAll("table", {"id": "desc-tbl"})
# for container in speccontainer:
#     speclist = container.findAll("tr")
#     n = 0
#     limitloop = len(speclist)
#     while n != limitloop:
#         print(speclist[n].text.strip())
#         n = n + 1

#note: no review and rating for each review
