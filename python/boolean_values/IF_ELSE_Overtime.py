BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input('Введите количество отработанных часов: '))
pay_rate = float(input('Введите почасовую ставку: '))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate

print('Заработная плата до удержаний составляет: $', format(gross_pay, ',.2f'), sep='')