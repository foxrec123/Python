correct_answers = 0;

answer = input('What language are we learning? ')
if answer.lower() == 'python':
    print('Correct answer');
    correct_answers = correct_answers + 1;
else:
    print('Wrong answer');

answer = input('2 > 1? ')
if answer.lower() == 'yes':
    print('Correct answer');
    correct_answers = correct_answers + 1;
else:
    print('Wrong answer');

answer = input('How old am I? ')
if answer.lower() == '31':
    print('Correct answer');
    correct_answers = correct_answers + 1;
else:
    print('Wrong answer');

answer = input('Where do I live? ')
if answer.lower() == 'lybertsy':
    print('Correct answer');
    correct_answers = correct_answers + 1;
else:
    print('Wrong answer');

answer = input('What is my favorite football club? ')
if answer.lower() == 'mu':
    print('Correct answer');
    correct_answers = correct_answers + 1;
else:
    print('Wrong answer');

information = 'Total: {} , correct answers: {}.';

print(information.format(5, correct_answers));
