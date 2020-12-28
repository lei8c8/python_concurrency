from multiprocessing import Process, Semaphore, Value
import multiprocessing


def child_process(sem1 , sem2, var):
    print("Child process received var = {0} with id {1} from queue".format(str(var.value), id(var)), flush=True)
    sem2.release()
    sem1.acquire()

    print("After changes by parent process var = {0}".format(var.value), flush=True)


if __name__ == '__main__':
    # multiprocessing.set_start_method('spawn')
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)    
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = Value('I', 1)
    print("Parent process puts item on queue with id " + str(id(var)))

    process = Process(target=child_process, args=(sem1, sem2, var))
    process.start()

    sem2.acquire()

    # change the var
    var.value += 2
    print("Parent process changed the enqueued item to " + str(var.value), flush=True)
    sem1.release()
    process.join()