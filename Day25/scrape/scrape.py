import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_"
location = "San+Francisco,+CA"
page = 0
file_path = "yelp-{loc}.txt".format(loc = location)



while page < 41:
	url = base_url + "loc=" + location + "&start=" + str(page)
	yelp_r = requests.get(url)
	yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")
	# print(yelp_soup.prettify())
	bussiness = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
	with open (file_path, "a") as txtfile:
		for biz in bussiness:
			title = biz.findAll('a', {'class': 'biz-name'})[0].text	
			address_first_line = ""
			address_second_line = ""

			try:
				address = biz.findAll('address')[0].contents
				address_first_line = address[0].strip(" \n\t\r")
				address_second_line = address[2].strip(" \n\t\r")			
				# print(address_first_line)
				# print(address_second_line)
			except:
				pass

			try:
				phone_number = biz.findAll('span', {'class': 'biz-phone'})[0].text.strip(" \n\t\r")
			except:
				phone_number = None

			content = "{title}\n{address_first_line}\n{address_second_line}\n{phone}\n\n".format(
					title = title,
					address_first_line = address_first_line,
					address_second_line = address_second_line,
					phone = phone_number
				)
			txtfile.write(content)	
	
	page += 20

