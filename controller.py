import RPi.GPIO as GPIO
import time

# controller.py is used as a seperate space for all interactions with the GPIO Pins

#IN1 : Both Rightside wheels reverse
#IN2 : Both Rightside wheels forward
#IN3 : Both Leftside wheels reverse
#IN4 : Both leftside wheels forward

F_R_TRIG = 20
F_R_ECHO = 21
F_L_TRIG = 19
F_L_ECHO = 26
F_LED1 = 6
F_LED2 = 13

B_R_TRIG = 0
B_R_ECHO = 0
B_L_TRIG = 0
B_L_ECHO = 0
B_LED1 = 0
B_LED2 = 0

IN1 = 18
IN2 = 17
IN3 = 27
IN4 = 22


# Setup Pins for later use
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Setting up Front Board
    GPIO.setup(F_R_TRIG, GPIO.OUT)
    GPIO.setup(F_R_ECHO, GPIO.IN)
    GPIO.setup(F_L_TRIG, GPIO.OUT)
    GPIO.setup(F_L_ECHO, GPIO.IN)
    GPIO.setup(F_LED1, GPIO.OUT)
    GPIO.setup(F_LED2, GPIO.OUT)

    # Setting up Back Board
    GPIO.setup(B_R_TRIG, GPIO.OUT)
    GPIO.setup(B_R_ECHO, GPIO.IN)
    GPIO.setup(B_L_TRIG, GPIO.OUT)
    GPIO.setup(B_L_ECHO, GPIO.IN)
    GPIO.setup(B_LED1, GPIO.OUT)
    GPIO.setup(B_LED2, GPIO.OUT)

    # Setting up Motor Controls
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


# Distance Sensor related functions
def calc_distance(TRIG, ECHO):
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

def front_distance():
    left_dist = calc_distance(F_L_TRIG, F_L_ECHO)
    right_dist = calc_distance(F_R_TRIG, F_R_ECHO)
    average_dist = (left_dist + right_dist) / 2
    return average_dist

def back_distance():
    left_dist = calc_distance(B_L_TRIG, B_L_ECHO)
    right_dist = calc_distance(B_R_TRIG, B_R_ECHO)
    average_dist = (left_dist + right_dist) / 2
    return average_dist


# Motor Control functions
def motor_stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def motor_forward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def motor_reverse():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def motor_left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def motor_right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)


# LED Related Functions
def LED_all_on():
    GPIO.output(F_LED1, True)
    GPIO.output(F_LED2, True)
    GPIO.output(B_LED1, True)
    GPIO.output(B_LED2, True)

def LED_all_off():
    GPIO.output(F_LED1, False)
    GPIO.output(F_LED2, False)
    GPIO.output(B_LED1, False)
    GPIO.output(B_LED2, False)

def LED_front_on():
    GPIO.output(F_LED1, True)
    GPIO.output(F_LED2, True)

def LED_front_off():
    GPIO.output(F_LED1, False)
    GPIO.output(F_LED2, False)

def LED_back_on():
    GPIO.output(B_LED1, True)
    GPIO.output(B_LED2, True)

def LED_back_off():
    GPIO.output(B_LED1, False)
    GPIO.output(B_LED2, False)