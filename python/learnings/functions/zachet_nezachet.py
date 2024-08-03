def zachet(parameter):
    count_5, count_other = 0, 0

    for score in parameter:
        if score == 5:
            count_5 += 1
        else:
            count_other += 1

    print("Зачет получен:", count_5 > count_other)


scores = [1]
zachet(scores)

zachet([5, 5, 4, 4])
zachet([5, 5, 4, 4, 3, 2])
zachet([5, 5, 5, 5, 3, 2])
