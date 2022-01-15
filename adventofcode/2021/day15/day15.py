import heapq
from datetime import datetime

ADJACENT_COORDINATES_OFFSET = (
    (-1, 0), (0, 1), (1, 0), (0, -1)
)


def get_neighbors4(coordinate: tuple[int, int], tmap: dict) -> [tuple[int]]:
    """ Return tuple with coordinates of adjacent points in <tmap>. """
    neighbors = (
        tuple(
            (x + d) for x, d in zip(coordinate, offset)
        ) for offset in ADJACENT_COORDINATES_OFFSET
    )
    return [x for x in neighbors if x in tmap]


def get_best_path_risk_level(risk_levels_map: dict):
    """
    Return path weight for the last point in map.
    Dijkstra's algorithm. Used heap.
    """
    height = max(x for x, _ in risk_levels_map)
    width = max(x for _, x in risk_levels_map)

    nodes_heap = [(0, 0, 0)]  # (<path_weight>, <x>, <y>)
    visited_nodes = set()

    while nodes_heap:
        path_weight, x, y = heapq.heappop(nodes_heap)

        if (x, y) == (height, width):
            return path_weight

        for node in get_neighbors4((x, y), risk_levels_map):
            if node not in visited_nodes:
                new_to_heap = (path_weight + risk_levels_map[node], *node)
                heapq.heappush(nodes_heap, new_to_heap)
                visited_nodes.add(node)


def build_full_grid(risk_levels_map: dict):
    """ Return full map (x25 for the input map). """
    h = max(x for x, _ in risk_levels_map) + 1
    w = max(x for _, x in risk_levels_map) + 1

    full_map = {}
    for (x, y), r in risk_levels_map.items():
        for dx in range(5):
            for dy in range(5):
                full_map[x + dx * h, y + dy * w] = (r + dx + dy - 1) % 9 + 1

    return full_map


def get_risk_level_for_full_map(risk_levels_map: dict):
    """ Part 2. Build full map and return best path weight. """
    full_map = build_full_grid(risk_levels_map)
    return get_best_path_risk_level(full_map)


if __name__ == '__main__':
    input_map = {}
    with open('input.txt', 'r') as file:
        data = file.read()

    for i, line in enumerate(data.splitlines()):
        for j, level in enumerate(line):
            input_map[(i, j)] = int(level)

    start_time = datetime.now()
    part1 = get_best_path_risk_level(input_map)
    print(f'Part 1: {part1} - {datetime.now() - start_time}')

    start_time = datetime.now()
    part2 = get_risk_level_for_full_map(input_map)
    print(f'Part 2: {part2} - {datetime.now() - start_time}')
