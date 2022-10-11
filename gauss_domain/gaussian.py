## Part 1: Building Class
class Gaussian():
    def __init__(self, mu, var, n):
        self.mu = mu
        self.var = var
        self.n = n

    @classmethod
    def from_numpy(cls, array):
        return cls(mu = array.mean(), var = array.var(), n = array.size)

    def __len__(self):
        return self.n

    def __eq__(self, other):
        mu_flag = self.mu == other.mu
        var_flag = self.var == other.var
        n_flag = self.n == other.n

        return mu_flag and var_flag and n_flag

    def __repr__(self):
        return f"Gaussian({self.mu:.2f}, {self.var:.2f}, {self.n})"




if __name__ == "__main__":
    ## Part 0: Intialization
    import numpy as np


    x0 = np.array([3, 4])
    x1 = np.array([1, 2])

    x2 = np.concatenate((x0, x1))

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    print(g0)
    print(g1)
    print(g2)



