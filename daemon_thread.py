from threading import Thread
from threading import current_thread
import time

def deamon_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)

if __name__ == '__main__':
    t = Thread(target=deamon_thread_task, name="daemonThread", daemon=True)
    t.start()

    time.sleep(3)
    print("Main thread exiting and Python program too")