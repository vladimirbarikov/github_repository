test_tuple1 = ()        # первый вариант создания кортежа - просто поставить круглые скобки перед переменной
test_tuple2 = tuple()   # второй вариант создания кортежа - указать тип переменной и оставить круглые скобки

print(type(test_tuple1))
print(type(test_tuple2))

test_tuple2 = tuple([1, 10, 0, 0])
print(test_tuple2)

test_tuple2 = tuple('tururum')
print(test_tuple2)

print(test_tuple2[0])
print(test_tuple2[-1])
print(test_tuple2[1:5])