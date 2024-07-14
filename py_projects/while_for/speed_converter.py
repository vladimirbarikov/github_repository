# эта программа преобразует скорости
# от 60 до 130 км/ч
# (с приращиванием в 10 км) в mph

start_speed = 60
end_speed = 131
increment = 10
conversion_factor = 0.6214

# напечатать заголовок
print('KPH\t\tMPH')
print('____________')

# напечатать скорости
for kph in range (start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(format(kph, '.1f')+'\t'+format(mph, '.1f'))