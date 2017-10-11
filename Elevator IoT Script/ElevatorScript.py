import random
import time
import socket

class Elevator():
    
    def __init__(self,ID,buildingname,floor,temperature,weight):
        self.ID = ID
        self.buildingname = buildingname
        self.floor = floor
        self.temperature = temperature
        self.weight = weight

    def changefloor(self, newfloor):
        self.floor = newfloor

    def changeweight(self, newweight):
        self.weight = newweight

    def changetemperature(self, newtemp):
        self.temperature = newtemp

    def randomize(self):
        self.floor = random.randint(1,6)
        self.weight = random.randint(0,500)
        self.temperature = random.randint(15,25)

    def senddata(self,address,port,data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address,port))
        sock.send(data)
        sock.close()
        
    def toString(self):
        return "Elevator ID: " + str(self.ID) + " | " + "Building: " + self.buildingname + " | " + "Current Floor: " + str(self.floor) + " | " + "Temperature: " + str(self.temperature) + " Celsius" + " | " + "Weight: " + str(self.weight) + " kg"

elevator = Elevator(1,"Dynamo",1,19,140)
while (True):
    elevator.senddata("localhost",8888,elevator.toString())
    time.sleep(60)
    elevator.randomize()
