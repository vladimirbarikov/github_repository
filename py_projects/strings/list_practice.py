list1 = [1, 10, 2]
list2 = [0, 100]
list3 = []

del list1[1]
list2.append(50)
list2.extend(list1)
list3 = list2 + list1
print(list1)
print(list2)
print(list3)

user_scores = [5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 3, 3, 3, 5, 5, 5, 2]
max_value = user_scores[0]
min_value = user_scores[0]

for i in range(1, len(user_scores)):
    if max_value < user_scores[i]:
        max_value = user_scores[i]
    elif min_value > user_scores[i]:
        min_value = user_scores[i]
print('Максимальная оценка:', max_value)
print('Минимальная оценка:', min_value)

user_scores1 = [1, 5, 5, 1, 5, 5]
user_scores2 = [2, 3, 4, 4, 2, 3, 4, 4]
user_scores3 = [5, 5]

print(user_scores1[:int(len(user_scores1)/2)])
print(user_scores2[:int(len(user_scores2)/2)])
print(user_scores3[:int(len(user_scores3)/2)])

my_list = [1, 2, 10, 1, 0, -1, -2, -3, 1, 1, 100, 23]
my_list_reversed = []

for i in my_list[::-1]:
    my_list_reversed.append(i)
print(my_list_reversed)

N = int(input('Введите количество степеней двойки: '))
degrees = []
for i in range(N):
    degrees.append(2 ** (i + 1))
print(degrees)

user_scores = [5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 3, 3, 3, 5, 5, 5, 2]
max_value = 5
min_value = 2
max_count = []
min_count = []

for i in range(len(user_scores)):
    if user_scores[i] == max_value:
        max_count.append(user_scores[i])
    elif user_scores[i] == min_value:
        min_count.append(user_scores[i])

print('Количество максимальных оценок = '+ str(len(max_count)))
print('Количество минимальных оценок = '+ str(len(min_count)))