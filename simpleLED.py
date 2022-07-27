import RPi.GPIO as GPIO
from time import sleep

led_list = [2,1]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in led_list:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

GPIO.cleanup()
