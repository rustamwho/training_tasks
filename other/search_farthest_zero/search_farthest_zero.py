"""
Как вы уже знаете, Виталий тщательно следит за соблюдением социальной
дистанции, поэтому в любом общественном месте он старается выбрать места
подальше от других посетителей.
Сейчас он выбирается в кино. Ему не важно, в каком ряду брать билет.
Информация о местах записана массивом строк: каждая строка описывает свой ряд.
если на. i-ом месте в строке 0, то i-ое место слева на этом ряду свободно,
если стоит 1 -- значит занято.
Необходимо указать номер ряда и сидения, которое необходимо купить Виталию,
чтоб минимальное расстояние до соседа по вертикали и по горизонтали было
максимальным. Выведите номер сидения, считая что нумерация кресел идет с
единицы.
В первой строке задано два числа: количество рядов и количество мест в каждом
ряде. Каждое до 10^5
В последующих строках задано описание мест в соответствующем ряду
"""

import os

import numpy as np
from collections import namedtuple

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Seat(namedtuple('Seat', 'coordinate distance_to_neighbor')):
    __slots__ = ()

    def __str__(self):
        return ' '.join(str(x + 1) for x in self.coordinate)


def get_minimum_distance(x: int, y: int, matrix: np.ndarray):
    """Поиск растояния до ближайшего соседа."""
    nearest_neighbor: bool = False
    count = 1
    errors = 0
    while not nearest_neighbor and errors < 4:
        errors = 0
        for dx, dy in DIRECTIONS:
            try:
                neighbor_coord = (x + count * dx, y + count * dy)
                if matrix[neighbor_coord]:
                    nearest_neighbor = True
                    break
            except IndexError:

                errors += 1
                continue
        count += 1 if not nearest_neighbor else 0
    return count - 1


def main(matrix: np.ndarray, length_x: int = None, length_y: int = None):
    best_seat = None

    for x in range(length_x):
        for y in range(length_y):

            if not matrix[x, y]:
                distance = get_minimum_distance(x, y, inp_matrix)

                if not best_seat or best_seat.distance_to_neighbor < distance:
                    best_seat = Seat(coordinate=(x, y),
                                     distance_to_neighbor=distance)

    return best_seat


if __name__ == '__main__':
    inp_matrix = []
    name_input_file = 'input.txt'
    # Если нет входного файла заполнение рандомом
    if os.path.exists(name_input_file):
        with open(name_input_file) as file:
            len_x = int(file.readline().rstrip())
            len_y = int(file.readline().rstrip())
            for _ in range(len_x):
                inp_matrix.append([int(x) for x in file.readline().rstrip()])
            inp_matrix = np.array(inp_matrix)
    else:
        inp_matrix = np.random.randint(0, 2, (10, 30))
        len_x, len_y = inp_matrix.shape
    print(inp_matrix)

    best_place = main(inp_matrix, len_x, len_y)
    print(f'Best seat on {best_place}')
