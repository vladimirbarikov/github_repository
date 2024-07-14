# округляет до 2-го знака после точки
number = format(12345.6789, '.2f')
print(number)

# округляет до 1-го знака после точки
number = format(12345.6789, '.1f')
print(number)

print('Число равно', format(1.234567, '.2f'))

# эта программа демонстрирует, как может быть
# отформатировано число с плавающей запятой

amount_due = 5000.0
monthly_payment = amount_due / 12
print('Ежемесячный платеж составляет',
      format(monthly_payment, '.2f'))

# вставка запятой в качестве разделителя
print(format(12345.6789, ',.2f'))
print(format(123456789.467, ',.2f')) # большее число чем предыдущее
print(format(12345.6789, ',f')) # без точности - округления до 2 знаков после запятой

# эта программа демонстрирует, как число с плавающей точкой
# может быть отформатировано в качестве валюты
monthly_pay = 30000.00
annual_pay = monthly_pay * 12
print('Ваша годовая зарплата составляет $',
      format(annual_pay, ',.2f'),
      sep='')

# форматирование в экспоненциальной записи
print(format(12345.6789, 'e'))
print(format(123456.789, 'e'))
print(format(1234567.89, 'e'))
print(format(12345.6789, '.2e'))
print(format(123456.789, '.2e'))
print(format(1234567.89, '.2e'))

# в первом случае после 12 стоит запятая, во втором запятой нет
print('Число равняется', format(12345.6789, '12,.2f'))
print('Число равняется', format(12345.6789, '12.2f'))
print()

# эта программа выводит приведенные ниже
# числа с плавающей точкой в столбце,
# в котором десячичные знаки выровнены
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# вывести каждое число в поле шириной 7 пробелов
# с 2-мя десятичными знаками
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))
print()

# форматирование числа в виде процента
print(format(0.5, '%'))
print(format(0.5, '.0%'))
print(format(0.5, '.2%'))
print()

# форматирование целых чисел
print(format(123456, 'd'))
print(format(123456, ',d'))
print()

# число печатается в поле шириной 10 пробелов
print(format(123456, '10d'))
print(format(123456, '10,d'))
print()