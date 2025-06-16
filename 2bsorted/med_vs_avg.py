from mypkg.mathzwo import MathZwo as M2

# Einkomme in k€
income = [1000] + list(range(1, 10)) # [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(M2.clc_avg(income))
print(M2.clc_med(income))

# --> der Median ist *robuster* gegenüber Ausreißern als das arithm. Mittel