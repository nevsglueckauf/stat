import statistics
import numpy as np
import pandas as pd
from mypkg.statz import StatzAfoot
import math
from collections import Counter

# dta = [1, 1, 5, 3, 1, 1, 3]

# ds = pd.Series(data=dta)

# print(ds.mean())
# print(StatzAfoot.avg(dta))

# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [-100, -100, 100, 100]
# z = [-300, 10, 20, 30, 40, 200]

# print(StatzAfoot.avg(x))
# print(StatzAfoot.avg(y))
# print(StatzAfoot.avg(z))

# dta = [4,3,1,4,3,2,3,1,2]
# cnt = Counter(dta)
# print(StatzAfoot.mode(dta))


# Quantile

dta = [-3, -2, -1, 0, 1, 2, 3]

print(statistics.quantiles(dta, n=2)) # n= Teilung
print(statistics.quantiles(dta, n=3)) # n= Teilung
