import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

# Parameter der normalverteilung  
# 
mu = 166 # Mittelwert μ  (Körpergröße Frauen Deutschland )
sigma = 10 # Standardabweichung σ

# Dichtefunktion, also hier Normalverteilung 
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000) 
pdf = norm.pdf(x, mu, sigma) # Probability density function (Wahrscheinlichkeitsdichtefunktion)

# Wahrscheinlichkeit P(X >= 171)
x_threshold = 166
prob_ge_threshold = norm.sf(x_threshold, mu, sigma) # Survival Funktion später noch wichtig
                            
# Plot 
fig, ax = plt.subplots()
ax.plot(x, pdf, label=r"$N(166, 10)")
ax.fill_between(x[x >= x_threshold], pdf[x >= x_threshold], alpha = 0.3)
ax.set_xlabel("Körpergröße")
ax.set_ylabel("Dichte")
ax.set_title(f"P(X>={x_threshold}cm) = {prob_ge_threshold:.3%}")
ax.legend()
plt.show()