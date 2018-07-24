from models_new import *

def main():
    field = Field()

    # it needs to create players and fill their fields now
    player_1 = Player(input('Enter name of the first player '), field)
    player_1.fill_the_field(field)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        typewriter('\nSee you next time!')

