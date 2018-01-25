import time
import threading
from threading import Thread, Event
import random
from termcolor import colored

# http://www.cnblogs.com/ArtsCrafts/archive/2013/04/24/Python.html

class VehicleThread(Thread):
    """Class representing a motor vehicle at an intersection"""

    def __init__(self, threadName, event):
        Thread.__init__(self, name=threadName)
        # ensures that each vehicle waits for a green light
        self.threadEvent = event

    def run(self):
        """Vehicle waits unless/until light is green"""
        # stagger arrival times
        time.sleep(random.randrange(1, 10))

        # prints arrival time of car at intersection
        print("%s arrived at %s" % \
              (self.getName(), time.ctime(time.time())) )

        # wait for green light
        self.threadEvent.wait()

        # displays time that car departs intersection
        print( "%s passes through intersection at %s" % \
              (self.getName(), time.ctime(time.time())) )


def main():
    greenLight = Event()
    vehicleThreads = []
    
    # creates and starts ten Vehicle threads
    for i in range(1, 11):
        vehicleThreads.append(VehicleThread("Vehicle" + str(i),
                                            greenLight))
    
    for vehicle in vehicleThreads:
        vehicle.start()
    
    while threading.activeCount() > 1:
        # sets the Event's flag to false -- block all incoming vehicles
        greenLight.clear()
        print(colored("RED LIGHT! at", "red"), time.ctime(time.time()) )
        time.sleep(3)
    
        # sets the Event's flag to true -- awaken all waiting vehicles
        print(colored("GREEN LIGHT! at", "green"), time.ctime(time.time()) )
        greenLight.set()
        time.sleep(1)

if __name__ == '__main__':
    main()