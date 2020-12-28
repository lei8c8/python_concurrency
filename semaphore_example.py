from threading import Thread
from threading import Semaphore
import time

sem_find = Semaphore(0)
sem_print = Semaphore(0)
primeHolder = None
exitProg = False

def print_thread():
    global primeHolder

    while not exitProg:
        sem_find.acquire()
        print(primeHolder)
        primeHolder = None
        sem_print.release()

def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True

def finder_thread():
    global primeHolder
    i = 1
    while not exitProg:
        while not is_prime(i):
            i += 1
            time.sleep(0.01)
        primeHolder = i
        sem_find.release()
        sem_print.acquire()
        i += 1

printerThread = Thread(target=print_thread)
printerThread.start()

finderThread = Thread(target=finder_thread)
finderThread.start()

# Let the threads run for 3 seconds
time.sleep(3)

exitProg = True

printerThread.join()
finderThread.join()