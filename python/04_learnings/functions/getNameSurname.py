def get_name_data(input_data, request=0):
    fi = input_data.lower().split(',')

    surname = fi[0].split(':')[1]
    name = fi[1].split(':')[1]

    if request == 'фамилия':
        return surname

    if request == 'имя':
        return name

    return surname, name


print(get_name_data('Фамилия:Петрова,Имя:Анжела', 'фамилия'))
print(get_name_data('Фамилия:Петрова,Имя:Анжела', 'имя'))
print(get_name_data('Фамилия:Петрова,Имя:Анжела'))
