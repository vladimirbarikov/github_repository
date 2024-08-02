HIGH_SCORE = 95

test1 = int(input('Введите оценку 1: '))
test2 = int(input('Введите оценку 2: '))
test3 = int(input('Введите оценку 3: '))

average = (test1 + test2 + test2) / 3

print('Средний бал составляет:', average)

if average >= HIGH_SCORE:
    print('Поздравляем!')
    print('Отличный средний бал!')