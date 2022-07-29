# works on HC04 IC Chip - Hex inverters

import RPi.GPIO as GPIO
from time import sleep

ON = GPIO.HIGH
OFF = GPIO.LOW

GPIO.setmode(GPIO.BCM)
pin_list = [1,3,5,9,11,13]

def setup():
    for pin in pin_list:
        GPIO.setup(pin, GPIO.OUT)

def turnon(delay):
    for pin in pin_list:
        GPIO.output(pin, ON)
        print("pin " + str(pin) + " is on!")
        sleep(delay)

def turnoff(delay):
    for pin in pin_list:
        GPIO.output(pin, OFF)
        print("pin " + str(pin) + " is off!!")
        sleep(delay)

def main():
    setup()
    try:
        while(True):
            turnon(0.7)
            turnoff(0.7)
    except KeyboardInterrupt:
        GPIO.cleanup()

main()


