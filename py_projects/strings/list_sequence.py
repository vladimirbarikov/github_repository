user_scores = []
while True:
    # считать значение в input_data
    # input_data = -1?
    # прервать цикл
    # если нет, добавить input_data в user_scores
    input_data = int(input('Введите оценку пользователя: '))
    if input_data == -1:
        break
    else:
        user_scores.append(input_data)
print(user_scores)