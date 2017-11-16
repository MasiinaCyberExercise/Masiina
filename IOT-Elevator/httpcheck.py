import urllib2

import time
class color:
	OKGREEN = "\x1b[32m"
	FAIL = "\x1b[31m"
	END = "\x1b[0m"




url = "http://www.masiina.com"
while True:
	time.sleep(3)
	start = time.time()
	try:
		nf = urllib2.urlopen(url, timeout = 3)
		page = nf.read()
		nf.close()
		stop = time.time()
		aika = stop - start
		print color.OKGREEN + "Server check succesfull, response time: " + color.END
		print aika
	except Exception as e:
		print color.FAIL + "SERVER TIMEOUT!" + color.END
		print e
