import random

#random
def random_gen():
    while True:
        yield random.randint(0, 100)

#like range
def like_range(first, second, step):
    while first < second:
        yield first
        first += step

#like_map
def like_map(func, some_list):
    for item in some_list:
        yield func(item)

#like enumerate
def like_enumerate(some_list):
    index = 1
    for item in some_list:
        yield index, item
        index += 1

#like_zip
def like_zip(*args):
    pass

#gen_inst = random_gen()
#gen_inst = like_range(1, 100, 10)
#gen_inst = like_map(lambda x: len(x), ['fuck', 'off', 'bastards'])
#gen_inst = like_enumerate(['fuck', 'off', 'bastards'])

i = iter(gen_inst)

for _ in range(0, 3):
    print(next(i))

zip()