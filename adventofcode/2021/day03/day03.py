from collections import OrderedDict


def get_counts_values_in_each_position(report: tuple):
    counts = {x: {'0': 0, '1': 0} for x in range(len(report[0]))}
    for report_noise in report:
        for i, value in enumerate(report_noise):
            counts[i][value] += 1
    return OrderedDict(counts)


def get_power_consumption_submarine(report: tuple) -> int:
    counts = get_counts_values_in_each_position(report)
    gamma_rate = ''.join(max(x, key=x.get) for x in counts.values())
    epsilon_rate = ''.join(min(x, key=x.get) for x in counts.values())
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_report = tuple(x for x in file.read().split('\n'))
    part1 = get_power_consumption_submarine(input_report)

    print('Part 1:', part1)
