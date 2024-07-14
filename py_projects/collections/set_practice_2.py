# Задача 2. Проверка на дубли
# Дан список numbers. Для каждого элемента выведите, встречался он до этого в списке или нет.
# Используйте множества для решения этой задачи.
# Проверьте работоспособность программы на разных значениях numbers.

numbers = [1, 2, 1, 3, 2]
numbers_set = set()

for number in numbers:
    if number in numbers_set:
        result = '- дубль'
    else:
        result = '- не встречалось'
        numbers_set.add(number)

    print(f'{number} {result}')
