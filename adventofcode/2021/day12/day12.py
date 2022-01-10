def get_count_of_paths(neighbors: dict[str, list[str]],
                       current_cave: str = 'start',
                       visited: list | None = None,
                       repeat_small_cave: bool = False) -> int:
    """ Return all paths count. """
    if not visited:
        visited = []

    if current_cave == 'end':
        return 1

    if current_cave.islower() and current_cave in visited:
        # If part 2 (can repeat one small cave twice)
        if repeat_small_cave and current_cave != 'start':
            repeat_small_cave = False
        else:
            return 0

    visited.append(current_cave)

    count = 0
    for adjacent_cave in neighbors[current_cave]:
        count += get_count_of_paths(neighbors, adjacent_cave, visited.copy(),
                                    repeat_small_cave)

    return count


def part_1(neighbors: dict[str, list[str]]) -> int:
    return get_count_of_paths(neighbors)


def part_2(neighbors: dict[str, list[str]]) -> int:
    return get_count_of_paths(neighbors, repeat_small_cave=True)


if __name__ == '__main__':
    input_neighbors: dict[str, list[str]] = {}

    with open('input.txt', 'r') as file:
        for line in file.read().splitlines():
            cave, neighbor = line.split('-')
            if cave in input_neighbors:
                input_neighbors[cave].append(neighbor)
            else:
                input_neighbors[cave] = [neighbor]
            if neighbor in input_neighbors:
                input_neighbors[neighbor].append(cave)
            else:
                input_neighbors[neighbor] = [cave]

    part1 = part_1(input_neighbors)
    part2 = part_2(input_neighbors)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
