from statistics import median, mean
from math import ceil


def calculate_quantity(crabs_positions: tuple):
    """ Part 1. Return sum of (<median> - <crab_position>). """
    crabs_median = int(median(crabs_positions))
    result = sum(abs(x - crabs_median) for x in crabs_positions)
    return result


def sum_of_distances(crabs_positions, value):
    """ Return sum of (every number in range(<crab_position> - value)). """
    result = 0
    for crab in crabs_positions:
        distance = abs(crab - value)
        result += sum(x for x in range(1, distance + 1))
    return result


def update_calculate_quantity(crabs_positions):
    """ Part 2. Use mean instead of median. """
    pre_crabs_mean = mean(crabs_positions)
    # 2 variants, more or less than mean
    variants = (int(pre_crabs_mean), ceil(pre_crabs_mean))
    return min(sum_of_distances(crabs_positions, x) for x in variants)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_crabs_position = tuple(int(x) for x in file.read().split(','))

    part1 = calculate_quantity(input_crabs_position)
    part2 = update_calculate_quantity(input_crabs_position)

    print('Part 1:', part1)
    print('Part 2:', part2)
