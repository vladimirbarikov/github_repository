items = ['Кофта', 'Брюки', 'Кроссовки', 'Шляпа', 'Игрушка']
prices = [1000, 2000, 1999, 3000, 500]

item_prices = {}  # присоединение ключей к их значениям вариант 1
for i in range(len(items)):
    item_prices[items[i]] = prices[i]
print(item_prices)

item_prices = {}  # присоединение ключей к их значениям с помощью функции zip вариант 2
for item, price in zip(items, prices):
    item_prices[item] = price
print(item_prices)

item_prices = dict(zip(items, prices))  # присоединение ключей к их значениям вариант 3
print(item_prices)

tuples_list = list(zip(items, prices))  # zip на выходе дает список таплов, что по факту (ключ, значение)
print(tuples_list)

item_prices = dict(zip(items, prices))  # присоединение ключей к их значениям
input_items = input()
if input_items in item_prices.keys():  # если введенный ключ есть в словаре item_prices, то его значение
    result = item_prices[input_items]  # добавляется в переменную result (вариант с функцией if)
else:
    result = 'Товара нет!'
print(result)

item_prices = dict(zip(items, prices))  # присоединение ключей к их значениям
input_items = input()
result = item_prices.get(input_items, 'Товара нет!')  # если введенный ключ есть в словаре item_prices, то его значение
print(result)  # добавляется в переменную result (вариант с методом get)

items = ['Кофта', 'Брюки', 'Кроссовки', 'Шляпа', 'Игрушка']
prices = [1000, 2000, 1999, 3000, 500]

items = [item.lower() for item in items]  # генератор / list comprehensions для изменения регистра

item_prices = dict(zip(items, prices))  # присоединение ключей к их значениям
input_items = input()
result = item_prices.get(input_items, 'Товара нет!')  # если введенный ключ есть в словаре item_prices, то его значение
print(result)  # добавляется в переменную result (вариант с методом get)

numbers = [x ** 2 for x in range(11)]  # цикл без условий
print(numbers)

numbers = [x ** 2 for x in range(11) if x % 2 == 0]  # цикл с одним условием (if)
print(numbers)

numbers = [x if x % 2 == 0 else x ** 2 for x in range(21)]  # цикл с двумя условиями (if/else)
print(numbers)

string_set = {str(x) for x in range(11)}  # создаем множество
print(string_set)

test_dict = {x: x * 5 for x in range(1, 6)}  # создаем словарь
print(test_dict)
print(type(test_dict))

item_prices = {item: price for item, price in zip(items, prices)}  # присоединение ключей к их значениям вариант 4
print(item_prices)  # с помощью генератора / list comprehensions
