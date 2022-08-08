from setup_3461BS import setup, terminate
from counter_3461BS import display
from threading import Thread

number = 1234

def foreground():
    global number
    number = int(input("Enter a number: "))

def background():
    global number
    display(number, duration=1)

def main():
    setup()
    
    try:
        fg = Thread(target=foreground).start()
        bg = Thread(target=background).start()
    except KeyboardInterrupt:
        terminate()

main()
    

