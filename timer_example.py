from threading import current_thread
from threading import Timer
import time

def say_hi(name):
    print("{0} says hi {1}!".format(current_thread().getName(), name))

if __name__ == '__main__':
    timer = Timer(10, say_hi, args=["reader"])
    timer.start()

    time.sleep(2)
    timer.join()
    print("{0} exiting...".format(current_thread().getName()))