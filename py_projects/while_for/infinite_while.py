# эта программа демонстрирует бесконечный цикл

# создать переменную для управления циклом
keep_going = 'д'

# Предупреждение! Бесконечный цикл!
while keep_going == 'д':
    # получить продажи продавца и его ставку комиссионных
    sales = float(input('введите объемы продаж: '))
    comm_rate = float(input('введите ставку комиссионных: '))

    # рассчитать комиссионное вознаграждение
    commission = sales * comm_rate

    # показать комиссионные вознаграждение
    print('комиссионное вознаграждение составляет $',
          format(commission, '.2f'), sep='')