"""
Реализация задачи из search_farthest_zero.py только с использованием строк.
"""

from collections import namedtuple

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Seat(namedtuple('Seat', 'coordinate distance_to_neighbor')):
    __slots__ = ()

    def __str__(self):
        return ' '.join(str(x + 1) for x in self.coordinate)


def get_minimum_distance(x: int, y: int, matrix: list[str]):
    """Поиск растояния до ближайшего соседа."""
    nearest_neighbor: bool = False
    count = 1
    errors = 0
    while not nearest_neighbor and errors < 4:
        errors = 0
        for dx, dy in DIRECTIONS:
            try:
                neighbor_x = x + count * dx
                neighbor_y = y + count * dy
                if matrix[neighbor_x][neighbor_y] == '1':
                    nearest_neighbor = True
                    break
            except IndexError:
                # Если все 4 направления вышли за границы, завершение цикла
                errors += 1
                continue
        count += 1 if not nearest_neighbor else 0
    return count - 1


def main(matrix: list[str], length_x: int = None, length_y: int = None):
    best_seat = None
    for x in range(length_x):
        for y in range(length_y):
            if matrix[x][y] == '0':
                distance = get_minimum_distance(x, y, inp_matrix)
                if not best_seat or best_seat.distance_to_neighbor < distance:
                    best_seat = Seat(coordinate=(x, y),
                                     distance_to_neighbor=distance)
    return best_seat


if __name__ == '__main__':
    inp_matrix = []
    with open('input.txt') as file:
        len_x = int(file.readline().rstrip())
        len_y = int(file.readline().rstrip())
        for _ in range(len_x):
            inp_matrix.append(file.readline().rstrip())

    best_place = main(inp_matrix, len_x, len_y)
    print(best_place)
