import requests


def get_habrahabr():
    r = requests.get('https://vk.com')

    print(r.status_code)
    print(r.headers)
    print(r.content)

get_habrahabr()