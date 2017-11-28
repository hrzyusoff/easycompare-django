from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.lazada.com.my/lenovo-thinkpad-carbon-x1-c5-20hqa07fmy-notebook-intel-i7-16gb-512gb-ssd-intel-hd-66325180.html'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)
page_soup = soup(page.text, "html.parser")

detailsdiv = page_soup.findAll("div",{"id","prd-detail-page"})

for rateseller in detailsdiv:
	ratingcontainer = rateseller[0].findAll("li")
	print(rateseller.text.strip())


