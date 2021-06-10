import numpy as np
from functools import reduce
from copy import deepcopy
import time


def convert_to_np(input_tile):
    matrix = np.array([[int(x) for x in list(row)] for row in input_tile])
    return matrix


def all_variations_tile(input_tile: np.ndarray):
    """Все возможные вариции тайла"""
    options = []
    for i in range(4):
        rotated_matrix = np.rot90(input_tile, i)
        flipped_matrix = np.flip(rotated_matrix, 1)
        options.append(rotated_matrix)
        options.append(flipped_matrix)
    return options


def get_borders(input_tile: np.ndarray):
    """Список боковых граней тайла"""
    all_borders = [input_tile[0]]
    all_borders.append(np.array([x[0] for x in input_tile]))
    all_borders.append(input_tile[-1])
    all_borders.append(np.array([x[-1] for x in input_tile]))
    return all_borders


def get_neighbors_count(all_variations: dict) -> {}:
    """Количество подходящих соседей для каждого тайла
    Также возвращаются словари:
     1. С гранями каждой вариации каждого тайла
     2. С соседями каждого тайла"""
    counts = {}
    # новый словарь - номер тайла: {номер варицаии: вариация}
    for name, variations_tiles in all_variations.items():
        options_dict = {}
        for i, variation in enumerate(variations_tiles):
            options_dict[i] = variation
        all_variations[name] = options_dict

    # {номер тайла:{номер вариации:боковые грани вариации}}
    all_borders = {}
    for name, variations_tiles in all_variations.items():
        variation_dict = {}
        for i, variation in variations_tiles.__items():
            variation_dict[i] = get_borders(variation)
        all_borders[name] = variation_dict
    all_borders_copy = deepcopy(all_borders)

    neighbors_dict = {}
    # перебор всех вариаций всех тайлов и подсчет количества подходящих соседей
    # {номер тайла:{номер вариации:боковые грани вариации}}
    for name, all_borders1 in all_borders.items():
        counts[name] = 0
        neighbors_dict[name] = []
        for name2, all_borders2 in all_borders.items():
            found = False
            if name == name2:
                continue
            # {номер вариации:боковые грани вариации}
            for _, borders in all_borders1.items():
                for _, borders2 in all_borders2.items():
                    for i, border in enumerate(borders):
                        if found:
                            break
                        for j, border2 in enumerate(borders2):
                            if all(np.equal(border, border2)):
                                # удаление значений из списка граней
                                borders.pop(i)
                                borders2.pop(j)
                                counts[name] += 1
                                neighbors_dict[name].append(name2)
                                found = True
                                break
    return counts, neighbors_dict, all_borders_copy


def build_image_names(corners, size_square, neighbors_dict, all_borders):
    """Построение матрицы с номерами тайлов"""
    """Для каждого тайла сохраняется только одна подходящая вариация"""
    first_corner_name = corners[0]

    image = np.zeros((size_square, size_square), dtype=int)
    image[0][0] = first_corner_name
    for i in range(0, size_square - 1):
        for j in range(0, size_square):
            name_this = image[i][j]
            found = False
            for index, borders in all_borders[name_this].__items():
                b_right = list(borders[3])
                b_bottom = list(borders[2])
                if found:
                    break
                if len(neighbors_dict[name_this]) > 1:
                    name_nbr1, name_nbr2 = neighbors_dict[name_this]
                    for index1, borders1 in all_borders[name_nbr1].__items():
                        if found:
                            break
                        for index2, borders2 in all_borders[name_nbr2].__items():
                            left1, top1 = list(borders1[1]), list(borders1[0])
                            left2, top2 = list(borders2[1]), list(borders2[0])
                            if not (b_right == left1 and b_bottom == top2) \
                                    and not (
                                    b_right == left2 and b_bottom == top1):
                                continue
                            if b_right == left1 and b_bottom == top2:
                                image[i][j + 1] = name_nbr1
                                image[i + 1][j] = name_nbr2
                            else:
                                image[i + 1][j] = name_nbr1
                                image[i][j + 1] = name_nbr2
                            found = True
                            all_borders[name_nbr1] = {index1: borders1}
                            all_borders[name_nbr2] = {index2: borders2}
                            neighbors_dict[name_nbr1].remove(name_this)
                            neighbors_dict[name_nbr2].remove(name_this)
                            break
                else:
                    name_nbr1 = neighbors_dict[name_this][0]
                    for index1, borders1 in all_borders[name_nbr1].__items():
                        top1 = list(borders1[0])
                        if b_bottom == top1:
                            image[i + 1][j] = name_nbr1
                            found = True
                            all_borders[name_nbr1] = {index1: borders1}
                            neighbors_dict[name_nbr1].remove(name_this)
                            break
    return image


def np_to_list_str(tile: np.ndarray):
    """Перевод numpy-матрицы в список"""
    new_tile = [list(row) for row in tile]
    new_tile = [['#' if x == 1 else '.' for x in row] for row in new_tile]
    return new_tile


def remove_borders(tile):
    """Удаление граней"""
    tile_without_borders = [row[1:-1] for row in tile[1:-1]]
    return tile_without_borders


def build_result_image(image_with_names, true_variations, size):
    """Построение готового изображения"""
    pre_image = []
    image = []
    for row in image_with_names:
        for tile_name in row:
            list_str_rows = np_to_list_str(true_variations[tile_name])
            tile_without_borders = remove_borders(list_str_rows)
            pre_image.append(tile_without_borders)

    index = 0
    while index < size ** 2:
        for i in range(len(tile_without_borders[0])):
            row = []
            for j in range(size):
                row.extend(pre_image[j + index][i])
            image.append(row)
        index += size

    return image


def all_variations_image(image):
    """Все вариации матрицы"""
    options = []
    pre_options = []
    flipped_image = flip_image(image)
    for flipped in flipped_image:
        pre_options.extend(rotate_image(flipped))
        pre_options.extend([flipped])

    for var in pre_options:
        if var not in options:
            options.append(var)

    return options


def flip_image(image):
    """Отражение матрицы горизонтально, вертикально и по диагонали"""
    flipped_image = [image[::-1]]
    flipped_image.append([row[::-1] for row in image if row])
    flipped_image.append([row[::-1] for row in flipped_image[0] if row])
    return flipped_image


def rotate_image(image):
    """Поворот матрицы"""
    rotate_images = []
    new_image = image.copy()
    for _ in range(4):
        rotated_image = zip(*new_image[::-1])
        new_image = []
        for rotated in rotated_image:
            new_image.append(list(rotated))
        rotate_images.append(new_image)
    return rotate_images


def find_monsters(image, monster_mask):
    """Поиск монстра по маске в поле"""
    size = len(image)
    # координаты частей монстра
    coordinates = []
    for coordinate in [(i, j) for i, x in enumerate(monster_mask) for j, y
                       in enumerate(x) if y == '#']:
        coordinates.append(coordinate)

    count = 0
    # количество совпадений всех частей монстра с изображением
    for i in range(size - len(monster_mask)):
        for j in range(size - len(monster_mask[0])):
            if all(image[i + dx][j + dy] == '#' for dx, dy in coordinates):
                count += 1
    if count != 0:
        return count
    return None


def read():
    input_tiles = {}
    with open('input.txt', 'r') as file:
        data = file.read().split('\n\n')
    for input_tile in data:
        n, t = input_tile.split(':\n')
        n = int(n.split(' ')[1])
        input_tiles[n] = t.replace('#', '1').replace('.', '0').split('\n')
    # количество тайлов в каждой строке
    input_size = int(pow(len(input_tiles), 0.5))
    return input_tiles, input_size


# PART1
tiles, size_of_square = read()

for name, tile in tiles.items():
    tiles[name] = convert_to_np(tiles[name])

variations = {}
for name, tile in tiles.items():
    variations[name] = all_variations_tile(tile)

# borders - {номер тайла:{номер вариации:боковые грани вариации}}
neighbors_count, neighbors_dict, borders = get_neighbors_count(variations)
# у угловых всего 2 соседа
corners = [name for name, value in neighbors_count.items() if value == 2]
corners_mul = reduce(lambda x, y: x * y, corners)

# PART 2
# матрица с правильно расположенными именами тайлов
image_names = build_image_names(corners, size_of_square, neighbors_dict,
                                borders)

# {name:tile} для каждого тайла остался один вариант
variations = {name: variations[name][index] for name, i in borders.items() for
              index, _ in i.items()}

res_image = build_result_image(image_names, variations, size_of_square)

monster = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)

image_variations = all_variations_image(res_image)

water_grids = 0
monsters_count = None

for image in image_variations:
    water_grids = sum(row.count('#') for row in image)
    monsters_count = find_monsters(image, monster)
    if monsters_count is not None:
        break

m_grids = sum(row.count('#') for row in monster)
roughness = water_grids - monsters_count * m_grids

print(f"Corners:\t\t\t{corners}\n"
      f"Multiply corners:\t{corners_mul}\n\n"
      f"Monsters count:\t\t{monsters_count}\n"
      f"Water roughness:\t{roughness}")
