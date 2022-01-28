import re
from collections import defaultdict
from itertools import combinations


def get_numbers_from_string(string: str) -> list[int]:
    """ Return list with all numbers in input string. """
    return list(map(int, re.findall(r'-?[0-9]+', string)))


def get_all_orientations(x, y, z):  # coordinate:tuple[int]):
    """
    g = []
    for ox,oy,oz in permutations((x,y,z), r=3):
        for dx,dy,dz in combinations_with_replacement((1, -1), r=3):
            g.append((ox*dx,oy*dy,oz*dz))
            #g.append(tuple(a*b for a,b in zip(diff,permuted_coordinate)))
    print(len(g), g)
    return g
    """
    return [
        (x, y, z),
        (-y, x, z),
        (-x, -y, z),
        (y, -x, z),
        (x, -z, y),
        (z, x, y),
        (-x, z, y),
        (-z, -x, y),
        (x, -y, -z),
        (y, x, -z),
        (-x, y, -z),
        (-y, -x, -z),
        (x, z, -y),
        (-z, x, -y),
        (-x, -z, -y),
        (z, -x, -y),
        (-z, y, x),
        (-y, -z, x),
        (z, -y, x),
        (y, z, x),
        (-y, z, -x),
        (-z, -y, -x),
        (y, -z, -x),
        (z, y, -x),
    ]


def get_all_orient_beacons(
        scanner: set[tuple[int]]) -> list[tuple[tuple[int]]]:
    """
    Return list of beacons positions for 24 different orientations of scanner.
    """
    return [*zip(*[get_all_orientations(*p) for p in scanner])]


def matching(
        located: set[tuple[int]],
        scanners: list[set[tuple[int]]]):
    """
    Search of match positions for each scanner (in all 24 orientations) with
    one of already located scanners.

    scanner: matched scanner with one of already located scanners
    scanner_position: position of matched scanner
    beacons_upd: right positions of beacons
    """
    for scanner in scanners:
        for beacons in get_all_orient_beacons(scanner):
            distance_counter = defaultdict(int)
            for b1 in located:
                for b2 in beacons:
                    distance = tuple([a - b for a, b in zip(b1, b2)])
                    distance_counter[distance] += 1

            counter_max = max(distance_counter.items(), key=lambda i: i[1])

            if counter_max[1] >= 12:
                dx, dy, dz = scanner_position = counter_max[0]
                beacons_upd = [(x + dx, y + dy, z + dz) for x, y, z in beacons]
                return scanner, scanner_position, beacons_upd


def relocate(scanners: list[set[tuple[int]]]):
    """
    Find positions of all beacons (relative to scanner 0).

    Returns
    -------
    located_scanners: list with scanners positions (relative to scanner 0)
    located_beacons: set of positions of all beacons
    """
    located_beacons = set(scanners.pop(0))
    located_scanners = {(0, 0, 0)}

    while scanners:
        matched_scanner, matched_scanner_pos, matched_beacons = matching(
            located_beacons, scanners)
        located_beacons |= set(matched_beacons)
        located_scanners.add(matched_scanner_pos)
        scanners.remove(matched_scanner)

    return located_scanners, located_beacons


def beacons_count(
        scanners: list[set[tuple[int]]]) -> tuple[set[tuple[int]], int]:
    """ Part 1. Return count of beacons for scanners. """
    scanners_positions, beacons = relocate(scanners)
    return scanners_positions, len(beacons)


def largest_manhattan_distance(scanners_positions: set[tuple[int]]):
    """ Part 2. Return max manhattan distance between any two scanners. """
    return max(
        sum(abs(a - b) for a, b in zip(pos2, pos1))
        for pos2, pos1 in combinations(scanners_positions, r=2)
    )


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    input_scanners = []

    for scanner_data in data.split('\n\n'):
        scanner_set = set()
        for line in scanner_data.splitlines()[1:]:
            scanner_set.add(tuple(get_numbers_from_string(line)))
        input_scanners.append(scanner_set)

    scanners_pos, part1 = beacons_count(input_scanners)
    print(f'Part 1: {part1}')

    part2 = largest_manhattan_distance(scanners_pos)
    print(f'Part 2: {part2}')
