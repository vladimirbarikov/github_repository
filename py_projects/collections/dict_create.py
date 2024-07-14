test_dict1 = {}
print(test_dict1)
print(type(test_dict1))

test_dict2 = dict()
print(test_dict2)
print(type(test_dict2))

test_dict = {'facebook': 120, 'youtube': 299}
print(len(test_dict))
print(test_dict['facebook'])  # если указать несуществующий ключ, выйдет ошибка

test_dict[1] = 115  # ключами могут быть и списки и кортежи
print(test_dict)

test_dict[(1, 2)] = 115  # ключами могут быть и списки и кортежи
print(test_dict)

test_dict[1] = -100  # если указать тот же ключ с другим значением, то значение обновится
print(test_dict)

# на типы данных ключей есть ограничения, ключи не могут быть списками, зато на типы данных значений
# нет никаких органичений, они могут быть и числами и списками и кортежами (чем угодно)

del test_dict[(1, 2)]
del test_dict[1]
print(test_dict)