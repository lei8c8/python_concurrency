from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time

def square(item):
    if item == 5:
        time.sleep(5)
    return item * item

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1, timeout=2)
    for sq in it:
        print(sq)

    executor.shutdown()