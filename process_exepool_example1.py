from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from multiprocessing import current_process
from threading import current_thread

import os

def say_hi(item):
    print("\nhi " + str(item) + " executed in thread id " + current_thread().name + 
          " in process id " + str(os.getpid()) + " with name " + current_process().name, flush=True)

if __name__ == '__main__':
    print("Main process id " + str(os.getpid()))
    multiprocessing.set_start_method('fork')
    executor = ProcessPoolExecutor(max_workers=10)
    lst = list()
    for i in range(1, 10):
        lst.append(executor.submit(say_hi, "guest" + str(i)))

    for future in lst:
        future.result()

    executor.shutdown()