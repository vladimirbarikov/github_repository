# Задача 6(1). Закупки
# Дан список orders, который состоит из кортежей. Каждый кортеж — это закупка определённого покупателя.
# В нём хранится следующая информация:
# - id покупателя, количество товаров, сумма покупки;
# Определите размер скидки для каждого покупателя по истории покупок из списка orders.
# Рассчитать скидку можно по следующему алгоритму:
# - если сумма покупок от 10 тыс. руб. — скидка 5%;
# - если сумма покупок от 15 тыс. руб. — скидка 10%;
# - если сумма покупок от 20 тыс. руб. — скидка 15%;
# - если сумма покупок менее 10 тыс. руб. — скидка 0%.
# Результаты расчёта запишите в словарь discount_system в следующем виде:
# - ключ — id покупателя;
# - значение — словарь вида: {'discount': 5, 'total_sum': 12000},
#   где discount — размер скидки, total_sum — общая сумма покупок.
# Используйте функции и декомпозицию.

orders = [
    (111, 3, 1200),
    (118, 9, 8000),
    (111, 10, 1000000),
    (119, 9, 13300),
    (156, 10, 11000),
    (123, 9, 11200),
    (178, 20, 3200),
    (178, 5, 8900),
    (156, 9, 8000),
    (123, 4, 3500),
    (101, 9, 8000),
    (101, 8, 1000),
]


def count_discount_system(orders):
    discount_system = {}
    for o in orders:
        if o[0] not in discount_system:
            discount_system[o[0]] = {'discount': 0, 'total_sum': 0}
        discount_system[o[0]]['total_sum'] += o[2]
        discount_system[o[0]]['discount'] = update_discount(discount_system[o[0]])

    return discount_system


def update_discount(customer):
    if customer['total_sum'] >= 20000:
        customer['discount'] = 15
    elif customer['total_sum'] >= 15000:
        customer['discount'] = 10
    elif customer['total_sum'] >= 10000:
        customer['discount'] = 5

    return customer['discount']


if __name__ == '__main__':
    discount_system = count_discount_system(orders)
    print(discount_system)
