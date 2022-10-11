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

def test_gaussian_len():
    x = np.array([1, 2, 3, 4])
    g = Gaussian.from_numpy(x)

    assert len(g) == len(x)

def test_gaussian_eq():
    x = np.array([1, 2, 3, 4])
    g0 = Gaussian.from_numpy(x)
    g1 = Gaussian.from_numpy(x)

    assert g0 == g1

def test_gaussian_add_n_same0():
    x0 = np.array([1, 2])
    x1 = np.array([3, 4])
    x2 = np.concatenate([x0, x1])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    g = g0 + g1

    assert g == g2


def test_gaussian_add_n_same1():
    x0 = np.array([1, 3, 1])
    x1 = np.array([3, 4, 5])
    x2 = np.concatenate([x0, x1])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    g = g0 + g1

    assert g == g2


def test_gaussian_add_n_dif():
    x0 = np.array([1, 3, 4, 5])
    x1 = np.array([-2, 3, 5])
    x2 = np.concatenate([x0, x1])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    g = g0 + g1

    assert g == g2


def test_gaussian_add_single_value():
    x0 = np.array([1, 3, 4, 5])
    x1 = np.array([10])
    x2 = np.concatenate([x0, x1])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    g = g0 + g1

    assert g == g2


def test_gaussian_add_two_single_values():
    x0 = np.array([1])
    x1 = np.array([10])
    x2 = np.concatenate([x0, x1])

    g0 = Gaussian.from_numpy(x0)
    g1 = Gaussian.from_numpy(x1)
    g2 = Gaussian.from_numpy(x2)

    g = g0 + g1

    assert g == g2
