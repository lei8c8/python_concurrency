from multiprocessing import Semaphore, Process, Value
from ctypes import c_bool
import time 
import multiprocessing

def process_A(sem1, sem2, exit):
    while not exit.value:
        print('ping')
        sem1.release()
        sem2.acquire()
        time.sleep(0.05)

def process_B(sem1, sem2, exit):
    while not exit.value:
        sem1.acquire()
        print('pong')
        sem2.release()
        time.sleep(2)

if __name__ == '__main__':
    sem1 = Semaphore(0)
    sem2 = Semaphore(1)
    exit_prog = Value(c_bool, False)
    
    process_a = Process(target=process_A, args=(sem1, sem2, exit_prog))
    process_a.start()

    process_b = Process(target=process_B, args=(sem1, sem2, exit_prog))
    process_b.start()

    time.sleep(3)
    exit_prog.value = True

    process_a.join()
    process_b.join()
    