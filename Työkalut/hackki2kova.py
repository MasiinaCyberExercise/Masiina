import socket
import time
while True:
	#time.sleep(1)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("62.106.4.2",8888))
	s.send("Elevator ID: 1 | Building: Russia 1 | Current Floor: 2 | Temperature(C): 15000 | Weight(kg): 1466")
	s.close()
