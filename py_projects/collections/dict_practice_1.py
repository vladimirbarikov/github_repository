# Задача 1. Турнирная таблица
# Даны финальные баллы спортсменов по результатам соревнований, которые хранятся в словаре final_scores.
# Напишите функцию, которая находит имена трёх победителей соревнования. И их результаты по данным, которые лежат
# в словаре. Победители — спортсмены с максимальным количеством баллов. Выведите результат функции на экран.
# Проверьте работоспособность программы на разных значениях final_scores.
# Пример:
# Input:
# final_scores = {'Евгений Потапенко': 120,
#                 'Иван Иванович': 200,
#                 'Кузьма Иванов': 190,
#                 'Иннокентий Соловьев': 150,
#                 'Герасим Маркелов': 190,
#                 'Олег Корнеев': 220}
# Output:
# 1 место - Олег Корнеев: 220
# 2 место - Иван Иванович: 200
# 3 место - Кузьма Иванов: 190

final_scores = {'Евгений Потапенко': 120,
                'Иван Иванович': 200,
                'Кузьма Иванов': 190,
                'Иннокентий Соловьев': 150,
                'Герасим Маркелов': 180,
                'Олег Корнеев': 220}


def champions(scores):
    scores_list = sorted(scores.values(), reverse=True)[:3]
    for i in range(3):
        for k, v in scores.items():
            if v == scores_list[i]:
                print(f'{i + 1} место - {k}: {v}')


if __name__ == '__main__':
    champions(final_scores)
