# file = open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt')
# words = file.read()
# print(words)

# file.close()

# words = file.read()

# result = file.closed
# print(result)

# with open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt') as file:
#     words = file.read()
# result = file.closed
# print(result)

# with open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt') as file:
#     print(file.readline())

# words = []
# with open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt') as file:
#     for word in file:
#         words.append(word)
# print(len(words))

# with open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt') as file:
#     words = file.readlines()
# print(len(words))

with open('/Users/vladimirbarikov/Skillbox/Data Scientist/Теория/Самостоятельные работы/11/anna_words.txt') as file:
    words = set(file.readlines())
print(len(words))
