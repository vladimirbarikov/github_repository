user_scores1 = [1, 2, 5, 5, 5, 5]
user_scores2 = [5, 5, 5, 5, 4]
new_scores = user_scores1 + user_scores2
print(new_scores)

user_scores1.extend(user_scores2)
print(user_scores1)