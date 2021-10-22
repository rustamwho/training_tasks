"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
from collections import Counter


def move_zeros(array):
    counts = Counter(array)
    array = [x for x in array if x != 0]
    array += [0] * counts[0]
    return array


# best practice
def move_zeros2(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


def test():
    assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]


test()
