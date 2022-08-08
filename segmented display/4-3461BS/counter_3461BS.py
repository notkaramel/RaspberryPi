from time import sleep
import RPi.GPIO as gpio
from setup_3461BS import setup, digit_show, digit_pins


def display(number, delay = 1/240, duration = 1):
    time = 0
    while time < duration:
        digit_show(digit_pins()[0], int(number/1000))
        sleep(delay)
        digit_show(digit_pins()[1], int((number%1000)/100))
        sleep(delay)
        digit_show(digit_pins()[2], int((number%100)/10))
        sleep(delay)
        digit_show(digit_pins()[3], number%10)
        sleep(delay)

        time += delay

def counter(start=0, end=9999, duration=1, delay = 1/240):
    start_num = start
    end_num = end
    custom_gap = duration
    custom_delay = delay
    for current in range(start_num,end_num):
        display(number=current, 
            delay=custom_delay, 
            duration=custom_gap)


def main():
    setup()
    try:
        while True:
            counter(284)
    except KeyboardInterrupt:
        print("\nProgram stopped")


# main()
# gpio.cleanup()
