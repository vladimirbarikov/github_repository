test_set = {1, 2, 10}
print(test_set)
print(type(test_set))

print(min(test_set))    # нахождение минимального значения
print(max(test_set))    # нахождение максимального значения
print(len(test_set))    # нахождение длинны множества

test_set.add(100)       # динамическое добавление значения в множество
print(test_set)

test_set.discard(100)   # удаление значения из множества
print(test_set)

test_set.discard(1000)   # если удалить несуществующего значения из множества, ничего не произойдет
print(test_set)

print(10 in test_set)