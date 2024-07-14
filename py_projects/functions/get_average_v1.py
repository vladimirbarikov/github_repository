def get_average(user_list):
    overall_sum = 0
    for i in range(len(user_list)):
        overall_sum += user_list[i]
    print(overall_sum/len(user_list))

user_1 = [1000, 1200, 100, 1200, 1500]
get_average(user_1)

user_2 = [100, 100, 100, 100, 100]
get_average(user_2)

avg1 = get_average(user_1)
print(avg1)