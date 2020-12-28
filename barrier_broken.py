from threading import Barrier
from threading import Thread
import time

def thread_task():
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()
    print("Barrier broken")


num_threads = 5
barrier = Barrier(num_threads + 1)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()

time.sleep(3)

print("Main thread about to invoke abort on barrier")
barrier.abort()
