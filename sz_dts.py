from textfoo import Texitfy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import gaussian_kde


heights = {
    "Beulah": 180,
    "Branden": 179,
    "Druci": 167,
    "Carolina": 168,
    "Aloin": 154,
    "Brok": 185,
    "Dorotea": 154,
    "Deena": 195,
    "Syman": 170,
    "Lynette": 184,
    "Batholomew": 198,
    "Darcee": 170,
    "Whitney": 186,
    "Robbie": 177,
    "Reina": 191,
    "Kinnie": 156,
    "Jeni": 151,
    "Fabio": 177,
    "Vinni": 182,
    "Jamie": 169,
    "Evelin": 194,
    "Shea": 195,
    "Jenine": 192,
    "Almeda": 190,
    "Yance": 152,
    "Mallorie": 164,
    "Darcie": 193,
    "Dermot": 193,
    "Elisabeth": 181,
    "Orlan": 169,
    "Erasmus": 181,
    "Eustace": 194,
    "Alyssa": 185,
    "Ulysses": 192,
    "Merell": 150,
    "Selia": 165,
    "Amelie": 157,
    "Jermain": 178,
    "Zarah": 180,
    "Betti": 172,
    "Fidel": 193,
    "Iona": 167,
    "Vivianna": 152,
    "Nelly": 189,
    "Kevyn": 168,
    "Nickolas": 167,
    "Athene": 180,
    "Angeline": 176,
    "Frederica": 169,
    "Merrie": 174,
    "Jere": 190,
    "Laraine": 197,
    "Wildon": 168,
    "Bartolemo": 191,
    "Adriaens": 157,
    "Nikolaus": 166,
    "Everett": 154,
    "Sherri": 189,
    "Lamar": 157,
    "Mortimer": 192,
}


heights_array = np.array(list(heights.values()))
# Für Kerndichteschätzung
kde = gaussian_kde(heights_array)

n = len(heights_array)

# Standardabweichung
std = heights_array.std(ddof=1)

# Abweichung
h = 1.06 * std * n ** (-1 / 5)

# Gauß Kernel Konstante
kern_konst = 1 / (h * math.sqrt(2 * math.pi))



# Integral von np.exp(-0.05 * (x-hi) **2) ist immer 1 ???

# AuswertungsGrid
x = np.linspace(heights_array.min() - 5, heights_array.max() + 5, 400)
y = kde(x)

mi = heights_array.min()
ma = heights_array.max()
me = heights_array.mean()
seg = ", ".join([str(mi), str(ma), str(me)])
# Plot

plt.figure(figsize=(6, 4))

# Anzeige der kleinen Kerne
kernels = [kern_konst*np.exp(-0.05 * (x-hi) **2) / n for hi in heights_array]
for y in kernels:
    plt.plot(x,y,alpha=0.2)



plt.plot(x, y, linewidth=2)
plt.hist(
    heights_array,
    bins=range(heights_array.min() - 5, heights_array.max() + 5, 8),
    density=True,
    alpha=0.3,
    edgecolor="black",
)
plt.xlabel("Größe in cm (" + seg + ")")
plt.ylabel("(Kernel) density")
plt.title("KDE")
# plt.grid(True)
plt.show()
