# Task 1

power_2_numbers = [2 ** x for x in range(1, 201) if 2 ** x < 200]
print(power_2_numbers)

generated_set = {1 if x % 5 == 0 else x for x in range(8, 51)}
print(generated_set, type(generated_set))

new_set = generated_set.symmetric_difference(power_2_numbers)
print(new_set, type(new_set))

new_set = {x for x in new_set if 34 < x < 128}
print(new_set)
