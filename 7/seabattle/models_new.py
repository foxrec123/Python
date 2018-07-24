from Constants import *

#Models

class Ship:
    def __init__(self, size):
        self.size = size
        self.place = []

    @staticmethod
    def handle_direction_input():
            """
            Handles user input. List of accepted moves:
                'w' - up,
                's' - down,
                'a' - left,
                'd' - right
            :return: <str> current move.
            """
            while True:
                direction = input('Enter direction of your ship (use "w", "a", "s", "d"): ')
                if direction in MOVES.keys():
                    return direction

    def parse_and_set_place(self, field):
        while True:
            try:
                place = input('Enter coords of the first deck without spaces (example: A1, C7): ')
                row = matching_letters[place[0].upper()]
                col = int(place[1:len(place)]) - 1

                self.place.append(col * 10 + row)
                field[self.place[0]] = DECK
            except:
                print('Incorrect input!')
            else:
                break


        while True:
            direction = self.handle_direction_input()
            counter = self.place[0]
            temp_counters = []
            try:
                for i in range(0, self.size - 1):
                    counter += MOVES[direction]
                    if counter < 0:
                        raise Exception
                    temp_counters.append(counter)
            except:
                print('Incorrect direction!')
            else:
                break
        for i in temp_counters:
            field[i] = DECK
        self.place.append(counter)
        field.print_field()

class Field(list):
    """
    Management of game
    """

    def __init__(self):
        for i in range(0, 100):
            self.append(' ')

    def print_field(self):
        def get_space(i):
            index = str(int(i / 10 + 1))
            if len(index) == 1:
                index += ' '
            return index

        print('     A', '   B', '   C', '   D', '   E', '   F', '   G', \
                '   H', '   I', '   J')
        for i in range(0, 100, 10):
            print(get_space(i), self[i:i + 10])
            print('-----------------------------------------------------')
        print('\n')


class Player:
    def __init__(self, name, field):
        self.name = name
        self.turn = False
        self.field = field
        print('{} has been joined to the game! '.format(name))
        print('Please, put your ships on the field: ')
        field.print_field()

    def fill_the_field(self, field):
        Ship_1 = Ship(4)
        print('You need to put 4-decker ship... ')
        Ship_1.parse_and_set_place(field)

        #self.field = field
        #field.print_field()




