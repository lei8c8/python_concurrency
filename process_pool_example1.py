from multiprocessing import Pool
import os

def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id))

def square(x):
    return x * x

if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=1,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=1
    )

    result = pool.apply(square, (3,))
    print(result)