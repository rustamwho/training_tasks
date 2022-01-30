def neighbors_9(x: int, y: int):
    """ Return 9 neighbors of point around (include it). """
    return ((i, j) for j in (y - 1, y, y + 1) for i in (x - 1, x, x + 1))


def index_for_pixel(x: int, y: int, matrix, default):
    """
    Return index for search in image enhancement algorithm for this pixel.
    """
    neighbors = neighbors_9(x, y)
    return int(''.join(str(matrix.get(n, default)) for n in neighbors), 2)


def enhance(image, algorithm, default):
    """ Applying the image enhancement algorithm to image. """
    minx, miny = min(image.keys())
    maxx, maxy = max(image.keys())
    new_image = dict()
    for y in range(minx - 1, maxx + 2):
        for x in range(miny - 1, maxy + 2):
            index = index_for_pixel(x, y, image, default)
            new_image[(x, y)] = int(algorithm[index])
    return new_image


def lit_pixels_count(input_image, algorithm, iterations_count):
    """
    Applying the image enhancement <algorithm> to image <iterations_count>
    times and return count number of lit pixels.

    Parameters
    ----------
    input_image: dict[tuple[int,int],int]
    algorithm: tuple[int]
    iterations_count: int
    """
    for i in range(iterations_count):
        # default use because index with 0 may be 1 in enhancement algorithm
        default = 0 if algorithm[0] == 0 or i % 2 == 0 else 1
        input_image = enhance(input_image, algorithm, default)
    return sum(input_image.values())


if __name__ == '__main__':
    raw_image = dict()
    with open('input.txt', 'r') as file:
        data = file.read()
    algo, data = data.split('\n\n')
    algo = tuple(map(int, algo.replace('#', '1').replace('.', '0')))
    for r, line in enumerate(data.splitlines()):
        for v, value in enumerate(line):
            raw_image[(v, r)] = 1 if value == '#' else 0

    part1 = lit_pixels_count(raw_image, algo, 2)
    print(f'Part 1: {part1}')

    part2 = lit_pixels_count(raw_image, algo, 50)
    print(f'Part 2: {part2}')
