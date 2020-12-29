from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def say_hi(item):
    print("\nhi " + str(item) + " executed in thread id " + current_thread().name, flush=True)

if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=10)
    lst = list()
    for i in range(1, 10):
        lst.append(executor.submit(say_hi, "guest" + str(i)))
    
    for future in lst:
        future.result()

    executor.shutdown()