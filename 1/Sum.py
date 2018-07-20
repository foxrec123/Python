print('Calculation sum or difference two numbers.' );

first_number = input('Enter first number: ');
second_number = input('Enter second number: ');

operation = input('Enter "+" or "-": ')

if operation == '+':
    print('result is: ' + str(int(first_number) + int(second_number)));
elif operation == '-':
    print('result is: ' + str(int(first_number) - int(second_number)));
else:
    print('Something was wrong');