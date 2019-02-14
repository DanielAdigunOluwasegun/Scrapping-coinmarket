import urllib.request
import os 
if not os.path.exists("html_files"):
	os.mkdir("html_files")




response = urllib.request.urlopen('https://coinmarketcap.com/')
html = response.read()
print(html)
print("requesting coin market cap")

f = open("html_files/coinmarketcap.html","wb")
f.write(html)
f.close()

