import requests
import re

def get_info():
    r = requests.get('https://habr.com/')
    return r.text


if __name__ == '__main__':
    text = get_info()

    name_pattern = '"https:.*/"'
    links = re.findall(name_pattern, text)
    print(len(links))
    for item in links:
        print(item + '\n')