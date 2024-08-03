# Задача 2. Расстановка людей в очереди
# Есть три типа билетов, которые хранятся в кортеже ticket_types. Также есть список посетителей, которые на данный
# момент стоят в очереди, типы их билетов хранятся в user_tickets.
# Напишите функцию, которая отсортирует user_tickets по очереди, указанной в ticket_types. Сначала в user_tickets
# должны оказаться все билеты, которые находятся на нулевом месте в ticket_types, потом те, которые на первом месте
# в ticket_types, затем остальные.
# Проверьте работоспособность программы на разных значениях ticket_types, user_tickets
# Пример:
# Input:
# ticket_types = ('Ж', 'К', 'З')
# user_tickets = ['З', 'К', 'К', 'З', 'З', 'З', 'Ж', 'К', 'Ж']
# Output: ['Ж', 'Ж', 'К', 'К', 'К', 'З', 'З', 'З', 'З']

ticket_types = ('Ж', 'К', 'З')
user_tickets = ['З', 'К', 'К', 'З', 'З', 'З', 'Ж', 'К', 'Ж']


def sorted_tickets(types, tickets):
    sorted_list_zh = []
    sorted_list_k = []
    sorted_list_z = []
    zh = ord(types[0])
    k = ord(types[1])
    z = ord(types[2])
    for elem in tickets:
        if ord(elem) == zh:
            sorted_list_zh.append(elem)
        elif ord(elem) == k:
            sorted_list_k.append(elem)
        elif ord(elem) == z:
            sorted_list_z.append(elem)
    output = sorted_list_zh + sorted_list_k + sorted_list_z
    return output


print(sorted_tickets(ticket_types, user_tickets))

# Попробуйте реализовать предыдущую задачу с помощью нового метода .count().
# Он считает, сколько раз элемент встречается в списке. Например, чтобы найти, сколько раз Ж встречается в списке,
# нужно вызвать: user_tickets.count('Ж').
# Сравните время выполнения вашего кода и кода c count c помощью функции timeit.
# P.S. Если вы изначально воспользовались методом count, сделайте задачу наоборот: попробуйте реализовать решение
# программы без его использования и также сравнить время выполнения.

zh = user_tickets.count(ticket_types[0])
k = user_tickets.count(ticket_types[1])
z = user_tickets.count(ticket_types[2])

sorted_list = [zh*ticket_types[0], k*ticket_types[1], z*ticket_types[2]]

print(sorted_list)