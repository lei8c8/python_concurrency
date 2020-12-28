import multiprocessing
from multiprocessing import Process

class Test:
    value = 777

def process_task():
    print(Test.value)

if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    Test.value = 999
    process = Process(target=process_task, name="process-1")
    process.start()
    process.join()