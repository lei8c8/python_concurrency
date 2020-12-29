from multiprocessing import Pool
import os
import time

def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id))

def square(x):
    return x * x

def on_success(result):
    print("result is " + str(result))

def on_error(err):
    print("error is " + str(err))

if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=1,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=2
    )

    result = pool.apply_async(square, (9,), callback=on_success, error_callback=on_error)
    time.sleep(6)