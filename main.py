import RPi.GPIO as GPIO
import time

import controller as CTRL


def start():
    while True:
        CTRL.LEDs_On()

        curr_distance = CTRL.calc_front_distance()
        print(curr_distance,"cm")

        if curr_distance < 5:
            return

        elif curr_distance > 5 and curr_distance < 20: 
            CTRL.stop()
            time.sleep(0.2)
            CTRL.reverse()
            time.sleep(2)

            CTRL.stop()
            time.sleep(0.2)

            CTRL.right()
            time.sleep(1.5)
            CTRL.stop()
            time.sleep(0.2)
            
        else:
            CTRL.forward()

CTRL.init()
start()

CTRL.LEDs_Off()
CTRL.stop()