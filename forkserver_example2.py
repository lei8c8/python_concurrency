from multiprocessing import Process
import multiprocessing
import time


def process_task():
    # block the new process
    time.sleep(1000 * 1000)


if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')

    process = Process(target=process_task)
    process.start()
    print("New process created")
    # block the main process too
    process.join()