# Задача 6(2). Закупки
# Далее напишите программу, которая будет запрашивать id пользователя и сумму его покупки.
# По данным скидок из словаря discount_system рассчитайте сумму покупки со скидкой и выведите на экран.
# После обновите значения discount и total_sum по данному пользователю.
# Если скидка изменилась, выведите сообщение о его новой скидке на последующие покупки.
# Если пришёл новый пользователь, просто добавьте его данные в словарь discount_system.

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


def add_order(discount_system, id, order):
    if id not in discount_system:
        discount_system[id] = {'discount': 0, 'total_sum': 0}
    discount_system[id]['total_sum'] += order
    discount_system[id]['discount'] = update_discount(discount_system[id])

    return discount_system


if __name__ == '__main__':
    discount_system = count_discount_system(orders)
    id = int(input('ID? '))
    order = float(input('Стоимость покупки? '))

    if id not in discount_system:
        discount = 0
    else:
        discount = discount_system[id]['discount']
    new_price = order * (1 - discount / 100)
    print(f'Стоимость покупки со скидкой {discount} = {new_price}')

    discount_system = add_order(discount_system, id, new_price)

    if discount_system[id]['discount'] != discount:
        print('Ваша программа лояльности обновилась, новая скидка:', discount_system[id]['discount'])
