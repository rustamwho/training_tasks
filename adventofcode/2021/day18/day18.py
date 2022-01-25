import itertools
import json
import math
from functools import reduce


def add_left(x, n):
    """ Add number to left pair if any. """
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    """ Add number to right pair if any. """
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_right(x[1], n)]


def explode(x, n=4):
    """ Explode input bracket. """
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exploded_a, left, a, right = explode(a, n - 1)
    if exploded_a:
        return True, left, [a, add_left(b, right)], None
    exploded_b, left, b, right = explode(b, n - 1)
    if exploded_b:
        return True, None, [add_right(a, left), b], right
    return False, None, x, None


def split(x: int | list) -> (bool, int | list):
    """ Split input number or list. If split, return <True> and new list. """
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b) -> list:
    """ Return sum of two lines. """
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def calculate_magnitude(x) -> int:
    """ Recursive function for calculate magnitude. """
    if isinstance(x, int):
        return x
    return 3 * calculate_magnitude(x[0]) + 2 * calculate_magnitude(x[1])


def get_magnitude(lines: list) -> int:
    """ Adds up all the lines and return magnitude for final sum. """
    return calculate_magnitude(reduce(add, lines))


def get_largest_magnitude(lines: list) -> int:
    """ Return largest magnitude of sum of two lines from input lines. """
    return max(calculate_magnitude(add(a, b)) for a, b in
               itertools.permutations(lines, 2))


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = list(map(json.loads, file.read().splitlines()))

    part1 = get_magnitude(input_lines)
    print(f'Part 1: {part1}')

    part2 = get_largest_magnitude(input_lines)
    print(f'Part 2: {part2}')
