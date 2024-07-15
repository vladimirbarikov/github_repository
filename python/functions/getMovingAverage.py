def moving_average(input_data, window):
    for elem in range(1, len(input_data)+1):
        if elem < window:
            number = 0
        else:
            number = format(sum(input_data[elem - window:elem]) / window, '.2f')
        print(number, end=', ')
    print()


input_data = [1, 2, 10, 3, 2, 4, 5]
moving_average(input_data, 2)
moving_average(input_data, 3)
