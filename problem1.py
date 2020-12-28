from threading import current_thread
from threading import Thread

def thread_task():
    print("{0} executing".format(current_thread().getName()))


myThread = Thread(group=None,  # reserved
                  target=thread_task,
                  name="childThread")

myThread.start()
myThread.join()