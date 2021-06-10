from functools import reduce


class Tile:

    def __init__(self, name, tile):
        self.name = name
        self.tile = tile
        # все вариации тайла (8)
        self.variations = all_variations_image(tile)
        # боковые грани всех вариаций тайла
        self.all_borders = get_borders_with_side(self.variations)


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


def get_borders_with_side(variations):
    """Список боковых граней каждой вариации тайла"""
    all_borders = {}
    for index, variation in enumerate(variations):
        top = variation[0]
        left = [x[0] for x in variation]
        bottom = variation[-1]
        right = [x[-1] for x in variation]
        all_borders[index] = {'top': top, 'right': right,
                              'bottom': bottom, 'left': left
                              }
    return all_borders


def build_image_with_names(tiles, size):
    """."""
    # пустой пре-список для выходного изображения
    image = []
    for _ in range(pow(size, 2)):
        image.append([])
    # список с копиями изображения для каждой вариации всех тайлов
    # в каждой копии предполагается, что тайл находится в левом верхнем углу
    # матрицы, поэтому ставится на первую позицию
    # 8 вариаций, 144 тайла = 1152
    image_variations = []
    for tile in tiles:
        for index, _ in enumerate(tile.variations):
            image_copy = image.copy()
            image_copy[0] = (tile, index)
            image_variations.append((image_copy, set([tile])))
    # перебор
    while True:
        image, used_tiles = image_variations.pop()

        # изображение построено
        if len(used_tiles) == len(tiles):
            return image

        current_index = len(used_tiles)

        top_variation = None
        left_variation = None

        # если индекс не первой строки матрицы, берется граница верхнего тайла
        if current_index >= size:
            top_tile, index = image[current_index - size]
            top_variation = top_tile.all_borders[index]['bottom']

        # если индекс не у правой границы матрицы, берется граница тайла слева
        if current_index % size != 0:
            left_tile, index = image[current_index - 1]
            left_variation = left_tile.all_borders[index]['right']

        for tile in tiles:
            if tile in used_tiles:
                continue

            for index, _ in enumerate(tile.variations):

                if top_variation:
                    if tile.all_borders[index]['top'] != top_variation:
                        continue

                if left_variation:
                    if tile.all_borders[index]['left'] != left_variation:
                        continue
                # данная вариация совпадает левой и верхней гранью с соседними
                # имя тайла и индекс вариации записываются в "матрицу"
                image[current_index] = (tile, index)
                used_tiles.add(tile)
                image_variations.append((image.copy(), used_tiles))


def remove_borders(tile):
    """Удаление граней"""
    tile_without_borders = [row[1:-1] for row in tile[1:-1]]
    return tile_without_borders


def build_result_image(image_with_names, size):
    """Построение матрицы готового изображения с удалением граней"""
    pre_image = []
    res_image = []
    for tile in image_with_names:
        true_tile, variation_index = tile
        variation = true_tile.variations[variation_index]
        tile_without_borders = remove_borders(variation)
        pre_image.append(tile_without_borders)

    index = 0
    while index < pow(size, 2):
        for i in range(len(tile_without_borders[0])):
            row = []
            for j in range(size):
                row.extend(pre_image[j + index][i])
            res_image.append(row)
        index += size
    return res_image


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


def search(image):
    monster = (
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    )
    # все 8 вариаций изображения
    image_variations = all_variations_image(image)

    water_grids = 0
    monsters_count = None
    # монстра можно найти только в одной вариации изображения
    for image_variation in image_variations:
        # количество решеток на всем поле
        water_grids = sum(row.count('#') for row in image_variation)
        monsters_count = find_monsters(image_variation, monster)
        if monsters_count is not None:
            break
    # количество решеток в маске монстра
    m_grids = sum(row.count('#') for row in monster)
    roughness = water_grids - monsters_count * m_grids

    return roughness, monsters_count


def read():
    with open('input.txt') as f:
        raw_tiles = f.read().split('\n\n')

    input_tiles = []
    for input_tile in raw_tiles:
        tile = []
        name, t = input_tile.split(':\n')
        name = int(name.split(' ')[1])
        for row in t.split('\n'):
            chars = []
            for char in row:
                chars.append(char)
            tile.append(chars)
        input_tiles.append(Tile(name, tile))

    size = int(pow(len(input_tiles), 0.5))
    return input_tiles, size


tiles, size_of_square = read()

# PART 1
# список с правильно расположенными именами тайлов
image_names = build_image_with_names(tiles, size_of_square)

corners_mask = [0, size_of_square - 1, -size_of_square, -1]
corners = [image_names[x][0].name for x in corners_mask]
corners_mul = reduce(lambda x, y: x * y, corners)

# PART 2
# готовое изображение
result_image = build_result_image(image_names, size_of_square)
# поиск монстров
roughness, monsters_count = search(result_image)

print(f"Corners:\t\t\t{corners}\n"
      f"Multiply corners:\t{corners_mul}\n\n"
      f"Monsters count:\t\t{monsters_count}\n"
      f"Water roughness:\t{roughness}")
