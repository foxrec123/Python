from flask import Flask, request

import random

from os import environ

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

class Numbers(object):
    """
    The class serves for working with numbers
    """
    number = None
    number_of_attempts = 1

    @classmethod
    def new_number(cls):

        cls.number = random.randint(1, 100)
        cls.number_of_attempts = 1
        print(cls.number)

    @classmethod
    def compare_number(cls, users_number):
        if cls.number == users_number:
            return '='
        elif cls.number > users_number:
            cls.number_of_attempts += 1
            return '>'
        elif cls.number < users_number:
            cls.number_of_attempts += 1
            return '<'


class Guess(FlaskForm):
    """
    The class gets number from user
    """
    users_number = DecimalField(label='Number is ', validators=[validators.Required()])



@app.route('/', methods=['GET'])
def home_get():
    Numbers.new_number()
    return 'Number is defined!'


@app.route('/guess', methods=['POST'])
def home_post():
    form = Guess(request.form)
    if form.validate():
        message = Numbers.compare_number(form.users_number.data)
        if message == '=':
            number_of_attempts = Numbers.number_of_attempts
            Numbers.new_number()
            return 'Numbers are equal!. Number of attempts is {}. ' \
                   'New number has been defined!'.format(number_of_attempts)
        else:
            return message


if __name__ == '__main__':
    seed_number = environ.get('FLASK_RANDOM_SEED')
    if seed_number is None:
        seed_number = 2

    print('FLASK_RANDOM_SEED =', seed_number)

    random.seed(seed_number)

    app.run()