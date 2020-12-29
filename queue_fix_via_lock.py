import multiprocessing
import sys
import random
import time
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import current_process
from multiprocessing import Lock

def child_process(q, lock):
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False
        lock.release()
        time.sleep(0.001)

    print("child process {0} processed {1} items for the queue".format(current_process().name, count), flush=True)

if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')
    print("this machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    lock = Lock()
    q = Queue()

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))
    
    p1 = Process(target=child_process, args=(q, lock))
    p2 = Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()