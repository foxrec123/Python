
number = int(input('Enter number: '))

try:
    if number % 2 == 0:
        raise ValueError()
    if number < 0:
        raise TypeError()
    if number > 10:
        raise IndexError()
except Exception as some_var:
    if some_var == ValueError():
        print('You have entered even number!')
    if some_var == TypeError():
        print('You have entered number which is less than zero!')
    if some_var == IndexError():
        print('You have entered number which is more than 10!')




