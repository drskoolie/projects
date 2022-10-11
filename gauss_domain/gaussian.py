## Part 1: Building Class
class Gaussian():
    def __init__(self, mu, var, n):
        self.mu = mu
        self.var = var
        self.n = n

    @classmethod
    def from_numpy(cls, array):
        return cls(mu = array.mean(), var = array.var(), n = array.size)

    def __repr__(self):
        return f"Gaussian({self.mu:.2f}, {self.var:.2f}, {self.n})"



if __name__ == "__main__":
    ## Part 0: Intialization
    import numpy as np


    x0 = np.array([1, 2, 3, 4])
    x1 = np.array([6, 7, 8, 9, 11, 12, 13])

    x2 = np.concatenate((x0, x1))

    g0 = Gaussian(x0.mean(), x0.std()**2, x0.size)
    g1 = Gaussian(x1.mean(), x1.std()**2, x1.size)

    g2 = Gaussian.from_numpy(x0)

