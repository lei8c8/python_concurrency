from multiprocessing import Process
from multiprocessing import Pipe
import time

def child_process(conn):
    for i in range(10):
        conn.send("hello" + str(i + 1))
    conn.close()

if __name__ == "__main__":
    pare_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn))
    p.start()

    for _ in range(10):
        msg = pare_conn.recv()
        print(msg)

    pare_conn.close()