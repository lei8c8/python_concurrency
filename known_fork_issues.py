from threading import Lock
from multiprocessing import Process
import time
import multiprocessing

lock = Lock()

def process_task():
    lock.acquire()
    print("I am child process")
    lock.release()

if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    process = Process(target=process_task)

    lock.acquire()
    process.start()
    lock.release()

    print("Parent process waiting for child process to finish")
    process.join()
    print('Done')