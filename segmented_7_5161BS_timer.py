from RPi.GPIO import cleanup
from segmented_7_5161BS import setup, displayNumber, turnALLoff
from time import sleep
def main():
    setup()
    try:
        while(True):
            for i in range(10):
                displayNumber(i)
                sleep(1)
    except KeyboardInterrupt:
        turnALLoff()
        cleanup()

main()
