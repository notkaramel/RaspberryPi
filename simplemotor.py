import RPi.GPIO as GPIO

motor = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)


p = GPIO.PWM(motor, 50)

p.start(2.5)
