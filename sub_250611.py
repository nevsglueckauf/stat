import numpy as np
import pandas as pd
import statistics


def clc_avg(dta:list) ->float:
    return  sum(dta) / len(dta)

data = [1, 4,5,1,2,2,2,1]
# Mittelwert - diverse!

# Hier: das arithmetische Mittel - auch E(X), Erwartungswert


print(clc_avg(dta=data))


print(statistics.mean(data))

fav_tec = ['PHP', 'Python', 'C++', 'Go', 'PHP', 'Rust', 'Pascal', 'PHP', 'Basic']

print(list(set(fav_tec)))

from collections import Counter
print(Counter(fav_tec))