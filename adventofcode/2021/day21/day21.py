from dataclasses import dataclass
from collections import defaultdict
from itertools import product
import functools


@dataclass
class Player:
    position: int
    score: int

    def is_win(self):
        return self.score >= 1000


def cube_generator(count_sides: int):
    """ Return next 3 values. """
    current_roll = 1
    while True:
        rolls = []
        for _ in range(3):
            if current_roll > count_sides:
                current_roll = 1
            rolls.append(current_roll)
            current_roll += 1
        yield rolls


def play_simple_game(players) -> int:
    """
    Part 1. Simulate the training game.
    Return multiply the score of the losing player by the number of
    times the die was rolled during the game.
    """
    count_rolls = 0
    current: int = 0
    cube = cube_generator(100)
    while not players[0].is_win() and not players[1].is_win():
        new_pos = players[current].position + sum(next(cube))
        new_pos = new_pos % 10 if new_pos % 10 != 0 else 10
        players[current].position = new_pos
        players[current].score += new_pos
        current = 1 - current
        count_rolls += 3
    return players[current].score * count_rolls


@functools.lru_cache(maxsize=None)
def play_true_game(positions, scores, current):
    """ Part 2. Return count of win universe for each player. """
    winners = defaultdict(int)

    new_positions = list(positions)
    new_scores = list(scores)

    for rolls in product((1, 2, 3), repeat=3):
        new_positions[current] = (positions[current] + sum(rolls) - 1) % 10 + 1
        new_scores[current] = scores[current] + new_positions[current]

        if new_scores[current] < 21:
            w1, w2 = play_true_game(
                tuple(new_positions),
                tuple(new_scores),
                1 - current
            )
            winners[0] += w1
            winners[1] += w2
        else:
            winners[current] += 1

    return winners[0], winners[1]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        start_points = tuple(int(line.split(' ')[-1])
                             for line in file.read().splitlines())

    players_input = [Player(x, 0) for x in start_points]

    part1 = play_simple_game(players_input)
    print(f'Part 1: {part1}')

    part2 = max(play_true_game(start_points, (0, 0), 0))
    print(f'Part 2: {part2}')
