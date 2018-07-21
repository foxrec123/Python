from datetime import datetime

quantity = []

def cancelling_of_func(func):
    def inner(end_number):
        print('{} is cancelled!'.format(func.__name__))
    return inner

def measure_speed(func):
    def inner(end_number):
        time_1 = datetime.now()
        func(end_number)
        time_2 = datetime.now()

        speed = time_2 - time_1
        print('Speed of execution is {}'.format(speed))
    return inner

def calc_calls(func):
    def inner(end_number):
        func(end_number)
        quantity.append('call')
        print('current calls quantity is {}'.format(len(quantity)))
    return inner

def logger(func):
    def inner(end_number):
        print('Decorator is created!')
        print('Started execution of function...')
        func(end_number)
        print('Finished execution of function.')
    return inner

def catch_exeption(func):
    def inner(end_number):
        try:
            func(end_number)
        except Exception as ex:
            print('Error is {}'.format(ex.__class__.__name__))
    return inner

@catch_exeption
def trial(end_number):

    """
    :param end_number:
    :return: sum of numbers from 0 to end_number
    """

    total = 0
    for i in range(0, end_number + 1):
        total += i
    print('Sum is ' + str(total))
    #f = 1/0



trial(10)


