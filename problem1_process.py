import multiprocessing
from multiprocessing import *

def child_task(str_obj):
    print(str_obj.__hash__())

if __name__ == '__main__':
    str_obj = "Educative!"
    multiprocessing.set_start_method('fork')
    print(str_obj.__hash__())

    process1 = Process(target=child_task, args=(str_obj,))
    process1.start()

    process2 = Process(target=child_task, args=(str_obj,))
    process2.start()

    process1.join()
    process2.join()