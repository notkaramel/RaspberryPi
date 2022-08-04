import RPi.GPIO as GPIO
from time import sleep
def digit_pins():
    return [17,10,5]

def segment_pins():
    return {
        'A': 14,
        'B': 15,
        'C': 18,
        'D': 23,
        'E': 24,
        'F': 25,
        'G': 8,
        'DP': 7
    }

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in segment_pins().values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in digit_pins():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def numbers():
    return {
        0 : ['A','B','C','D','E','F'],
        1 : [    'B','C'],
        2 : ['A','B',    'D','E',    'G'],
        3 : ['A','B','C','D',        'G'],
        4 : [    'B','C',        'F','G'],
        5 : ['A',    'C','D',    'F','G'],
        6 : ['A',    'C','D','E','F','G'],
        7 : ['A','B','C'],
        8 : ['A','B','C','D','E','F','G'],
        9 : ['A','B','C','D',    'F','G']
        }

def turnon(segment):
    GPIO.output(segment, GPIO.HIGH)

def turnoff(segment):
    GPIO.output(segment, GPIO.LOW)

def turnAllOff():
    for segment in segment_pins().values():
        turnoff(segment)

def show_number(number):
    turnAllOff()
    if number in numbers().keys():
        for segment in numbers()[number]:
            turnon(segment_pins()[segment])
    else:
        print("Invalid number")

def digit_show(digit, number):
    show_number(number)   
    for pin in digit_pins():
        if pin == digit:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

def loop():
    try:
        setup() 
        for digit in digit_pins():
            for i in range(0,10):
                digit_show(digit, i)
                sleep(1)
            sleep(1) 
        turnAllOff()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nProgram stopped by user.")
        exit()

print("\nPlease check wiring.md for wiring details!\n")
# loop()
