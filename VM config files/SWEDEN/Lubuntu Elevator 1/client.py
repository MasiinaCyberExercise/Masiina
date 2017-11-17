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
        return "Elevator ID: " + str(self.ID) + " | " + "Building: " + self.buildingname + " | " + "Current Floor: " + str(self.floor) + " | " + "Temperature(C): " + str(self.temperature) + " | " + "Weight(kg): " + str(self.weight)

elevator = Elevator(3,"Sweden 1",1,20,70)
while (True):
    elevator.senddata("62.106.4.2",8888,elevator.toString())
    time.sleep(random.randint(2,7))
    elevator.randomize()

