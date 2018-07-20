import random

#funtion for drawing field
def draw_game_field(field):
    for row in field:
        print(row)
    print('\n')

#function describing my step
def my_step(field):
    while True:
        col = int(input('Enter column '))
        row = int(input('Enter row '))
        if field[row - 1][col - 1] == ' ':
            field[row - 1][col - 1] = 'X'
            break
        else:
            print('Wrong step! Try again')
            #draw_game_field(field)
    draw_game_field(field)
#function describing computer's step
def computer_step(field):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col] == ' ':
            field[row][col] = 'O'
            break
    draw_game_field(field)

#check the end of the game
def is_game_finished(field):
    stop_game = False

    # rows
    for i in range(0, 3):
        if field[i][0] == 'X' and field[i][1] == 'X' and field[i][2] == 'X':
            print('You win!')
            return True

    # rows
    for i in range(0, 3):
        if field[i][0] == 'O' and field[i][1] == 'O' and field[i][2] == 'O':
            print('Computer wins!')
            return True

    # columns
    for i in range(0, 3):
        if field[0][i] == 'X' and field[1][i] == 'X' and field[2][i] == 'X':
            print('You win!')
            return True

    # columns
    for i in range(0, 3):
        if field[0][i] == 'O' and field[1][i] == 'O' and field[2][i] == 'O':
            print('Computer wins!')
            return True

    #first cross
    if field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':
        print('You win!')
        return True

    # first cross
    if field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O':
        print('Computer wins!')
        return True

    # second cross
    if field[2][0] == 'X' and field[1][1] == 'X' and field[0][2] == 'X':
        print('You win!')
        return True

    # second cross
    if field[2][0] == 'O' and field[1][1] == 'O' and field[0][2] == 'O':
        print('Computer wins!')
        return True

    draw = True
    for x in range(0, 3):
        for y in range(0, 3):
            if field[x][y] == ' ':
                draw = False
                break

    if draw:
        print('This is draw!')
        return True

    return False

def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """

    field = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    draw_game_field(field)

    while True:
        my_step(field)
        if is_game_finished(field):
            break
        computer_step(field)
        if is_game_finished(field):
            break

    print('Game is over!')

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()