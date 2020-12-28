import multiprocessing
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Semaphore

def child_process(q, sem1, sem2):
    var = q.get()
    print("child process received var = {0} with id {1} from queue".format(str(var), id(var)))
    sem2.release()
    sem1.acquire()

    print("after changes by parent process var = {0}".format(str(var)), flush=True)

if __name__ == '__main__':
    q = Queue()
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print("this machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = 1
    print("Parent process puts item on queue with id " + str(id(var)))
    q.put(var)

    process = Process(target=child_process, args=(q, sem1, sem2))
    process.start()

    sem2.acquire()
    var += 2
    print("parent process changed the enqueued item to " + str(var), flush=True)
    sem1.release()
    process.join()
