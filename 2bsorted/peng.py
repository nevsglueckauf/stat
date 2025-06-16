import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

penguins = pd.read_json("penguins.json")

#penguins.to_json('penguins.json')

n = len(penguins)

adelies = penguins[penguins['species']=='Adelie']

k = len(adelies)
p_hat = k/n
#print(adelies, len(adelies))

Nsim = 10_000
sim_k = np.random.binomial(n, p_hat, size=Nsim)
 
bin_edges = np.arange(-5,4)

mu = n*p_hat

sigma=np.sqrt(n * p_hat * (1-p_hat))
x_grid = np.linspace(bin_edges[0], bin_edges[-1],400)
plt.figure()
plt.hist(sim_k, bins=bin_edges)

plt.show()