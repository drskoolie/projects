from functools import wraps
from time import time
from matplotlib import pyplot as plt

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        return te-ts
    return wrap

@timing
def foo_o1(n):
    for i in range(n):
        x = i * i

@timing
def foo_o2(n):
    for i in range(n):
        for j in range(n):
            x = i * i


@timing
def foo_o3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                y = k * k


x = [x for x in range(100)]
y_o1 = []
y_o2 = []
y_o3 = []

for n in x:
    y_o1.append(foo_o1(n))
    y_o2.append(foo_o2(n))
    y_o3.append(foo_o3(n))

plt.plot(x, y_o1, label='O(n)')
plt.plot(x, y_o2, label='O(n$^2$)')
plt.plot(x, y_o3, label='O(n$^3$)')
plt.legend(loc = 'best')
plt.show()

