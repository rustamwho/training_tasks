from itertools import product
from collections import defaultdict


def do_cycles(grid, deltas):
    """Выполнение правил"""
    for _ in range(6):
        new_grid = defaultdict(int)
        # список с количеством соседних активных кубов для каждого куба
        neighbors = defaultdict(int)

        for index, value in grid.items():
            if value:
                # для всех соседних кубов
                for delta in deltas:
                    i = tuple([x + y for x, y in zip(index, delta)])
                    neighbors[i] += 1

        for index, count in neighbors.items():
            if grid[index]:
                if count in (2, 3):
                    new_grid[index] = 1
                continue
            if count == 3:
                new_grid[index] = 1

        grid = new_grid

    return sum(grid.values())


def read():
    # словари для трехмерного и четырехмерного кубов
    input_grid3d = defaultdict(int)
    input_grid4d = defaultdict(int)
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            for j, value in enumerate(line.strip()):
                if value == '#':
                    input_grid3d[(i, j, 0)] = 1
                    input_grid4d[(i, j, 0, 0)] = 1
    return input_grid3d, input_grid4d


# отклонения индексов соседних кубов
deltas3d = list(product([-1, 0, 1], repeat=3))
deltas3d.remove((0, 0, 0))
deltas4d = list(product([-1, 0, 1], repeat=4))
deltas4d.remove((0, 0, 0, 0))

main_grid3d, main_grid4d = read()

sum_active3d = do_cycles(main_grid3d, deltas3d)
sum_active4d = do_cycles(main_grid4d, deltas4d)

print(f"Part 1: SUM of active cubes in 3d - {sum_active3d}\n"
      f"Part2: SUM of active cubes in 4d - {sum_active4d}")
