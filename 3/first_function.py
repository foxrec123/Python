
def my_func(value1, value2):
    if value1 > 0 and value2 > 0:
        return value1 + value2
    elif value1 < 0 and value2 < 0:
        return value1 - value2
    elif value1 > 0 and value2 < 0 or value1 < 0 and value2 > 0:
        return 0
    else:
        return None

print(my_func(int(input('Enter value1: ')), int(input('Enter value2: '))))

