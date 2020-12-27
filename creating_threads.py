from threading import Thread
from threading import current_thread

def thread_task(a, b, c, key1, key2):
    print("{0} received the arguments: {1} {2} {3} {4} {5}".format(current_thread().getName(), a, b, c, key1, key2))

if __name__ == '__main__':
    my_thread = Thread(
        group = None,
        target = thread_task,
        name = 'daemonThread',
        args = (1, 2, 3),
        kwargs = {'key1': 777, 'key2': 111},
        daemon = None
    )
    my_thread.start()
    my_thread.join()