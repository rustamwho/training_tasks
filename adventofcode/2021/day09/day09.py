from math import prod


def get_adjacent_points(heightmap: tuple[tuple[int]], i: int, j: int) -> dict:
    """ Return dict of existing adjacent points {<coordinate> : <value>}. """
    adjacent_points = {}
    if j > 0:
        adjacent_points[(i, j - 1)] = heightmap[i][j - 1]  # left adjacent
    if j < len(heightmap[i]) - 1:
        adjacent_points[(i, j + 1)] = heightmap[i][j + 1]  # right adjacent
    if i > 0:
        adjacent_points[(i - 1, j)] = heightmap[i - 1][j]  # up adjacent
    if i < len(heightmap) - 1:
        adjacent_points[(i + 1, j)] = heightmap[i + 1][j]  # down adjacent
    return adjacent_points


def is_low_point(heightmap: tuple[tuple[int]], i: int, j: int) -> bool:
    """ Return current point less than all adjacent points. """
    current_value = heightmap[i][j]
    adjacent_points = get_adjacent_points(heightmap, i, j)
    return all(current_value < value for value in adjacent_points.values())


def get_all_low_points(heightmap: tuple[tuple[int]]) -> dict:
    """
    Return dict with all points that are less than all adjacent points.
    {<coordinate> : <value>}
    """
    low_points = {}
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if is_low_point(heightmap, i, j):
                low_points[(i, j)] = heightmap[i][j]
    return low_points


def sum_risk_levels_of_low_points(heightmap: tuple[tuple[int]]) -> int:
    """ Part 1. Return sum of risk level of all low points. """
    low_points = get_all_low_points(heightmap)
    return sum(point_value + 1 for point_value in low_points.values())


def get_basin_length(heightmap: tuple[tuple[int]],
                     point: tuple[int, int]) -> int:
    """ Create basin with its coordinates and return count of points in it. """
    basin_points = set()  # All point in current basin
    borders = [point]  # Basin borders list

    while borders:
        i, j = borders.pop()

        if (i, j) in basin_points:
            continue

        adjacent_points = get_adjacent_points(heightmap, i, j)
        # If adjacent point larger than current - add it to borders list
        for point, value in adjacent_points.items():
            if heightmap[i][j] < value < 9:
                borders.append(point)

        basin_points.add((i, j))

    return len(basin_points)


def multiply_larges_basins(heightmap):
    """ Part 2. Return multiply together the sizes of three largest basins. """
    low_points = get_all_low_points(heightmap)
    basins_sizes = [get_basin_length(heightmap, point) for point in low_points]

    return prod(sorted(basins_sizes, reverse=True)[:3])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_heightmap = tuple(
            tuple(int(x) for x in row) for row in file.read().split('\n')
        )

    part1 = sum_risk_levels_of_low_points(input_heightmap)
    part2 = multiply_larges_basins(input_heightmap)

    print('Part 1:', part1)
    print('Part 2:', part2)
