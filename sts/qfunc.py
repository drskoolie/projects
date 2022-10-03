import numpy as np
from statistics import NormalDist
from matplotlib import pyplot as plt

x = np.arange(0, 5, 0.05)
y = np.zeros(len(x))

for idx, value in enumerate(x):
    y[idx] = 1 - NormalDist(mu=0, sigma=1).cdf(value)

plt.plot(x, y)
plt.title("Q function")
plt.show()
