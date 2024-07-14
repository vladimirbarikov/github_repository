def get_average_v2(user_list):
    overall_sum = 0
    for elem in user_list:  # elem - это итерируемая переменная,
        # которая перебирает каждый элемент в списке user_list
        overall_sum += elem
    return overall_sum/len(user_list), overall_sum
    # print("I'm here")
    # все что пишется после return не исполняется,
    # так как работа функции завершается,
    # поэтому print("I'm here") не работает, и не выводит выражение "I'm here" на экран

user_1 = [1000, 1200, 100, 1200, 1500]
average, total_sum = get_average_v2(user_1)

print(average)
print(total_sum)