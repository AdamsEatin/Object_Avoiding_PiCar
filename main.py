import RPi.GPIO as GPIO
import time

#IN1 : Both Rightside wheels reverse
#IN2 : Both Rightside wheels forward
#IN3 : Both Leftside wheels reverse
#IN4 : Both leftside wheels forward

def init(LED1, LED2, IN1, IN2, IN3, IN4):
    GPIO.setmode(GPIO.BCM)
    # Setting up Pins
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def calc_distance(TRIG, ECHO):  
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(0.1)

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

"""
while True:
    L_TRIG = 6
    L_ECHO = 13
    R_TRIG = 20
    R_ECHO = 21
    
    LED1 = 19
    LED2 = 26

    IN1 = 18
    IN2 = 17
    IN3 = 27
    IN4 = 22

    init(LED1, LED2, IN1, IN2, IN3, IN4)

    GPIO.output(IN1, True)
    time.sleep(3)
    GPIO.output(IN1, False)

    
    #TODO : Rename to represent Front Left/Right, Back Left/Right Sensors
    Sensor_One = calc_distance(L_TRIG, L_ECHO)
    Sensor_Two = calc_distance(R_TRIG, R_ECHO)

    
    if Sensor_One <= 9.00 or Sensor_Two <= 9.00:
        GPIO.output(LED1, True)
        GPIO.output(LED2, True)

    else:
        GPIO.output(LED1, False)
        GPIO.output(LED2, False)

    print("Distance Sensor One: ", Sensor_One, "cm")
    print("Distance Sensor Two: ", Sensor_Two, "cm")
"""
L_TRIG = 6
L_ECHO = 13
R_TRIG = 20
R_ECHO = 21
    
IN1 = 18
IN2 = 17
IN3 = 27
IN4 = 22

LED1 = 19
LED2 = 26

init(LED1, LED2, IN1, IN2, IN3, IN4)

timeout = time.time() + 30

while True:
    
    if time.time() > timeout:
        break
    
    Sensor_One = calc_distance(L_TRIG, L_ECHO)
    Sensor_Two = calc_distance(R_TRIG, R_ECHO)
    
    if(Sensor_One > 9.00 and Sensor_Two > 9.00):
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, True)
    else:
        while(Sensor_One <= 9.00 and Sensor_Two <= 9.00):
            GPIO.output(IN1, True)
            GPIO.output(IN2, False)
            GPIO.output(IN3, False)
            GPIO.output(IN4, True)