def get_name_data(input_data):
    fi = input_data.lower().split(',')

    surname = fi[0].split(':')[1]
    name = fi[1].split(':')[1]

    return surname, name


input_data = 'Фамилия:Иванов,Имя:Герасим'
print(get_name_data(input_data))

input_data = 'Фамилия:Сидоров-Ильин,Имя:Петр'
print(get_name_data(input_data))
