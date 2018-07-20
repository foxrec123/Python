
def my_func(value1, value2, value3):
    my_list = [value1, value2, value3]
    my_list.sort(reverse = True)

    print(my_list[0], my_list[1])

value1 = int(input('Enter value1: '))
value2 = int(input('Enter value2: '))
value3 = int(input('Enter value3: '))

my_func(value1, value2, value3)