input_data = [1, 2, 10, 3, 2, 4, 5]


def moving_average(input_data, window):
    mov_avgs = []
    for i in range(1, len(input_data) + 1):
        if i < window:
            mov_avgs.append(0)
        else:
            mov_avgs.append(sum(input_data[i - window:i]) / window)

    return mov_avgs


# функция замены выброса
def replace_outlier(input_data):
    mov_avgs = moving_average(input_data, 3)

    max_index = 0
    for i in range(len(input_data)):  # находим индекс максимального элемента
        if input_data[i] > input_data[max_index]:
            max_index = i

    new_data = input_data.copy()
    new_data[max_index] = mov_avgs[max_index]

    print('до:', sum(input_data)/len(input_data),
          'после:', sum(new_data)/len(new_data))


replace_outlier(input_data)
