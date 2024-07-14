fio = 'Иванов Герасим Александрович'
splitted_fio = fio.split()
surname = splitted_fio[0]
name = splitted_fio[1]
middle_name = splitted_fio[2]



print(f'Фамилия:{surname}, Имя:{name}, Отчество:{middle_name}')
print(f'Фамилия:{1+2}, Имя:{name}, Отчество:{middle_name}')
print(f'Фамилия:{len(fio)}, Имя:{name}, Отчество:{middle_name}')

fio = '??Иванов Герасим Александрович'
print(fio[2:])