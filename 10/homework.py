from flask import Flask, request
from flask.json import jsonify

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


# 1. shows locales
@app.route('/locales/')
def home1():
    js = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(js)


# 2. sun of numbers
@app.route('/sum_numbers/<first_number>/<second_number>/')
def home2(first_number, second_number):
    return str(int(first_number) + int(second_number))


# 3. shows name of user
@app.route('/greet/<user_name>/')
def home3(user_name):
    return 'Hello, {}!'.format(user_name)


# 4. Validation
class ContactForm(FlaskForm):

    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=20, message='Lenght must be from 5 to 20'),
        validators.Email(message='This is not email')
    ])

    password = PasswordField(label='New Password', validators=[
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField(label='Repeat Password')



@app.route('/form/user/', methods=['GET', 'POST'])
def home4():

    if request.method == 'POST':
        form = ContactForm(request.form)

        if form.validate():
            return jsonify({'status': 0, 'errors': {}})
        else:
            return jsonify({'status': 1, 'errors': form.errors})



    if request.method == 'GET':
        return 'hello world!', 200

#5. Return file's content
@app.route('/serve/<path:filename>/')
def home5(filename):
    try:
        f = open(r'C:\Иван\Python\Homework\.files\{}'.format(filename))
        f.close()
        return f.read()
    except:
        return '404: There is no such file!'

if __name__ == '__main__':
    app.run()
