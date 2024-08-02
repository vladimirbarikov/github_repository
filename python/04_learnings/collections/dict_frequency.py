frequency_dict = {'facebook': 120, 'youtube': 299, 'google': 300, 'radio': 432, 'other': 1}

print(frequency_dict.values())  # метод показать все значения словаря
print(frequency_dict.keys())  # метод показать все ключи словаря
print(frequency_dict.items())  # метод показать все пары словаря

print()

total_users = sum(frequency_dict.values())
print(f'Общее количество пользователей: {total_users}')

print()

for k,v in frequency_dict.items():  # k = keys, v = values
    percent = (v/total_users)*100
    print(f'{k}: {round(percent, 2)}')
