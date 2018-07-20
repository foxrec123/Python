import pygame
import random
import math
from pynput import keyboard

#checking possibility of game
def checking_list(my_list):
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

    return (k_final + pos_of_X) % 2 == 0

def generate_field(my_list):
    field = []
    sublist = []
    size_of_sublist = 0

    for item in my_list:
        sublist.append(item)
        size_of_sublist += 1
        if size_of_sublist == 4:
            field.append(sublist)
            sublist = []
            size_of_sublist = 0
    return field

#funtion for drawing field
def draw_game_field():
    for row in field:
        print(row)
    print('\n')

#function for searching X
def get_index_of_X():
    for item in field:
        if item.__contains__('X'):
            return (field.index(item), item.index('X'))

#fucntion for exchange
def exchange(row, col, index):
    if row >= 0 and row <= 3 and col >= 0 and col <= 3:
        item_from_there           = field[row][col]
        field[row][col]           = 'X'
        field[index[0]][index[1]] = item_from_there
    else:
        print('You are trying to go out of field!')

#function for changing position
def change_position(index, direction):
    if direction == 'w':
        exchange(index[0] - 1, index[1], index)
    if direction == 'a':
        exchange(index[0], index[1] - 1, index)
    if direction == 's':
        exchange(index[0] + 1, index[1], index)
    if direction == 'd':
        exchange(index[0], index[1] + 1, index)

#function for checking the end of the game

#function for pressing keys
def on_press(key):
    #global counter_of_steps
    keys = ('w', 'a', 's', 'd')
    if keys.__contains__(key.char):
        index = get_index_of_X()
        change_position(index, key.char)
        #counter_of_steps += 1
        if field == end_of_the_game:
            print('You win!')
            print('Steps made: ', counter_of_steps)
            exit(0)
        draw_game_field()

#************   body of the main program  *******************************************
pygame.init()

counter_of_steps = 0  # type: int

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'X', 15]

while True:
    random.shuffle(my_list)
    if checking_list(my_list):
        break

field = generate_field(my_list)
end_of_the_game = generate_field([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'X'])

draw_game_field()

#Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
