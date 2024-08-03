for day in range(1, 32):
    day_str = str(day)
    print('Сегодня ' + day_str + '-е число.', end = ' - ')
    if day % 7 == 0:
        print('Сплю весь день.')
        continue
    elif day & 7 == 6:
        pass
    else:
        print('Усердно работаю.', end = ' - ')
    print('Что-то я устал.')
