import RPi.GPIO as GPIO
import time

import controller as CTRL


def start():
    while True:
        CTRL.LED_all_on()

        curr_distance = CTRL.front_distance()
        print(curr_distance,"cm")

        if curr_distance < 8:
            return

        elif curr_distance > 8 and curr_distance < 20: 
            CTRL.LED_all_on()
            """
            CTRL.motor_stop()
            time.sleep(0.2)
            CTRL.motor_reverse()
            time.sleep(2)

            CTRL.motor_stop()
            time.sleep(0.2)

            CTRL.motor_right()
            time.sleep(2.0)
            CTRL.motor_stop()
            time.sleep(0.2)
            """
        else:
            CTRL.motor_forward()
            CTRL.LED_all_off()

CTRL.init()
start()

CTRL.LED_all_off()
CTRL.motor_stop()