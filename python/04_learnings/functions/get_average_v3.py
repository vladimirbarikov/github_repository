def get_sum(user_list):
    overall_sum = 0
    for elem in user_list:
        overall_sum += elem
    return overall_sum


def get_average_v2(user_list):
    overall_sum = get_sum(user_list)
    return overall_sum/len(user_list)


user1 = [1000, 1000, 1200, 1200, 1200]

print(get_sum([1, 2, 5]))
print(get_average_v2(user1))
print(min(user1))
print(max(user1))
