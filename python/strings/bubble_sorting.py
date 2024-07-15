input_data = [58, 111, 93, 72, 100, 55, 13]

n = len(input_data)

for i in range(1, n):  # цикл для расчета проходов - проходов столько, сколько пар значений в списке
    for j in range(0, n-i):  # цикл для сравнения каждой пары значений,
        # исключая последнее значение (в первом цикле i=0, во втором i=-1)
        print(j, j+1, end=' ; ')
    print()

n = len(input_data)

for i in range(1, n):
    for j in range(0, n-i):
        print(f'сейчас  стравниваем: {input_data[j]} c {input_data[j+1]}')
        if input_data[j+1] < input_data[j]:
            input_data[j], input_data[j+1] = input_data[j+1], input_data[j]

print(input_data)