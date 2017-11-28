import urllib2
import time
import sys 

host = sys.argv[1]
while True:
	time.sleep(2)
	try:
		request = urllib2.urlopen(host,timeout=2)
		print "OK"
	except Exception as e:
		print "ERROR"
		print e
