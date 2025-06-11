import numpy as np
from collections import Counter

anzahl_wuerfe = 100000

# anzahl_wuerfe = 10

outcome = np.random.randint(1, 7, size=anzahl_wuerfe)

c = Counter(outcome)

sum = 0
for augenzahl in c:
    rel = c[augenzahl]/anzahl_wuerfe
    sum += rel
    print(f"Augenzahl: {augenzahl}, \
          relative Häufigkeit: {rel}")

print(sum)
print(outcome)

