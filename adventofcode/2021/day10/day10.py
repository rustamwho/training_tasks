from statistics import median

LEGAL_PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}
SCORE_TABLE_1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORE_TABLE_2 = {')': 1, ']': 2, '}': 3, '>': 4}


def get_corrupted_and_incomplete_lines(lines):
    """
    Return dicts:
    1) corrupted lines - { <line_index> : <first_wrong_bracket> }
    2) incomplete lines - { <line_index> : <unclosed_brackets_list> }
    """
    corrupted_lines = {}
    incomplete_lines = {}
    for i, line in enumerate(lines):
        unclosed_brackets = []
        for character in line:
            if character in LEGAL_PAIRS:
                unclosed_brackets.append(character)
                continue
            # If character is not close bracket for last open bracket
            if character != LEGAL_PAIRS[unclosed_brackets.pop()]:
                corrupted_lines[i] = character
                break
        # When line is incomplete
        if i not in corrupted_lines:
            incomplete_lines[i] = unclosed_brackets
    return corrupted_lines, incomplete_lines


def calculate_syntax_error_score(lines):
    """ Part 1. Return sum of syntax error scores for all lines. """
    corrupted_lines, _ = get_corrupted_and_incomplete_lines(lines)
    return sum(SCORE_TABLE_1[x] for x in corrupted_lines.values())


def calculate_middle_score(lines):
    """ Part 2. Return middle from all incomplete lines scores. """
    _, incomplete_lines = get_corrupted_and_incomplete_lines(lines)
    score_lines = []
    for unclosed_brackets in incomplete_lines.values():
        score = 0
        # For the correct completion of the sequence, it is necessary to add
        # close brackets in reverse order
        for bracket in reversed(unclosed_brackets):
            score = score * 5 + SCORE_TABLE_2[LEGAL_PAIRS[bracket]]
        score_lines.append(score)
    return median(score_lines)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.read().splitlines()

    part1 = calculate_syntax_error_score(input_lines)
    part2 = calculate_middle_score(input_lines)

    print('Part 1:', part1)
    print('Part 2:', part2)
