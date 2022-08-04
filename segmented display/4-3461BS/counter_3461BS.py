from time import sleep
import RPi.GPIO as gpio
from setup_3461BS import setup, digit_show, digit_pins


def display(number):
    t = 1/270
    hold = 1
    time = 0.0
    while (number < 10000 and number >= 0):
        while time < hold:
            digit_show(digit_pins()[0], int(number/1000))
            sleep(t)
            digit_show(digit_pins()[1], int((number%1000)/100))
            sleep(t)
            digit_show(digit_pins()[2], int((number%100)/10))
            sleep(t)
            digit_show(digit_pins()[3], number%10)
            sleep(t)
            time+=0.25
        number += 1
        time = 0.0


def main():
    setup()
    try:
        while True:
            display(0)
    except KeyboardInterrupt:
        print("\nProgram stopped")


main()
gpio.cleanup()
