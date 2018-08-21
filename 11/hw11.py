from time import time, sleep
from contextlib import contextmanager


#1. Redefining False on True
class Lock(object):
    def __init__(self):
        self.lock = False

#a) with class
class Redefine(object):
    def __init__(self, Lock_int):
        Lock_int.lock = True
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


#b) with class
@contextmanager
def redefine_cont(lock_int):
    lock_int.lock = True
    yield lock_int


#2. Exceptions
@contextmanager
def no_exceptions():
    try:
        yield
    except Exception as ex:
        print('Expeption {} happened'.format(ex))

#3. Time counter
#a) with class
class TimeCounter():
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
    def __enter__(self):
        self.start_time = time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        print('Time of execution (class): {}'.format(self.end_time - self.start_time))

#b) with contextmanager
@contextmanager
def time_counter_cont():
    start_time = time()
    yield
    end_time = time()
    print('Time of execution (cont): {}'.format(end_time - start_time))

if __name__ == '__main__':
    #1
    lock_int = Lock()
    print(lock_int.lock)

    with redefine_cont(lock_int) as r:
        print(lock_int.lock)

    #2.
    with no_exceptions():
        1 / 0

    #3.
    with TimeCounter():
        sleep(5)
    with time_counter_cont():
        sleep(8)








