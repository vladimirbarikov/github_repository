# эта программа вычисляет торговые комиссионные

# создать переменную для управления циклом
keep_going = 'д'

# вычислить серию комиссионных вознаграждений
while keep_going == 'д':
    # получить продажи продавца и его ставку комиссионных
    sales = float(input('введите объемы продаж: '))
    comm_rate = float(input('введите ставку комиссионных: '))

    # рассчитать комиссионное вознаграждение
    commission = sales * comm_rate

    # показать комиссионные вознаграждение
    print('комиссионное вознаграждение составляет $',
          format(commission, '.2f'), sep='')

    # убедиться что пользователь хочет выполнить еще одно
    keep_going = input('Хотите выполнить еще одно' +
                       '(Введите д, если да): ')