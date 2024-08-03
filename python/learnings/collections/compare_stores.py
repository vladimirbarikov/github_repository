store_a = ['телевизоры', 'планшеты', 'ноутбуки', 'смартфоны', 'компьютеры', 'аудиомагнитола']
store_b = ['ноутбуки', 'смартфоны', 'колонки', 'аксессуары', 'бытовая техника', 'мониторы', 'умный дом', 'ноутбуки']

store_a_set = set(store_a)
store_b_set = set(store_b)

print(f'ДО: {len(store_a)}, ПОСЛЕ: {len(store_a_set)}')
print(f'ДО: {len(store_b)}, ПОСЛЕ: {len(store_b_set)}')

print()

print(store_a_set.intersection(store_b_set))  # пересечение двух множеств вариант 1
# ищутся одинаковые значения в двух множествах
print(store_a_set & store_b_set)  # пересечение двух множеств вариант 2

print()

print(store_a_set.union(store_b_set))  # объединение двух множеств вариант 1
print(store_a_set | store_b_set)  # объединение двух множеств вариант 2

print()

print(store_b_set - store_a_set)  # вычитание одного множества из другого, вариант 1
# то, что есть в store_b_set и нет в store_a_set
print(store_b_set.difference(store_a_set))  # вычитание одного множества из другого, вариант 2
# то, что есть в store_b_set и нет в store_a_set

print()

print(store_b_set.symmetric_difference(store_a_set))  # симметричное вычитание одного множества из другого, вариант 1
# ищутся разные значения в обоих множествах
print(store_b_set ^ store_a_set)  # симметричное вычитание одного множества из другого, вариант 2
# ищутся разные значения в обоих множествах

print()

stores_intersection = store_a_set & store_b_set
stores_union = store_a_set | store_b_set

intersection_percent = (len(stores_intersection) / len(stores_union)) * 100
print(f'Процент совпавших категорий: {intersection_percent} %')

print()

b_dif_a = store_b_set.difference(store_a_set)
b_dif_a_percent = (len(b_dif_a) / len(stores_union)) * 100
print(f'Процент непокрытых категорий из В: {b_dif_a_percent} %')

print()

a_dif_b = store_a_set.difference(store_b_set)
a_dif_b_percent = (len(a_dif_b) / len(stores_union)) * 100
print(f'Процент непокрытых категорий из A: {a_dif_b_percent} %')

print()

for elem in b_dif_a:
    print(elem)
