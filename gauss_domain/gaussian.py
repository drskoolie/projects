## Part 0: Intialization
import numpy as np


x0 = np.array([1, 2, 3, 4, 5])
x1 = np.array([6, 7, 8, 9, 11])

x2 = np.concatenate((x0, x1))

x0.mean()
x1.mean()

x2.mean()

(x0.mean() + x1.mean())/2

## Part 1: Building Class
class Gaussian():
    def __init__(self, mu, var, n):
        self.mu = mu
        self.var = var
        self.n = n

    def __repr__(self):
        return f"Gaussian({self.mu:.2f}, {self.var:.2f}, {self.n})"


g0 = Gaussian(x0.mean(), x0.std()**2, x0.size)
g1 = Gaussian(x1.mean(), x1.std()**2, x1.size)

g1.__repr__()
