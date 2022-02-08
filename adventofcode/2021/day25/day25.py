from collections import defaultdict


def step(imap: defaultdict,
         height: int, width: int) -> tuple[defaultdict, bool]:
    """ Simulate one step of moving for all sea cucumbers. """
    new_map = defaultdict(lambda: '.')
    changed = False

    for x in range(height):
        for y in range(width):
            value = imap[(x, y)]
            new_y = (y + 1) % width
            if value == '>' and imap[(x, new_y)] == '.':
                new_map[(x, new_y)] = '>'
                changed = True
            elif value != '.':
                new_map[(x, y)] = value

    imap = new_map
    new_map = defaultdict(lambda: '.')

    for x in range(height):
        for y in range(width):

            value = imap[(x, y)]
            new_x = (x + 1) % height

            if value == 'v' and imap[(new_x, y)] == '.':
                new_map[(new_x, y)] = 'v'
                changed = True
            elif value != '.':
                new_map[(x, y)] = value

    return new_map, changed


def print_map(imap: defaultdict, height: int, width: int) -> None:
    """ Only for visualization of map. """
    for x in range(height):
        print(''.join(imap[(x, y)] for y in range(width)))
    print()


def simulate_cucumber_moves(imap: defaultdict, height: int, width: int) -> int:
    """ Simulate moves of cucumbers, while all of them move. """
    count = 0
    changed = True

    while changed:
        imap, changed = step(imap, height, width)
        count += 1

    return count


if __name__ == '__main__':
    input_map = defaultdict(lambda: '.')
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()

    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if val != '.':
                input_map[(i, j)] = val

    part1 = simulate_cucumber_moves(input_map, i + 1, j + 1)
    print(f'Part 1: {part1}')
