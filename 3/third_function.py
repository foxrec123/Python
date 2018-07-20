
def my_func(list_of_numbers, flag):
    my_list = []
    if flag:
        for item in list_of_numbers:
            if item % 2 != 0:
                my_list.append(item)
    else:
        for item in list_of_numbers:
            if item % 2 == 0:
                my_list.append(item)
    print(my_list)

my_func([1,2,5,8,4,6,9,8,4,6,9,4], False)