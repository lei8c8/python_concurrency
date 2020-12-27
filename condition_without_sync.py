from threading import Thread
import time

found_prime = False
prime_holder = None
exit_prog = False

def print_thread_func():
    global prime_holder
    global found_prime
    while not exit_prog:
        while not found_prime and not exit_prog:
            time.sleep(0.1)
        if not exit_prog:
            print(prime_holder)
            prime_holder = None
            found_prime = False

def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2 
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True

def finder_thread_func():
    global prime_holder
    global found_prime
    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
        prime_holder = i
        found_prime = True
        while found_prime and not exit_prog:
            time.sleep(0.1)
        i += 1

if __name__ == '__main__':
    printer_thread = Thread(target=print_thread_func)
    printer_thread.start()
    finder_thread = Thread(target=finder_thread_func)
    finder_thread.start()
    time.sleep(3)
    exit_prog = True
    printer_thread.join()
    finder_thread.join()
