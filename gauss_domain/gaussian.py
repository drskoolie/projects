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
        mu_flag = round(self.mu, 3) == round(other.mu, 3)
        var_flag = round(self.var, 3) == round(other.var, 3)
        n_flag = self.n == other.n

        return mu_flag and var_flag and n_flag

    def __add__(self, other):
        n_new = self.n + other.n
        mu_new = (self.mu*self.n + other.mu*other.n)/n_new
        var_new = self.n * (self.var + self.mu ** 2)
        var_new += other.n * (other.var + other.mu ** 2)
        var_new /= n_new
        var_new += -(mu_new ** 2)

        return Gaussian(mu_new, var_new, n_new)

    def __mul__(self, other):
        if self.n == 1:
            mu_new = self.mu * other.mu
            var_new = (self.mu ** 2) * other.var
            n_new = other.n

        elif other.n == 1:
            mu_new = self.mu * other.mu
            var_new = (other.mu ** 2) * self.var
            n_new = self.n

        return Gaussian(mu_new, var_new, n_new)

    def __repr__(self):
        return f"Gaussian({self.mu:.2f}, {self.var:.2f}, {self.n})"


if __name__ == "__main__":
    ## Part 0: Intialization
    import numpy as np
    import matplotlib.pyplot as plt

    x0 = np.array([2])
    x1 = np.array([3, 4])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)

    print(f"g0: {g0}")
    print(f"g1: {g1}")

    print(g0 * g1)

    y = 50
    z = y * np.random.normal(loc=g1.mu, scale=g1.var**0.5, size=100000)
    print(f"z(mu) = {z.mean()}, z(var) = {z.std() ** 2}")
    print(f"z(mu) = {y * g1.mu}, z(var) {(y ** 2) * g1.var}")
    plt.hist(z, bins=1000)
    plt.show()


