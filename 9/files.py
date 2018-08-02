def read_file():
    filename = input('Enter path of file:')

    with open(filename) as f:
        print(f.read())


def write_to_file():
    filename = input('Enter path of file: ')
    content  = input('Enter content: ')

    with open(filename, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    read_file()
    #write_to_file()