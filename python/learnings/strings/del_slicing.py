# command del
user_scores = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4]
del user_scores[0]
print(user_scores)
print(user_scores[0])

# slicing (start:stop:step), step 1
user_scores = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4]
print(user_scores[3:11:1])

# slicing (start:stop:step), step 2
user_scores = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4]
print(user_scores[3:11:2])

# slicing (start:stop:step), without step
user_scores = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4]
print(user_scores[3:11])

# slicing (start:stop:step), without stop
user_scores = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4]
print(user_scores[3:])

print('ABCD'[1:])
print('ABCD'[::-1])

l = [0, 1, 2, 3]
print(l)
l[:2] = ('AB', 'CD')
print(l)

l = [0, 1, 2, 3]
print(l)
l[:2] = (7, 8, 9, 10)
print(l)