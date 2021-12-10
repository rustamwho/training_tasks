from collections import OrderedDict


# ----> Part 1
def get_counts_values_in_position(report: tuple, position: int = None):
    """
    Return dict with counts of 0 and 1.
    If position received - return counts only for this position bits.
    e.g. {'0': 3, '1': 5}.
    If position not received - return counts for all positions.
    e.g. {0: {'0': 3, '1': 5}, 1: {'0': 6, '1': 2} ...}
    """
    if isinstance(position, int):
        counts = {'0': 0, '1': 0}
        for report_noise in report:
            counts[report_noise[position]] += 1
        return counts

    counts = {x: {'0': 0, '1': 0} for x in range(len(report[0]))}
    for report_noise in report:
        for i, value in enumerate(report_noise):
            counts[i][value] += 1
    return OrderedDict(counts)


def get_power_consumption_submarine(report: tuple) -> int:
    """ Calculate gamma and epsilon rates and return multiply their. """
    counts = get_counts_values_in_position(report)
    gamma_rate = ''.join(max(x, key=x.get) for x in counts.values())
    epsilon_rate = ''.join(min(x, key=x.get) for x in counts.values())
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


# ----> Part 2
def filter_report(report: tuple, rating_name: str) -> str:
    """
    Filter report for calculating oxygen generator rating or CO2 scrubber
    rating and return only one matching element from report.
    """
    bit_position = 0
    support = '1' if rating_name == 'oxygen_generator' else '0'

    while len(report) > 1:
        counts = get_counts_values_in_position(report, position=bit_position)
        count0, count1 = counts.values()

        if count0 == count1:
            report = [x for x in report if x[bit_position] == support]
            bit_position += 1
            continue

        if rating_name == 'oxygen_generator':
            max_bit = max(counts, key=counts.get)
            report = [x for x in report if x[bit_position] == max_bit]
        if rating_name == 'co2_scrubber':
            min_bit = min(counts, key=counts.get)
            report = [x for x in report if x[bit_position] == min_bit]
        bit_position += 1

    return report[0]


def get_multiply_ratings(report: tuple) -> int:
    """
    Calculate oxygen generator and CO2 scrubber ratings and return their
    multiplication.
    """
    oxygen_generator_rating = filter_report(report, 'oxygen_generator')
    co2_scrubber_rating = filter_report(report, 'co2_scrubber')
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_report = tuple(x for x in file.read().split('\n'))

    part1 = get_power_consumption_submarine(input_report)
    part2 = get_multiply_ratings(input_report)

    print('Part 1:', part1)
    print('Part 2:', part2)
