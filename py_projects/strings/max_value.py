user_scores = []
max_value = 0

clients_count = int(input('Введите количество клиентов: '))

for i in range(clients_count):
    input_data = int(input('Введите оценку клиента: '))

    while input_data not in [1, 2, 3, 4, 5]:
        print('Оценка должна быть в диапазоне от 1 до 5!')
        input_data = int(input('Введите оценку клиента: '))

    user_scores.append(input_data)

for value in user_scores:
    if max_value < value:
        max_value = value

max_value = str(max_value)

print(user_scores)
print('Максимальная оценка = ' + max_value)