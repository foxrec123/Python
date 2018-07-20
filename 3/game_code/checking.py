import random
import math

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'X']
random.shuffle(my_list)

k_final = 0
k = 0
pos_of_X = 0

for x in range(0, 16):
    if my_list[x] == 'X':
        pos_of_X = math.ceil((x + 1) / 4)
        continue
    if x == 15:
        break
    k_final += k
    k = 0
    for y in range(x + 1, 16):
        if my_list[y] != 'X' and my_list[x] > my_list[y]:
             k += 1

final = k_final + pos_of_X

if final % 2 == 0:
    print('Ok')
else:
    print('Never!')

