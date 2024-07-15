def fibonacci(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))


def power_2(n):
    if n != 0:
        return 2 * power_2(n - 1)
    else:
        return 1


print(power_2(5))
