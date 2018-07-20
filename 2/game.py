
survey = {
    'What language are we learning? ': 'python',
    '2 > 1? ': 'yes',
    'How old am I? ': '31',
    'Where do I live? ': 'lybertsy',
    'What is my favorite football club? ': 'mu'
}

correct_answers = 0

for question in survey.keys():
     answer = input(question)
     if answer.lower() == survey[question]:
         print('Correct answer!')
         correct_answers += 1
     else:
         print('Wrong answer!')

information = 'Total: {} , correct answers: {}.'

print(information.format(5, correct_answers))