import requests
import json

def get_info():
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    return r.headers

def write_json(headers):
    with open(r'C:\Иван\test.json', 'w') as f:
       js = dict(headers)
       for key, value in js.items():
           print('{}:{}'.format(key, value))
       json.dump(js, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    headers = get_info()
    write_json(headers)
