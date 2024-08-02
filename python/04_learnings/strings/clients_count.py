user_scores = []

clients_count = int(input('Введите количество клиентов: '))
scores = [1, 2, 3, 4, 5]

for i in range(clients_count):
    input_data = int(input('Введите оценку клиента: '))

    while input_data not in scores:
      print('Введите оценку от 1 до 5')
      input_data = int(input('Введите оценку клиента: '))

    user_scores.append((input_data))
print(user_scores)