import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
ON = GPIO.HIGH
OFF = GPIO.LOW

segment_pin = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6, 
        'G': 7, 
        'DP':8
        }

number_presets = {
        1 : [    'B','C'],
        2 : ['A','B',    'D','E',    'G'],
        3 : ['A','B','C','D',        'G'],
        4 : [    'B','C',        'F','G'],
        5 : ['A',    'C','D',    'F','G'],
        6 : ['A',    'C','D','E','F','G'],
        7 : ['A','B','C'],
        8 : ['A','B','C','D','E','F','G'],
        9 : ['A','B','C','D',    'F','G'],
        0 : ['A','B','C','D','E','F']
        }

def setup():
    for pin in segment_pin.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, OFF)

def turnon(segment_choice):
    pin = segment_pin[segment_choice]
    GPIO.output(pin, ON)
    print("pin " + str(pin) + " is set to ON!")
    print("segment " + segment_choice + " is on!")

def turnoff(segment_choice):
    GPIO.output(segment_pin[segment_choice], OFF)
    print("segment " + segment_choice + " is off!")

def turnALLoff():
    print("turning off all pins!")
    for pin in segment_pin.values():
        GPIO.output(pin, OFF)

def displayNumber(number):
    turnALLoff()
    for segment in number_presets[number]:
        turnon(segment)

def loop():
    while(True):
        choice = int(input("What number do you want to be displayed?:"))
        if choice in number_presets.keys():
            displayNumber(choice)
        else:
            print("NOPE!")

def main():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        turnALLoff()
        GPIO.cleanup()




