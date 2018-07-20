print('Calculation of simple numbers.');

your_number = int(input('Enter your number: '));


for number in range(2, your_number + 1):
    composite = False;
    for divider in range(3, number):
        rest_of_division = number % divider;
        if rest_of_division == 0:
            composite = True;
            break;
    if not composite:
        print(number);