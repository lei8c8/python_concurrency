import threading

class MyTask(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name='subclassThread', args=(2,3))

    def run(self):
        print("{0} is executing".format(threading.current_thread().getName()))

if __name__ == '__main__':
    my_task = MyTask()
    my_task.start()
    my_task.join()
    print("{0} exiting...".format(threading.current_thread().getName()))