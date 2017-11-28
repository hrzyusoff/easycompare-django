from bs4 import BeautifulSoup as soup
import requests

#url of site to scrap
# my_url = 'https://www.lazada.com.my/catalog/?q=aorus'
my_url = 'https://www.lazada.com.my/catalog/?q=aorus'
#to act like human that browse from browser
headers = {'User-Agent':'Mozilla/5.0'}
#do requesting to act like human not bot
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")

#main container including header
mainbigcontainer = page_soup.findAll("div",{"class":"catalog__main__content"})
main_url = 'https://www.lazada.com.my'

for container in mainbigcontainer:
	productdiv = container.findAll("div",{"class":"c-product-card__description"})
	pricediv = container.findAll("div",{"class":"c-product-card__price"})
	propicdiv = container.findAll("div",{"class":"c-product-card__img-placeholder"})
	prodattrdiv = container.findAll("ul",{"class":"c-product-card__attributes"})
	limitloop = len(propicdiv)
	n = 0
	while n!= limitloop:
		prodattr = prodattrdiv[n].findAll("li")
		piclist = propicdiv[n].a.span["data-js-component-params"]
		productname = productdiv[n].a.text.strip()
		linkdirect = propicdiv[n].a["href"]
		detail_url = main_url + linkdirect
		pricename = pricediv[n].span.text.strip()
		#r indicate remove, renoving unnecessary element in src
		lcurlyr = piclist.replace("{","")
		rcurlyr = lcurlyr.replace("}","")
		srcr = rcurlyr.replace('"src"',"")
		twodotr = srcr.replace(': "',"")
		allr = twodotr.replace('"',"").strip()

		n = n + 1

		print(n,"\n Product Name : "+productname+"\n","Product price : "+pricename+"\n","Product pic address : "+allr+"\n","Product detail link : "+detail_url+"\n","Item Specs or Detail : ")
		
		# perlu loop sebab perlu iterate setiap li dalam satu ul
		for attrdetail in prodattr:
			print(" -"+attrdetail.text.strip())