#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import time
#from SEN040134 import SEN040134_Tracking as Tracking_Sensor
from SR02 import SR02_Supersonic as Supersonic_Sensor
import rear_wheels
import front_wheels

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        steering = front_wheels.Front_Wheels(db='config')
        steering.center_alignment()
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)
        accelerator = rear_wheels.Rear_Wheels(db='config')
        accelerator.ready()

	#first driving
        accelerator.go_forward(30)
        while True:
            if 0 < distance_detector.get_distance() <= 17:
                break
        accelerator.stop()
        time.sleep(1)
        accelerator.go_backward(30)
        time.sleep(4)
        accelerator.stop()
        time.sleep(1)
        
        #second driving
        accelerator.go_forward(50)
        while True:
            if 0 < distance_detector.get_distance() <= 24:
                break
        accelerator.stop()
        time.sleep(1)
        accelerator.go_backward(50)
        time.sleep(4)
        accelerator.stop()
        time.sleep(1)

        #third driving
        accelerator.go_forward(70)
        while True:
            if 0 < distance_detector.get_distance() <= 33:
                break
        accelerator.stop()    
        time.sleep(1)
        accelerator.go_backward(70)
        time.sleep(4)
        accelerator.stop()
        time.sleep(1)

        accelerator.power_down()

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
