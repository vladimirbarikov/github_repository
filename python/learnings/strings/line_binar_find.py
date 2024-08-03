# линейный поиск
input_data = [58, 90, 93, 93, 100, 111, 123, 2345, 2600]
found = False
for i in range(len(input_data)):
    if input_data[i] == 111:
        found = True
        break
print(found)

# бинарный поиск
input_data = [58, 90, 93, 94, 100, 111, 123, 2345, 2600]
b = 0
e = len(input_data) - 1
key = int(input('Введите id документа для поиска: '))
found = False

while not found:
    mid_index = int((b + e) / 2)
    mid_value = input_data[mid_index]
    if mid_value == key:
        found = True
    elif b == e:
        break
    elif mid_value < key:
        b = mid_index + 1
    else:
        e = mid_index - 1

print(found)