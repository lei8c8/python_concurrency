from multiprocessing import Process, RLock, current_process
import multiprocessing
import time

def child_task(rlock):
    for _ in range(0, 5):
        rlock.acquire()
        print("I am child process {0}".format(current_process().name))
        time.sleep(0.1)
    for _ in range(0, 5):
        rlock.release()

if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    rlock = RLock()
    rlock.acquire()

    process1 = Process(target=child_task, args=(rlock,))
    process2 = Process(target=child_task, args=(rlock,))
    process1.start()
    process2.start()

    time.sleep(3)
    rlock.release()

    process1.join()
    process2.join()