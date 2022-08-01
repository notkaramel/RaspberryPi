import RPi.GPIO as GPIO
from time import sleep

pins = [2,3]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def loop():
    while(True):
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            print("pin " + str(pin) + " is on")
            sleep(1)
        print("AND gate must be activated!")
        sleep(3)
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
            print("pin " + str(pin) + " is off")
            sleep(1)
        print("SLEEP FOR 2 SECs")
        sleep(2)
def main():
    setup()
    loop()

main()
GPIO.cleanup()


