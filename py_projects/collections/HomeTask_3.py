# Task 3

# Рекомендации к выполнению:
# Используйте функцию zip, чтобы итерироваться одновременно по координатам точки A и точки B.
# Квадратный корень числа можно вычислить, возведя его в степень 0.5.

coords1 = [(1, 10), (1, 11)]
coords2 = [(0, 20), (20, 20)]
coords3 = [(100, 91, 87), (80, 35, 70)]
coords4 = [(0, 100, 20), (0, 0, 80)]


def ab_distance(coords):
    a, b = coords
    coords_list = []

    for coord in zip(a, b):
        coords_list.append(coord)

    if len(coords_list) < 3:
        xa = coords_list[0][0]
        xb = coords_list[0][1]
        ya = coords_list[1][0]
        yb = coords_list[1][1]

        ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5

    else:
        xa = coords_list[0][0]
        xb = coords_list[0][1]
        ya = coords_list[1][0]
        yb = coords_list[1][1]
        za = coords_list[2][0]
        zb = coords_list[2][1]

        ab = ((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2) ** 0.5

    return ab


print(ab_distance(coords1))
print(ab_distance(coords2))
print(ab_distance(coords3))
print(ab_distance(coords4))
