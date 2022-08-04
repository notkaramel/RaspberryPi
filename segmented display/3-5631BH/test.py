from threading import Thread
from time import sleep
import RPi.GPIO as gpio
from setup_5631BH import setup, digit_show

def display(number):
    t = 0.01
    while (number < 1000 and number >= 0):    
        digit_show(2, int(number/100))
        sleep(t)
        digit_show(3, int(number/10)%10)
        sleep(t)
        digit_show(4, number%10)
        sleep(t)
        number += 1

def getinput():
    return int(input("Enter a number: "))

def main():
    setup()
    try:
        number = getinput()
        b = Thread(name="display", target=display(number))
        b.start()
        print("Thread started")
    except KeyboardInterrupt:
        gpio.cleanup()
        print("\nProgram stopped by user")
        exit()

main()

