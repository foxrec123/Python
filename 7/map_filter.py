from functools import reduce

#1.При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
print(list(map(lambda x: x % 5, [1, 4, 5, 30, 99])))

#При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
print(list(map(lambda x: str(x), [3, 4, 90, -2])))

#При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
print(list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str])))

#При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']

def calc(x, y):
    if isinstance(x, str):
        return len(x) + len(y)
    else:
        return x + len(y)

print(reduce(calc, ['some', 'other', 'value']))



