# Reduce is a function which accumulates the values in a certain var
from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
