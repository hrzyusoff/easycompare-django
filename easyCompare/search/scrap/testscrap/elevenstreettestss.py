from bs4 import BeautifulSoup as soup
import requests

# url of site to scrap
my_url = 'http://www.11street.my/productdetail/gigabyte-aorus-gtx1060-6gb-9gbps-gddr5-xtreme-52247327'
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(my_url)
page_soup = soup(page.text, "html.parser")

# item spec
itemspec = page_soup.findAll("ul", {"class": "display-table"})
for container in itemspec:
    print("Specs:" + container.text.strip())

# item rate
rateitem = page_soup.findAll("div", {"class": "product-ranking-star sprites star5"})
for container in rateitem:
    rateitemval = container.span["content"]
    print("Rate Item:" + rateitemval)
