#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        count = 0
        while True:
            record = self.car.line_detector.read_digital()
            self.car.accelerator.go_forward(70)
            if 0 < self.car.distance_detector.get_distance() <= 30:
                count += 1
                self.car.steering.turn(60)
                self.car.accelerator.go_forward(60)
                time.sleep(0.6)
                while True:
                    record = self.car.line_detector.read_digital()
                    if record == [0,0,0,0,0]:
                        self.car.steering.turn(90)
                        self.car.accelerator.go_forward(60)
                    else: 
                        break
                while True:
                    record = self.car.line_detector.read_digital()
                    if record != [0,0,0,0,0]:
                        self.car.steering.turn(125)
                        self.car.accelerator.go_forward(60)
                        time.sleep(1.3)
                        break
                while True:
                    record = self.car.line_detector.read_digital()
                    if record == [0,0,0,0,0]:
                        self.car.steering.turn(90)
                        self.car.accelerator.go_forward(60)
                    else: 
                        break
            
            elif record == [0,0,0,0,0]:
                self.car.steering.turn(125)
                self.car.accelerator.go_backward(45)
                time.sleep(0.5)
                self.car.steering.turn(60)
                self.car.accelerator.go_forward(45)
                time.sleep(0.2)
            elif record == [1,0,0,0,0]:
                self.car.steering.turn(60)
                time.sleep(0.03)
            elif record == [0,1,0,0,0]:
                self.car.steering.turn(75)
                time.sleep(0.03)
            elif record == [0,0,1,0,0]:
                self.car.steering.turn(90)
                time.sleep(0.03)
            elif record == [0,0,0,1,0]:
                self.car.steering.turn(105)
                time.sleep(0.03)
            elif record == [0,0,0,0,1]:
                self.car.steering.turn(120)
                time.sleep(0.03)
            elif record == [1,1,0,0,0]:
                self.car.steering.turn(60)
                time.sleep(0.03)
            elif record == [0,1,1,0,0]:
                self.car.steering.turn(75)
                time.sleep(0.03)
            elif record == [0,0,1,1,0]:
                self.car.steering.turn(105)
                time.sleep(0.03)
            elif record == [0,0,0,1,1]:
                self.car.steering.turn(120)
                time.sleep(0.03)
            elif record == [1, 1, 1, 1, 1]:
                self.car.steering.turn(90)
                if count == 4:
                    break
            elif record == [1, 1, 1, 0, 0]:
                self.car.steering.turn(75)
                time.sleep(0.03)
            elif record == [0, 1, 1, 1, 0]:
                self.car.steering.turn(90)
                time.sleep(0.03)
            elif record == [0, 0, 1, 1, 1]:
                self.car.steering.turn(105)
                time.sleep(0.03)
            elif record == [1, 1, 0, 0, 1]:
                self.car.steering.turn(60)
                time.sleep(0.03)
            elif record == [1, 0, 0, 1, 1]:
                self.car.steering.turn(120)
                time.sleep(0.03)
                
            else:
                time.sleep(0.03)
        self.car.accelerator.stop()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()