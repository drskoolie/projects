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
        n_new = int((self.n + other.n)/2)
        mu_new = (self.mu*self.n + other.mu*other.n)/(self.n + other.n)
        var_new = (self.var*self.n + other.var*other.n)/(self.n + other.n)

        return Gaussian(mu_new, var_new, n_new)

    def __repr__(self):
        return f"Gaussian({self.mu:.2f}, {self.var:.2f}, {self.n})"


if __name__ == "__main__":
    ## Part 0: Intialization
    import numpy as np

    x0 = np.array([1, 3])
    x1 = np.array([3, 4])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)

    print(g0)
    print(g1)

    print(g0 * g1)

