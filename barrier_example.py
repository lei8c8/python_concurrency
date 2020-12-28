from threading import Barrier
from threading import Thread
import random
import time

def thread_task():
    time.sleep(random.randint(0, 7))
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()

num_threads = 5
barrier = Barrier(num_threads)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i-1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()
