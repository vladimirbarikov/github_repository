test1 = set()    #создаем пустое множество
print(test1)
print(type(test1))

test_set1 = set([1, 5, 10])    #создаем множество из списка
print(test_set1)
print(type(test_set1))

test_set2 = set('mama')    #создаем множество из списка
print(test_set2)
print(type(test_set2))

test_set3 = set((1, 2, 1))    #создаем множество из кортежа
print(test_set3)
print(type(test_set3))

test_set4 = {}    #невозможно создать множество просто из фигурных скобок, получится другой тип
print(test_set4)
print(type(test_set4))

test_set5 = {1, 2, 10}    #создаем множество с помощью фигурных скобок
print(test_set5)
print(type(test_set5))
