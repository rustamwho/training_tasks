from collections import Counter
import re

directions = {'e': (1, 0), 'w': (-1, 0), 'se': (1, 1),
              'sw': (0, 1), 'ne': (0, -1), 'nw': (-1, -1)}


def search_coordinate_tile(tile):
    # Получение координат по командам
    x, y = 0, 0
    for move in tile:
        dx, dy = directions[move]
        x += dx
        y += dy
    return x, y


def count_black_tiles(tiles):
    """Количество черных плиток в первой части
    Берутся координаты очередной плитки,
    если она есть в списке черных плиток - удаляем"""
    black_tiles = []

    for tile in tiles:
        p = search_coordinate_tile(tile)
        if p in black_tiles:
            black_tiles.remove(p)
        else:
            black_tiles.append(p)

    count = len(black_tiles)
    return count, black_tiles


def one_day(tiles):
    """Очередной переворот"""
    neighbors_delta = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
    # {Координата плитки : количество соседних черных плиток}
    neighbors_count = Counter(
        (x + dx, y + dy) for x, y in tiles for dx, dy in neighbors_delta)
    # Новый список черных тайлов исходя из условий
    new_tiles = [neighbor for neighbor, count in neighbors_count.items() if
                 count == 2 or (count == 1 and neighbor in tiles)]
    return new_tiles


def count_black_tiles_after100(black_tiles):
    """Количсетво черных тайлов спустя 100 дней"""
    for _ in range(100):
        black_tiles = one_day(black_tiles)
    count = len(black_tiles)
    return count


def read():
    tiles = []
    with open('input.txt', 'r') as file:
        for line in file:
            tiles.append(re.findall(r"(e|w|se|sw|ne|nw)", line))
    return tiles


list_tiles = read()
count1, blacks = count_black_tiles(list_tiles)
count2 = count_black_tiles_after100(blacks)
print(f"Number of black tiles after 1 day:\t\t{count1}\n"
      f"Number of black tiles after 100 days:\t{count2}")
