import socket
import time
while True:
	time.sleep(0.2)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("62.106.4.2",8888))
	s.send("Elevator ID: 5 | Building: Poland 1 | Current Floor: 4 | Temperature(C): liiian kuuma! tehkaa jotain | Weight(kg): iha hitosti kiloja")
	s.close()
