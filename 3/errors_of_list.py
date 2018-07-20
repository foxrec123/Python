
my_list = ['World', 1, True, 5, 6]



try:
    index = input('Enter index, please: ')
    if int(index) > len(my_list) - 1 or int(index) < - len(my_list):
        raise IndexError('Index is out of range!')
    print(my_list[int(index)])
except IndexError:
    print('Index is out of range!')
except ValueError:
    print('Index has an apropriate type!')
