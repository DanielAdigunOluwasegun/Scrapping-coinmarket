import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 


#pandas to write into a csv file
#glob is used to arrange stuffs

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r", encoding="utf-8")
	#f = open("html_files/coinmarketcap20190212161834.html","r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	currencies_table = soup.find("table", {"id": "currencies"})
	currencies_tbody = currencies_table.find("tbody")
	#currency_rows = currencies_tbody.find("tr", {"td": "id-bitcoin"})
	currency_rows = currencies_tbody.find_all("tr")
	#allows you get for all currencies
	for r in currency_rows:
		#currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class": "curreny-symbol"}).find("a").text
	    currency_name = r.find("td", {"class": "currency-name"})["data-sort"]
	    currency_market_cap = r.find("td", {"class": "market-cap"})["data-sort"]
	    currency_price = r.find("a", {"class": "price"}).text
	    currency_volume = r.find("a", {"class": "volume"}).text
	    currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
	    currency_change = r.find("td", {"class": "percent-change"})['data-sort']
	    #print(scrapping_time)
	    #print(currency_short_name)
	    #print(currency_name)
	    #print(currency_market_cap)
	    #print(currency_price)
	    #print(currency_volume)
	    #print(currency_supply)
	    #print(currency_change)

	    df = df.append({
	    	'scrapping_time': scrapping_time,
	    	# 'short_name': currency_short_name,
	    	'name': currency_name,
	    	'market_cap': currency_market_cap,
	    	'price': currency_price,
	    	'volume': currency_volume,
	    	'supply': currency_volume,
	    	'24H_change': currency_change
	    	}, ignore_index=True)
#print(df)
df.to_csv("parsed_results/coinmarketcap_dataset.csv")
