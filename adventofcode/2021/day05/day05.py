class Line:
    def __init__(self, coordinates: str):
        start, end = coordinates.split(' -> ')
        self.start = tuple(int(x) for x in start.split(','))
        self.end = tuple(int(x) for x in end.split(','))

    def is_horizontal_or_vertical(self) -> bool:
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def __repr__(self):
        return self.__str__()


def get_hashmap_with_overlap_points(lines: list[Line]) -> dict:
    """
    Pass through all points in each line and save it in hashmap.
    Return hashmap with intersection point f at least two lines.
    """
    hashmap = {}

    for line in lines:
        # dx, dy - diffs for iteration:
        # +1 -- if coordinate increasing
        # -1 -- if coordinate decreasing
        # 0 -- if start and end coordinates are equal
        dx = (1 if line.end[0] > line.start[0] else
              -1 if line.end[0] < line.start[0] else 0)
        dy = (1 if line.end[1] > line.start[1] else
              -1 if line.end[1] < line.start[1] else 0)

        x, y = line.start

        while (x, y) != (line.end[0] + dx, line.end[1] + dy):
            if (x, y) in hashmap:
                hashmap[(x, y)] += 1
            else:
                hashmap[(x, y)] = 1
            x, y = x + dx, y + dy

    result = {x: y for x, y in hashmap.items() if y > 1}
    return result


def count_overlap_horizontal_vertical_lines(lines: list[Line]) -> int:
    """Part 1. Count of intersections of only horizontal and vertical lines."""
    correct_lines = [x for x in lines if x.is_horizontal_or_vertical()]
    hashmap = get_hashmap_with_overlap_points(correct_lines)
    return len(hashmap)


def count_overlap_lines(lines: list[Line]) -> int:
    """ Part 2. Count of intersections of all lines. """
    hashmap = get_hashmap_with_overlap_points(lines)
    return len(hashmap)


if __name__ == '__main__':
    input_coordinates = []
    with open('input.txt', 'r') as file:
        for input_line in file.read().split('\n'):
            input_coordinates.append(Line(input_line))

    part1 = count_overlap_horizontal_vertical_lines(input_coordinates)
    part2 = count_overlap_lines(input_coordinates)
    print('Part 1:', part1)
    print('Part 2:', part2)
