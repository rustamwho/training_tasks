import math


def difference_jolts(adapters):
    diff_one_jolt = 0
    diff_three_jolt = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff == 1:
            diff_one_jolt += 1
        elif diff == 3:
            diff_three_jolt += 1
        else:
            print('Ошибка!')
    return diff_one_jolt, diff_three_jolt


def count_combination(adapters):
    counts = [1]
    for i in range(1, len(adapters)):
        count = counts[i - 1]
        j = i - 2
        while j >= 0 and adapters[i] - adapters[j] <= 3:
            count += counts[j]
            j -= 1
        counts.append(count)
    return counts[- 1]


def count_adapters():
    adapters = []
    with open('input.txt', 'r') as file:
        for line in file:
            adapters.append(int(line.strip()))
    if 0 not in adapters:
        adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    diff_one_jolt, diff_three_jolt = difference_jolts(adapters)
    diff = diff_one_jolt * diff_three_jolt
    return adapters, diff


adapters, diff_multiply = count_adapters()
print(f'Part 1: {diff_multiply}')
combinations_cnt = count_combination(adapters)
print(f'Part 2: {combinations_cnt}')
