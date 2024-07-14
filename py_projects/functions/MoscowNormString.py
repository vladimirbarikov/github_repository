def city_normalization(city_string, city_name = 'москва'):
    normalized_string = city_string.lower()
    index = normalized_string.find(city_name)

    if index != -1:
        return city_name
    else:
        return None


print(city_normalization('москва', 'Г москва'))  # если поменять строку и подстроку, то функция выдаст None
print(city_normalization(city_name = 'москва', city_string = 'Г москва'))  # чтоб не запутаться в аргументах,
# можно прописать, какие значения нужно положить в определенный параметр
print(city_normalization('Г москва'))  # в функции по умолчанию входной параметр city_name = 'москва',
# поэтому при вызове функции без второго параметра тоже находится 'москва'
print(city_normalization('Г КАЗАНЬ', 'казань'))  # если же указать оба параметра то будет искаться тот параметр,
# что указан, например подстрока 'казань', в строке 'Г КАЗАНЬ'

print('город москва'.find('москва'))  # метод находит первый индекс подстроки в строке и возвращает его
print('город москва'.find('казань'))  # если такой подстроки нет, то метод возвращает -1
print('город москва'[6:])  # с помощью слайсинга можно вывести на экран часть строки

user_cities = ['Г москва', 'город москва', 'МоСкВа', 'г Москва', 'г.москва', 'Москва']
for elem in user_cities:
    print(f'До: {elem}, После: {city_normalization(elem)}')
