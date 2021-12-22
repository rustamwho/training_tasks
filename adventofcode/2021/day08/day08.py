import re
from collections import Counter

DIGITS_IN_LETTERS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}


def get_count_1478(four_digits: list):
    """ Part 1. Return count of 1,4,7,8 numbers in output values."""
    regex = r'\b\w{2}\b|\b\w{4}\b|\b\w{3}\b|\b\w{7}\b'
    matched = re.findall(regex, ' '.join(four_digits))
    return len(matched)


def get_one_letter(pattern: str | tuple, exclude_letters: tuple) -> str:
    """
    Return one letter from <pattern> that is not in <exclude_letters>.
    """
    return [x for x in pattern if x not in exclude_letters][0]


def get_dict_for_translate(patterns: str):
    """
    Return dict = {<letter_in_source_signals> : <letter_in_this_patterns>}.
    For translate DIGITS_IN_LETTERS to this four-digit seven-segment displays.
    """
    # Calculate count of each symbols in patterns
    counter = Counter(patterns)
    del counter[' ']
    translate_letters = {x: None for x in 'abcdefg'}

    for letter, count in dict(counter).items():
        if count == 4:
            translate_letters['e'] = letter
        if count == 6:
            translate_letters['b'] = letter
        if count == 9:
            translate_letters['f'] = letter

    patterns = sorted(patterns.split(' '), key=len)

    # Translate letter for c based on 1 (cf)
    translate_letters['c'] = get_one_letter(
        patterns[0],
        exclude_letters=(translate_letters['f'])
    )
    # Translate letter for a based on 7 (acf)
    translate_letters['a'] = get_one_letter(
        patterns[1],
        exclude_letters=(translate_letters['f'], translate_letters['c'])
    )
    # Translate letter for d based on 4 (bcdf)
    translate_letters['d'] = get_one_letter(
        patterns[2],
        (
            translate_letters['b'], translate_letters['c'],
            translate_letters['f'])
    )
    # Translate letter for g - last letter
    translate_letters['g'] = get_one_letter(
        tuple(translate_letters.keys()),
        tuple(translate_letters.values())
    )
    return translate_letters


def get_number(patterns: str, digits: str) -> int:
    """ Return output signals in int for this four-digit displays. """
    translate_letters = get_dict_for_translate(patterns)
    new_digits_in_letters = {}
    for digit, letters in DIGITS_IN_LETTERS.items():
        translated = ''.join(translate_letters[x] for x in letters)
        new_digits_in_letters[digit] = translated
    result = ''
    for encrypted_digit in digits.split(' '):
        for digit, letters in new_digits_in_letters.items():
            if (len(encrypted_digit) == len(letters) and
                    all(x in letters for x in encrypted_digit)):
                result += str(digit)
                break
    return int(result)


def get_sum_all_numbers(unique_signal_patterns: list, four_digits: list):
    """ Part 2. Return sum of all output numbers. """
    result = 0
    for patterns, digits in zip(unique_signal_patterns, four_digits):
        result += get_number(patterns, digits)
    return result


if __name__ == '__main__':
    input_unique_signal_patterns = []
    input_four_digit = []
    with open('input.txt', 'r') as file:
        for line in file.read().split('\n'):
            first, second = line.split(' | ')
            input_unique_signal_patterns.append(first)
            input_four_digit.append(second)

    part1 = get_count_1478(input_four_digit)
    part2 = get_sum_all_numbers(input_unique_signal_patterns, input_four_digit)
    print('Part 1:', part1)
    print('Part 2:', part2)
