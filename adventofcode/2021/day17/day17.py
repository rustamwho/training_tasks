import re
from dataclasses import dataclass
from collections import defaultdict
import itertools


@dataclass
class Area:
    x1: int
    x2: int
    y1: int
    y2: int


def get_numbers_from_string(string: str) -> list[int]:
    """ Return list with all numbers in input string. """
    return list(map(int, re.findall(r'-?[0-9]+', string)))


def max_height(area: Area) -> int:
    """ Part 1. Return max height on the best trajectory. """
    vy_max = -area.y1 - 1
    return vy_max * (vy_max + 1) // 2


def all_variants(area: Area) -> int:
    """
    Part 2. Return the count of distinct initial velocity values cause the
    probe to be within the target area after any step.
    """
    vys = defaultdict(list)  # <V_y> : <steps_count from y=0 to target area>
    for init in range(area.y1, -area.y1):
        y, vy = 0, init
        for i in itertools.count(1):
            y += vy
            vy -= 1
            if area.y1 <= y <= area.y2:
                vys[init].append(i)
            elif y < area.y1:
                break

    vxs = defaultdict(set)  # <V_x> : <steps_count from x=0 to target area>
    for init in range(1, area.x2 + 1):
        x, vx = 0, init
        for i in itertools.count(1):
            x += vx
            if vx > 0:
                vx -= 1
            if vx == 0:
                if area.x1 <= x <= area.x2:
                    vxs[init] = min(vxs[init], default=i)
                break
            if area.x1 <= x <= area.x2:
                vxs[init].add(i)
            elif x > area.x2:
                break

    count = 0
    for y_steps_count in vys.values():
        for x_steps_count in vxs.values():
            if isinstance(x_steps_count, int):
                if any(i >= x_steps_count for i in y_steps_count):
                    count += 1
            elif any(i in x_steps_count for i in y_steps_count):
                count += 1

    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        xmin, xmax, ymin, ymax = get_numbers_from_string(file.read().strip())
        target_area = Area(xmin, xmax, ymin, ymax)
    part1 = max_height(target_area)
    print(f'Part 1: {part1}')

    part2 = all_variants(target_area)
    print(f'Part 2: {part2}')
