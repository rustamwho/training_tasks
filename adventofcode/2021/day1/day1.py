def count_of_larger_than_previous_value(measurements: tuple) -> int:
    """Part 1. Return count of values in tuple are larger then previous."""
    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1

    return count


def count_of_larger_than_previous_sum(measurements: tuple) -> int:
    """Part 2. Return count of sums in tuple are larger then previous."""
    windows = tuple(
        x + y + z for x, y, z in zip(
            measurements[:-2], measurements[1:-1], measurements[2:])
    )

    count = count_of_larger_than_previous_value(windows)

    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        report = tuple(int(x) for x in file.read().split('\n'))

    print('Part 1:', count_of_larger_than_previous_value(report))
    print('Part 2:', count_of_larger_than_previous_sum(report))
