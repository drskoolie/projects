import random

random.seed(12345)
n = 10

x = [random.randint(1, 10000000) for _ in range(n)]

def min_n(input_list):
    min = 100000000000000000

    for element in input_list:
        if element < min:
            min = element

    return min

print(min_n(x))

def min_n_2(input_list):
    min = 100000000000000000
    for element1 in input_list:
        for element2 in input_list:
            if element1 < element2:


