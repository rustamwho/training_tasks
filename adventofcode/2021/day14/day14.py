from collections import defaultdict


def insertion_process(pairs: defaultdict[str, int], rules: dict[str, str]):
    """ Simulation of one step of polymerization. """
    new_pairs = pairs.copy()

    for pair, count in pairs.items():
        if pair not in rules:
            continue
        replace_letter = rules[pair]

        first_pair = pair[0] + replace_letter
        second_pair = replace_letter + pair[1]

        new_pairs[pair] -= count
        new_pairs[first_pair] += count
        new_pairs[second_pair] += count

    return new_pairs


def polymerization(template: str, rules: dict, steps: int) -> int:
    """
    Return difference between quantities of most common and least common chars
    after < steps > steps polymerization.
    """
    len_template = len(template)

    first_char = template[0]
    last_char = template[-1]

    # Create dict with pairs in input template
    pairs = defaultdict(int)
    for i, j in zip(range(len_template - 1), range(1, len_template)):
        pair = template[i:j + 1]
        pairs[pair] += 1

    # Simulation
    for _ in range(steps):
        pairs = insertion_process(pairs, rules)

    # Calculate quantities of every char in output pairs with counts
    counts = defaultdict(int)
    for pair, count in pairs.items():
        for char in pair:
            counts[char] += count

    # All chars in the dict are repeated twice,
    # except for the first and last chars in input template
    for char, count in counts.items():
        if char is first_char or char is last_char:
            counts[char] = (count + 1) // 2
        else:
            counts[char] = count // 2

    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()

    input_polymer_template, input_rules_list = data.split('\n\n')
    input_rules = {}
    for pair_rule in input_rules_list.splitlines():
        pair, letter = pair_rule.split(' -> ')
        input_rules[pair] = letter

    part1 = polymerization(input_polymer_template, input_rules, 10)
    part2 = polymerization(input_polymer_template, input_rules, 40)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
