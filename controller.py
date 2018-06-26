import RPi.GPIO as GPIO
import time

# controller.py is used as a seperate space for all interactions with the GPIO Pins

#IN1 : Both Rightside wheels reverse
#IN2 : Both Rightside wheels forward
#IN3 : Both Leftside wheels reverse
#IN4 : Both leftside wheels forward

F_TRIG = 19
F_ECHO = 26
    
IN1 = 18
IN2 = 17
IN3 = 27
IN4 = 22

L_LED1 = 6
L_LED2 = 13
R_LED1 = 20 
R_LED2 = 21

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Setting up Pins
    GPIO.setup(L_LED1, GPIO.OUT)
    GPIO.setup(L_LED2, GPIO.OUT)
    GPIO.setup(R_LED1, GPIO.OUT)
    GPIO.setup(R_LED2, GPIO.OUT)

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def calc_front_distance():  
    GPIO.setup(F_TRIG, GPIO.OUT)
    GPIO.setup(F_ECHO, GPIO.IN)

    GPIO.output(F_TRIG, False)
    time.sleep(0.1)

    GPIO.output(F_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(F_TRIG, False)

    while GPIO.input(F_ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(F_ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def forward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def reverse():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def LEDs_On():
    GPIO.output(L_LED1, True)
    GPIO.output(L_LED2, True)
    GPIO.output(R_LED1, True)
    GPIO.output(R_LED2, True)

def LEDs_Off():
    GPIO.output(L_LED1, False)
    GPIO.output(L_LED2, False)
    GPIO.output(R_LED1, False)
    GPIO.output(R_LED2, False )
