import socket, sys, logging

class color:
	BGBLUE = "\x1b[44m"
	BGMAG = "\x1b[45m"
	BGCYAN = "\x1b[46m"
	BGLGRAY = "\x1b[100m"
	BGLYELLOW = "\x1b[103m"
	BGLBLUE = "\x1b[104m"
	BGLMAG = "\x1b[105m"
	BGLCYAN = "\x1b[106m"
	BGYELLOW = "\x1b[43m"
	BGWHITE = "\x1b[47m"
	FGBLACK = "\x1b[30m"
	FGYELLOW = "\x1b[33m"
	FGBLUE = "\x1b[34m"
	FGMAG ="\x1b[35m"
	FGCYAN = "\x1b[36m"
	FGWHITE = "\x1b[37m"
	FGLBLUE = "\x1b[94m"
	OKGREEN = "\x1b[32m"
	FAIL = "\x1b[41m"
	WARNING = "\x1b[31m"
	END = "\x1b[0m"
	OK = "\x1b[6;30;42m"

def server():
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.bind(("192.168.2.20", 8888))
		sock.listen(5)
		print ("Server start\n" + color.OK + "OK!" + color.END +  color.WARNING + "\nNo active connections" + color.END)
		return sock
	except Exception, e:
		print color.FAIL + "Server failed to start!" + color.END
		logger.error(e)

def parse_data(msg):
	try:
        	data = msg.split(" | ")
        	for d in data:
                	temp1, temp2 = d.split(": ", 1)
			color_data(temp1,temp2)

	except Exception, e:
		print color.FAIL + "Error logged in hissi.log" + color.END
		logger.error(color.FAIL+msg+color.END)
		pass


def color_data(header,value):
	try:
		value = int(value)
	except:
		value = value

	if header=="Elevator ID":
		if value <= 8:
			statuslist.insert(1, id_build(value))

	elif header == "Building":
		if value == "Russia 1" or value == "Russia 2" or value == "Sweden 1" or value == "Sweden 2" or value == "Poland 1" or value == "Poland 2" or value == "Finland 1" or value == "Finland 2":
			statuslist.insert(3, id_build(value))

	elif header == "Current Floor":
		if value <= 6 and value > 0:
			statuslist.insert(5, good_values(value))
		else:
			statuslist.insert(5, log_error(value))
	elif header == "Temperature(C)":
		if value <= 25 and value > 14:
			statuslist.insert(7, good_values(value))
		else:
			statuslist.insert(7, log_error(value))

	elif header == "Weight(kg)":
		if value <= 499 and value >= 0:
			statuslist.insert(9, good_values(value))
		else:
			statuslist.insert(9, log_error(value))

def id_build(value):
	id_dict = {
		"Dynamo": 1,
		"Nordea": 2,
		"Poland": 3,
		"Sweden": 4,
		"Russia": 5,
		"Finland": 6
	}

        if value == 1 or value == "Russia 1":
                return color.BGBLUE + color.FGWHITE + str(value) + color.END
        elif value == 2 or value == "Russia 2":
                return color.BGMAG + color.FGBLACK + str(value) + color.END
        elif value == 3 or value == "Sweden 1":
                return color.BGCYAN + color.FGBLACK+ str(value) + color.END
        elif value == 4 or value == "Sweden 2":
                return color.BGWHITE+ color.FGBLACK + str(value) + color.END
        elif value == 5 or value == "Poland 1":
                return color.BGYELLOW+ color.FGBLACK + str(value) + color.END
        elif value == 6 or value == "Poland 2":
                return color.BGLYELLOW+ color.FGBLACK + str(value) + color.END
	elif value == 7 or value == "Finland 1":
                return color.BGLBLUE+ color.FGWHITE + str(value) + color.END
        elif value == 8 or value == "Finland 2":
                return color.BGLCYAN+ color.FGBLACK + str(value) + color.END



def log_error(value):
	return color.FAIL + str(value) + color.END

def good_values(value):
	return color.OKGREEN + str(value) + color.END


logging.basicConfig(filename="/home/lubuntu/hissi.log" , level=logging.DEBUG,format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger=logging.getLogger(__name__)

sock=server()

while True:
	statuslist = ["Elevator ID:","Building:", "Current Floor:", "Temperature(C):","Weight(kg):"]
	client, add = sock.accept()
	a,b =add
	parse_data(client.recv(1024))
	try:
		if color.FAIL in statuslist[3] or color.FAIL in statuslist[5] or color.FAIL in statuslist[7]:
			logger.error("IP: "+a+"; " + " ".join(statuslist))
	except:
		pass
	print "IP: "+a+ "; " +" ".join(statuslist)
	client.close()
