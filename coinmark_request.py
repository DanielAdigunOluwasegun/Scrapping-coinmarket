import urllib.request
import os 
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")
#request for 3 files with this command
for i in range(3): 
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	#to print time stamp
	print(str(i) + ":" + current_time_stamp)
	#above allows to save using time stamp as indicator 
	#thereby saving a diff file for every request
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html","wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/')
	html = response.read()
	#print(html)
	f.write(html)
	f.close()
	print("requesting coin market cap")
	time.sleep(10)
	#above command means the code will sleep 
	#for 10 seconds 
	# the range shows the periods and the time the frequency
	#eg range 72 and time 3600 means 3 days every hour




