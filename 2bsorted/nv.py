import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

np.random.seed(19680801)
mu = 100  ## Mittelwert der Verteilung
sigma = 15  ## Standardabweichung der Verteilung
x = mu + sigma * np.random.randn(437)

num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

ax.set_xlabel('Smarts')
ax.set_ylabel('Wahrscheinlichkeitsdichte')
ax.set_title(r'Histogramm der IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()