# Task 4

# Дано два списка: ids, count. В первом списке лежат уникальные идентификаторы товаров, во втором списке —
# количество соответствующих товаров на складе.

# Из данных в списках создайте словарь items_count, в котором будет храниться количество товара на складе.
# Ключ — ID товара, значение — количество. Решение оформите в одну строчку.

# ID товара — это строка вида: число1:число2. Число1 обозначает категорию товара, а число2 — его номер.
# Посчитайте следующие статистики на этих данных:

# 1. Количество уникальных категорий (решение оформите в одну строчку).
# 2. Среднее количество единиц товара на складе в категории (округлите до 1 цифры после запятой).
# 3. Среднее количество уникальных товаров в категории.
# 4. ID товаров с максимальным количеством единиц на складе.

ids = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205', '1001:223', '1001:127',
       '1001:236', '1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259',
       '1231:253', '1001:220', '1001:202', '1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]

items_count = dict(zip(ids, count))
unique_count = len({id.split(':')[0] for id in ids})


def avg_units_count(count, unique_count):
    sum_count = sum(count)
    avg_units = round(sum_count / unique_count, 1)
    return avg_units


def avg_uniques_count(ids, unique_count):
    sum_ids = len(ids)
    avg_uniques = round(sum_ids / unique_count, 1)
    return avg_uniques


def max_count(items_count):
    max_value = max(items_count.values())
    for k, v in items_count.items():
        if max_value == v:
            print(f'{k}: {v}')


if __name__ == '__main__':
    print(unique_count)  # 1
    print(avg_units_count(count, unique_count))  # 2
    print(avg_uniques_count(ids, unique_count))  # 3
    max_count(items_count)  # 4
