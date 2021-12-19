from collections import defaultdict


def pass_day(fishes: dict) -> dict:
    """ Calculate population of fishes after one day. """
    # new_fishes_days_count = {days: count_of_fishes with this *day* number}
    new_fishes_days_count = defaultdict(int)
    for days, fish_count in fishes.items():
        if days == 0:
            days = 7
            new_fishes_days_count[8] += fish_count
        new_fishes_days_count[days - 1] += fish_count
    return new_fishes_days_count


def emulation_of_life(fishes_days_count: dict, days: int) -> int:
    """ Emulation of *days* life of lanternfishes. """
    for _ in range(days):
        fishes_days_count = pass_day(fishes_days_count)
    return sum(fishes_days_count.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_ages = [int(x) for x in file.read().split(',')]
    input_dict = {days: input_ages.count(days) for days in set(input_ages)}
    part1 = emulation_of_life(input_dict, 80)
    part2 = emulation_of_life(input_dict, 256)

    print('Part 1:', part1)
    print('Part 2:', part2)
