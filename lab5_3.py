one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one_min, one_max = min(one), max(one)
two_min, two_max = min(two), max(two)
three_min, three_max = min(three), max(three)

one_treug_max = (one_max * (one_max - one_min) * (one_max - one_min - one_min)) ** 0.5 / 4
one_treug_min = (one_min * (one_min - one_min) * (one_min - one_max - one_max)) ** 0.5 / 4
two_treug_max = (two_max * (two_max - two_min) * (two_max - two_min - two_min)) ** 0.5 / 4
two_treug_min = (two_min * (two_min - two_min) * (two_min - two_max - two_max)) ** 0.5 / 4
three_treug_max = (three_max * (three_max - three_min) * (three_max - three_min - three_min)) ** 0.5 / 4
three_treug_min = (three_min * (three_min - three_min) * (three_min - three_max - three_max)) ** 0.5 / 4

print("Площадь треугольника из максимальных значений:", one_treug_max)
print("Площадь треугольника из минимальных значений:", one_treug_min)
print("Площадь треугольника из максимальных значений:", two_treug_max)
print("Площадь треугольника из минимальных значений:", two_treug_min)
print("Площадь треугольника из максимальных значений:", three_treug_max)
print("Площадь треугольника из минимальных значений:", three_treug_min)
