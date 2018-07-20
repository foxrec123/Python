
def my_func(*strings, glue = ':'):
    list_of_strings = []
    for item in strings:
        if len(item) > 3:
            list_of_strings.append(item)
    total_string = glue.join(list_of_strings)
    print(total_string)

my_func('Hello','Sergei', '125','History',glue='->')
