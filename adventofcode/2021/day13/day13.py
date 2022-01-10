def do_fold(dots: set, fold_instruction: str) -> set:
    """ Return dots after the fold of sheet. """
    axis, value = fold_instruction.split('=')
    index = 0 if axis.endswith('x') else 1
    value = int(value)

    new_dots = set()
    for coordinate in dots:
        new_coordinate = list(coordinate)
        if new_coordinate[index] > value:
            new_coordinate[index] = value - (new_coordinate[index] - value)
        new_dots.add(tuple(new_coordinate))
    return new_dots


def print_dots_after_folds(dots, folds):
    """ Print sheet after all fold instructions. """
    for fold in folds:
        dots = do_fold(dots, fold)

    max_x = max(x[0] for x in dots)
    max_y = max(y[1] for y in dots)

    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            if (x, y) in dots:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':
    input_dots = set()
    input_folds = []
    with open('input.txt', 'r') as file:
        data = file.read().split('\n\n')
    for line in data[0].splitlines():
        x, y = line.split(',')
        input_dots.add((int(x), int(y)))
    input_folds = [instruction for instruction in data[1].splitlines()]

    part1 = len(do_fold(input_dots, input_folds[0]))
    print(f'Part 1: {part1}')

    print('Part 2:')
    print_dots_after_folds(input_dots, input_folds)
