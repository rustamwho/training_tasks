def largest_smallest_model_number(add_x: list, div_z: list, add_y: list):
    """ Return largest and smallest model number for monad. """
    stack = []
    largest = [None] * 14
    smallest = [None] * 14

    for i in range(14):
        if div_z[i] == 1:
            stack.append((i, add_y[i]))

        else:
            j, must_value = stack.pop()
            must_value += add_x[i]

            if must_value > 0:
                largest[i] = 9
                largest[j] = 9 - must_value
                smallest[i] = 1 + must_value
                smallest[j] = 1

            else:
                largest[i] = 9 + must_value
                largest[j] = 9
                smallest[i] = 1
                smallest[j] = 1 - must_value

    return ''.join(map(str, largest)), ''.join(map(str, smallest))


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()

    # the monad repeat the same pattern for 14 times,
    # the pattern include 18 alu commands
    # and the following 3 type of alu commands/data are all we need
    add_x_input, div_z_input, add_y_input = [], [], []

    for k, line in enumerate(data):
        splitted_line = line.split()
        match splitted_line:
            case 'add', 'x', str(value) if value != 'z':
                add_x_input.append(int(value))
            case 'div', 'z', str(value):
                div_z_input.append(int(value))
            case 'add', 'y', str(value):
                if k % 18 == 15:
                    add_y_input.append(int(value))

    part1, part2 = largest_smallest_model_number(add_x_input,
                                                 div_z_input, add_y_input)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
