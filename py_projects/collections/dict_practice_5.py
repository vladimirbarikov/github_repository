# Задача 5. Аналитика пользователей
# У вас есть информация по пользователям, которая хранится в users_info. Каждый элемент списка —
# это словарь с данными пользователя.
# Выведите имена и id всех пользователей, удовлетворяющих следующему условию: возраст больше 35 лет,
# в браке и без детей.

users_info = [
    {'id': 111, 'name': 'Ирина', 'age': 40, 'has_children': False, 'is_married': True},
    {'id': 121, 'name': 'Надежда', 'age': 20, 'has_children': False, 'is_married': False},
    {'id': 131, 'name': 'Степан', 'age': 21, 'has_children': False, 'is_married': False},
    {'id': 141, 'name': 'Константин', 'age': 65, 'has_children': True, 'is_married': False},
    {'id': 151, 'name': 'Мария', 'age': 52, 'has_children': True, 'is_married': True},
    {'id': 161, 'name': 'Валерия', 'age': 38, 'has_children': False, 'is_married': False},
    {'id': 171, 'name': 'Александр', 'age': 29, 'has_children': True, 'is_married': True},
]

for dicts in users_info:
    if dicts['age'] > 35 and dicts['has_children'] is False and dicts['is_married'] is True:
        print(dicts['id'], dicts['name'])
