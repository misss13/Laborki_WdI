import matplotlib.pyplot as plt
import numpy as np

m=10
#szachownica=[[0 for i in range(m)] for j in range(m)]
#matrix=np.array(szachownica)
#data = matrix
data = np.random.random((m, m))

fig, ax = plt.subplots()
# Using matshow here just because it sets the ticks up nicely. imshow is faster.
ax.matshow(data, cmap='seismic')

for (i, j), z in np.ndenumerate(data):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')

plt.show()
