import time
from threading import Lock
from threading import Thread
from threading import current_thread

sharedState = [1, 2, 3]
my_lock = Lock()

def thread1_op():
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().getName()))
    time.sleep(3)
    sharedState[0] = 777
    print("{0} about to release the lock".format(current_thread().getName()))
    my_lock.release()
    print("{0} released the lock".format(current_thread().getName()))

def thread2_op():
    print("{0} is attempting to acquire the lock".format(current_thread().getName()))
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().getName()))
    print(sharedState[0])
    print("{0} about to release the lock".format(current_thread().getName()))
    my_lock.release()
    print("{0} released the lock".format(current_thread().getName()))

if __name__ == '__main__':
    thread1 = Thread(target=thread1_op, name='thread1')
    thread1.start()
    thread2 = Thread(target=thread2_op, name='thread2')
    thread2.start()
    thread1.join()
    thread2.join()

