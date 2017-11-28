import socket
import time
while True:
	time.sleep(1)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("62.106.4.2",8888))
	s.send("Elevator ID: 2 | Building: Poland 1 | Current Floor: int i = 1 | Temperature: 100")
	s.close()
