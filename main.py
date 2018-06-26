import RPi.GPIO as GPIO
import time

#IN1 : Both Rightside wheels reverse
#IN2 : Both Rightside wheels forward
#IN3 : Both Leftside wheels reverse
#IN4 : Both leftside wheels forward

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


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

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
    GPIO.output(LED1, True)
    GPIO.output(LED2, True)

def LEDs_Off():
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)


def start():
    while True:
        LEDs_On()
        """
        for x in range(5):
            average_distance = 0
            Sensor_One = calc_distance(L_TRIG, L_ECHO)
            #Sensor_Two = calc_distance(R_TRIG, R_ECHO)

            average_distance += Sensor_One
            #average_distance += Sensor_Two
        """
        average_distance = calc_distance(L_TRIG, L_ECHO)
        print("Average Distance: ",average_distance,"cm")

        if average_distance < 5:
            return

        elif average_distance > 5 and average_distance < 25: 
            stop()
            time.sleep(0.2)
            reverse()
            time.sleep(2)

            stop()
            time.sleep(0.2)

            right()
            time.sleep(1.5)
            stop()
            time.sleep(0.2)
            
        else:
            forward()

init()
start()

LEDs_Off()
stop()