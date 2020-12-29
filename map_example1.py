from multiprocessing import Pool
import os

def square(arg):
    return arg * arg

def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id))

def on_success(new_result):
    print("\nReceived result as: " + str(new_result))

def on_error(err):
    print("Error: " + str(err))

if __name__ == '__main__':
    pool = Pool(
        processes=5,
        initializer=init,
        initargs=(os.getpid(),),
        maxtasksperchild=50
    )
    res = pool.map_async(square,
                        (1,2,3,4,5,6,7,8,9,10),
                        chunksize=2,
                        callback=on_success,
                        error_callback=on_error)
    pool.close()
    pool.join()