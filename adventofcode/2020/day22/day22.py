from copy import deepcopy


def round(first_player_cards, second_player_cards):
    """НЕрекурсивный раунд (сравнивание очередных карт игроков)"""
    card_first = first_player_cards.pop(0)
    card_second = second_player_cards.pop(0)
    if card_first > card_second:
        first_player_cards.extend([card_first, card_second])
        return 1
    second_player_cards.extend([card_second, card_first])
    return 2


def scoring(players, first=False):
    """Подсчет очков победившего игрока"""
    # для случая, когда игрок 1 выиграл до конца игры
    if first:
        winner_score = sum((i) * x for i, x in enumerate(players[1][::-1], 1))
        return 1, winner_score
    winner_name = [i for i, x in players.items() if x][0]
    winner_deck = [x for _, x in players.items() if x][0]
    winner_score = sum((i) * x for i, x in enumerate(winner_deck[::-1], 1))
    return winner_name, winner_score


def play_game(players):
    """Обычная игра"""
    rounds_winner = []

    while players[1] and players[2]:
        rounds_winner.append(round(players[1], players[2]))

    winner_name, winner_score = scoring(players)
    return winner_name, winner_score, len(rounds_winner)


def recursive_game(players, rounds_count):
    """Рекурсивная версия игры"""
    previous_round = set()
    while players[1] and players[2]:
        rounds_count += 1
        # если карты полностью совпали с предыдущим раундом
        if (tuple(players[1]), tuple(players[2])) in previous_round:
            # выигрывает игрок 1
            players[1].extend([players[1].pop(0), players[2].pop(0)])
            winner_name, winner_score = scoring(players, first=True)
            return winner_name, winner_score, rounds_count

        previous_round.add((tuple(players[1]), tuple(players[2])))

        if len(players[1]) - 1 >= players[1][0] and \
                len(players[2]) - 1 >= players[2][0]:

            first_card, second_card = players[1].pop(0), players[2].pop(0)
            sub_players = {1: players[1][:first_card].copy(),
                           2: players[2][:second_card].copy()}
            winner, _, rounds_count = recursive_game(sub_players, rounds_count)

            if winner == 1:
                players[1].extend([first_card, second_card])
            else:
                players[2].extend([second_card, first_card])

        else:
            round(players[1], players[2])

    winner_name, winner_score = scoring(players)
    return winner_name, winner_score, rounds_count


def read():
    # {номер игрока: [карты игрока]}
    players = {}
    with open('input.txt', 'r') as file:
        data = file.read()
    for i, player in enumerate(data.split('\n\n')):
        _, cards = player.split(':')
        players[i + 1] = [int(x) for x in cards.strip().split()]
    return players


players_dict = read()
# PART 1
winner, score, count_rounds = play_game(deepcopy(players_dict))
print(f"Combat:\n"
      f"{winner}'s player won with a score of "
      f"{score} over {count_rounds} rounds")

# PART 2
winner, score, count_rounds = recursive_game(players_dict, 0)
print(f"\nRecursive Combat:\n"
      f"{winner}'s player won with a score of "
      f"{score} over {count_rounds} rounds and sub-rounds")
