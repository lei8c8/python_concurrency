from threading import RLock
from threading import Thread

def perform_unlock():
    rlock.release()
    print("child task executing")
    rlock.release()
    
rlock = RLock()
rlock.acquire()

thread = Thread(target=perform_unlock)
thread.start()
thread.join()