def get_min2(a, b):
    if a > b:
        return b
    else:
        return a


def get_min_list(numbers):
    min_value = numbers[0]
    for i in range(1, len(numbers)):
        min_value = get_min2(min_value, numbers[i])
    return min_value


numbers = [11, 9, 100, 5, 56]
print(get_min_list(numbers))
