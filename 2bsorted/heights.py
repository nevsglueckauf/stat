import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# np.random.randint(1, 7000))
heights = {
    "franziska": 169,
    "laura": 165,
    "steffen": 180,
    "mario": 180,
    "sarah": 165,
    "pouria": 184,
    "sammy": 174,
    "caterina": 169,
    "chrinstine": 168,
    "nadja": 162,
    "michael": 186,
    "patrick": 185,
    "jan": 186,
    "bruno": 178,
    "theo": 179,
    "tim": 172,
    "sven": 178,
    "jaxx": 187,
    "alexej": 185,
    "jo": 176,
    "iulia": 164,
    "sascha": 186,
}
ha = np.array([list(heights.values())])
# df = pd.array(heights)

# print(heights.values())

# KDE Kerndichteschätzer
# Kernel density estimator
# print(ha)
kde = gaussian_kde(ha)
x = np.linspace(ha.min() - 5, ha.max() + 5)
y = kde
# print([ha.min() - 5, ha.max() + 5])
# exit()
#plt.figure(figsize=(6, 4))
try:
    plt.plot(x, y)
except Exception as e:
    print(repr(e))
#plt.hist(ha, bins=range(160, 191, 55), density=True)


plt.show()
