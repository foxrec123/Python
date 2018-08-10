from flask import Flask

app = Flask(__name__)


@app.route('/sum_strings/<first_str>/<second_str>/')
def home1(first_str, second_str):
    return first_str + second_str

@app.route('/sum_numbers/<first_number>/<second_number>/')
def home2(first_number, second_number):
    return str(int(first_number) + int(second_number))

@app.route('/max_string/<first_str>/<second_str>/<third_str>/')
def home3(first_str, second_str, third_str):
    return str(max(first_str, second_str, third_str))

@app.route('/file_exists/<path:my_path>/')
def home4(my_path):
    response = ''
    try:
        f = open(r'C:\Иван\Python\Homework\{}'.format(my_path))
        response = 'Yes'
    except:
        response = 'No'
    finally:
        return response
        f.close()

if __name__ == '__main__':
    app.run()

