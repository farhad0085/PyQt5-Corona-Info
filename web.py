import requests
from bs4 import BeautifulSoup

def get_stats(countryName):
	countryStats = []
	URL = 'https://www.worldometers.info/coronavirus/'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	#my_table = soup.find(id='main_table_countries_today')

	table_body=soup.find('tbody')
	rows = table_body.find_all('tr')
	for row in rows:
		cols=row.find_all('td')
		cols=[x.text.strip() for x in cols]
		if cols[0] == countryName:
			i = 0
			while i<8: # because we only need first 8 column
				if cols[i] == "":
					countryStats.append("0")
				else:
					countryStats.append(cols[i])
				i += 1

	return countryStats