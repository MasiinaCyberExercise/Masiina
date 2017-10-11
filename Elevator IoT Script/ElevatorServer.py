import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost",8888))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print client.recv(1024)
    client.close()
