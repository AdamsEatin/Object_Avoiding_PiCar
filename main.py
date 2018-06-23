import RPi.GPIO as GPIO
import time

#TRIG = 23
#ECHO = 24

def calc_distance(TRIG, ECHO):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    GPIO.cleanup()

    return distance

print("Distance Sensor One: ", calc_distance(23, 24), "cm")
print("Distance Sensor Two: ", calc_distance(17, 27), "cm")