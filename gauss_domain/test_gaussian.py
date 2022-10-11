import numpy as np
import pytest

from gaussian import Gaussian

def test_gaussian_init():
    g = Gaussian(1, 2, 5)

    assert [g.mu, g.var, g.n] == [1, 2, 5]

def test_gaussian_init_numpy():
    x = np.array([1, 2, 3, 4])
    g = Gaussian.from_numpy(x)

    assert [g.mu, g.var, g.n] == [2.5, 1.25, 4]

