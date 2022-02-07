import re
from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True)
class Cubes:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def intersection(self, other):
        """ Intersect two cubes and return new Cubes object if is exists. """
        new_cubes = Cubes(
            max(self.x1, other.x1),
            min(self.x2, other.x2),
            max(self.y1, other.y1),
            min(self.y2, other.y2),
            max(self.z1, other.z1),
            min(self.z2, other.z2),
        )

        if (new_cubes.x1 <= new_cubes.x2 and new_cubes.y1 <= new_cubes.y2 and
                new_cubes.z1 <= new_cubes.z2):
            return new_cubes

    def cubes_count(self):
        """ Return count of cubes in Cubes object. """
        return (
                (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) *
                (self.z2 - self.z1 + 1)
        )


def cubes_from_string(string: str) -> Cubes:
    """ Return Cubes object from input line. """
    return Cubes(*map(int, re.findall(r'-?[0-9]+', string)))


def count_on_cubes_after_reboot(instructions, region=None):
    """ Simulate of reactor rebooting and return count of turn on cubes. """
    cubes_counter = Counter()

    for turn_on, cubes in instructions:
        if region and (cubes := cubes.intersection(region)) is None:
            continue

        new_counter = Counter()
        for c_cubes, count in cubes_counter.items():
            if intersection := cubes.intersection(c_cubes):
                new_counter[intersection] -= count

        cubes_counter.update(new_counter)

        if turn_on:
            cubes_counter[cubes] += 1

    return sum(c.cubes_count() * count for c, count in cubes_counter.items())


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()

    instructions_input = [
        (line.split(' ')[0] == 'on', cubes_from_string(line))
        for line in data.splitlines()
    ]
    inp_region = Cubes(-50, 50, -50, 50, -50, 50)

    part1 = count_on_cubes_after_reboot(instructions_input, inp_region)
    print(f'Part 1: {part1}')

    part2 = count_on_cubes_after_reboot(instructions_input)
    print(f'Part 2: {part2}')
