import RPi.GPIO as GPIO
import time

#TRIG = 23
#ECHO = 24

def calc_distance(TRIG, ECHO):  
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(0.2)

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
    return distance

while True:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

    Sensor_One = calc_distance(23, 24)
    Sensor_Two = calc_distance(17, 27)

    if Sensor_One <= 9.00 or Sensor_Two <= 9.00:
        GPIO.output(20, True)
        GPIO.output(21, True)
    else:
        GPIO.output(20, False)
        GPIO.output(21, False)

    print("Distance Sensor One: ", calc_distance(23, 24), "cm")
    print("Distance Sensor Two: ", calc_distance(17, 27), "cm")