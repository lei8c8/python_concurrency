from multiprocessing import Process
import multiprocessing
import os

def process_task():
    file_desc.write("\nline written by child process with id {0}".format(os.getpid()))
    file_desc.flush()

if __name__ == "__main__":
    file_desc = open("sample.txt", "w")
    file_desc.write("\nline written by parent process with id {0}".format(os.getpid()))
    file_desc.flush()

    multiprocessing.set_start_method('fork')
    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    file_desc = open("sample.txt", "r")
    print(file_desc.read())
    os.remove("sample.txt")