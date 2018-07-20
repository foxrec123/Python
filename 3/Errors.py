
number = int(input('Enter number: '))

try:
    if number % 2 == 0:
        raise ValueError()
    if number < 0:
        raise TypeError()
    if number > 10:
        raise IndexError()
except ValueError as some_var:
    print('You have entered even number!')
except TypeError:
    print('You have entered number which is less than zero!')
except IndexError:
    print('You have entered number which is more than 10!')




