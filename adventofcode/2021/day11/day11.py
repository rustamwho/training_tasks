ADJACENT_COORDINATES_OFFSET = (
    (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
)


def get_adjacent_octopuses(coordinate: tuple[int, int]) -> tuple[tuple[int]]:
    """ Return tuple with coordinates of adjacent octopuses. """
    adjacents = tuple((
        tuple(
            (x + y) for x, y in zip(coordinate, offset)
        ) for offset in ADJACENT_COORDINATES_OFFSET
    ))
    return adjacents


def do_step(energy_levels: dict) -> tuple[dict, int]:
    """
    Emulation of one step for all octopuses.
    Return updated energy levels and count of flashes on this step.
    """
    flashed_octopuses = []  # Coordinates of all flashed octopuses on this step

    # +1 to energy level of all octopuses
    for coordinate in energy_levels.keys():
        energy_levels[coordinate] += 1
        if energy_levels[coordinate] > 9:
            flashed_octopuses.append(coordinate)
            energy_levels[coordinate] = 0

    # Stack for checking all adjacent of flashed octopuses
    to_check = flashed_octopuses.copy()

    while to_check:
        coordinate = to_check.pop()
        for adjacent in get_adjacent_octopuses(coordinate):
            if adjacent in energy_levels and adjacent not in flashed_octopuses:
                energy_levels[adjacent] += 1
                if energy_levels[adjacent] > 9:
                    to_check.append(adjacent)
                    flashed_octopuses.append(adjacent)
                    energy_levels[adjacent] = 0

    flashes_count = len(flashed_octopuses)

    return energy_levels, flashes_count


def count_flashes(energy_levels) -> int:
    """ Part 1. Return count of flashes after 100 steps. """
    flashes = 0
    for _ in range(100):
        energy_levels, flashes_in_step = do_step(energy_levels)
        flashes += flashes_in_step

    return flashes


def get_step_when_all_octopuses_flashed(energy_levels: dict):
    """ Part 2. Return number of step when all octopuses are flashed. """
    step_number = 0
    while True:
        energy_levels, flashes_count = do_step(energy_levels)
        step_number += 1
        # When all octopuses are flashed on step
        if len(energy_levels) == flashes_count:
            return step_number


if __name__ == '__main__':
    input_energy_levels = {}
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file.read().splitlines()):
            for j, x in enumerate(line):
                input_energy_levels[(i, j)] = int(x)

    part1 = count_flashes(input_energy_levels.copy())
    part2 = get_step_when_all_octopuses_flashed(input_energy_levels)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
