# SBx4HC08 IC Chip

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

signal_pins = [2,3,4,5,9,10,12,13]

for pin in signal_pins:
    GPIO.setup(pin, GPIO.OUT)

def pinon(pin):
    GPIO.output(pin, GPIO.HIGH)
    print("pin " + str(pin) + " is on")

def pinoff(pin):
    GPIO.output(pin, GPIO.LOW)
    print("pin " + str(pin) + " is off")

for pin in signal_pins:
    pinon(pin)
    sleep(0.5)

for pin in signal_pins:
    pinoff(pin)
    sleep(0.5)

GPIO.cleanup()
