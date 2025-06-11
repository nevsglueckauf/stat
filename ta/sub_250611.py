import numpy as np
import pandas as pd
import statistics
from mypkg.statz import StatPy

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
rel = Counter(fav_tec)
l = len(rel)
for k,v  in rel.items():
    rel[k] = round(v/l, 2)
    



print(rel)

sp = StatPy()

print(sp.rel_freq(fav_tec))

lst  = ['ausreichend', 'befriedigend', 'mangelhaft', 'gut', 'ausreichend', 'gut', 'sehr gut', 'mangelhaft', 'befriedigend', 'sehr gut', 'ungenügend', 'sehr gut', 'befriedigend', 'ausreichend', 'ausreichend', 'ungenügend', 'ausreichend', 'gut', 'ungenügend', 'gut', 'sehr gut', 'mangelhaft']

print(Counter(lst))