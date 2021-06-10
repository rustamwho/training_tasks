def move100(cups):
    """100 ходов"""
    current_cup = cups[0]
    for _ in range(100):
        current_index = cups.index(current_cup)
        pick_up = cups[current_index + 1: current_index + 4]
        i = 0
        while len(pick_up) != 3:
            pick_up.append(cups[i])
            i += 1
        for cup in pick_up:
            cups.remove(cup)

        destination = current_cup - 1
        if destination < min(cups):
            destination = max(cups)
        if destination in pick_up:
            while destination not in cups:
                destination -= 1
                if destination < min(cups):
                    destination = max(cups)
                    break

        index_put = cups.index(destination) + 1
        for _ in range(3):
            cups.insert(index_put, pick_up.pop())

        current_index = cups.index(current_cup) + 1
        if current_index >= len(cups):
            current_index = current_index - len(cups)
        current_cup = cups[current_index]

    # Составление строки с цифрами чашек начиная с 1
    str_cups = ''
    one_cup_index = cups.index(1)
    index = one_cup_index + 1
    while index != one_cup_index:
        str_cups += str(cups[index])
        index += 1
        if index >= len(cups):
            index = index - len(cups)

    return str_cups


def move_millions(input_cups):
    """10 миллионов ходов с миллионом чашек"""
    # {индекс чашки : индекс следующей}
    cups = {}
    for index, cup in enumerate(input_cups[:-1], 1):
        cups[cup] = input_cups[index]
    cups[input_cups[-1]] = max(cups) + 1
    for i in range(len(cups) + 1, 1000000):
        cups[i] = i + 1
    cups[1000000] = input_cups[0]

    current_cup = input_cups[0]
    for _ in range(10000000):
        pick_up = []
        cup_to_pick = current_cup
        for _ in range(3):
            cup_to_pick = cups[cup_to_pick]
            pick_up.append(cup_to_pick)

        cups[current_cup] = cups[cup_to_pick]

        destination = current_cup - 1
        # для случаев, когда целевая чашка наименьшая из не поднятых
        min_cups = [x for x in range(1, 4) if x not in pick_up]
        max_cups = [x for x in range(999997, 1000001) if
                      x not in pick_up]
        if destination < min_cups[0]:
            destination = max_cups[-1]
        elif destination in pick_up:
            while True:
                destination -= 1
                if destination not in pick_up:
                    break
                if destination < min_cups[0]:
                    destination = max_cups[-1]
                    break

        # чашки кладутся на новые места
        dist = cups[destination]
        cups[destination] = pick_up[0]
        cups[pick_up[1]] = pick_up[2]
        cups[pick_up[2]] = dist
        # берется следующая чашка
        current_cup = cups[current_cup]

    next_one_cup = cups[1]
    mul = next_one_cup * cups[next_one_cup]
    return mul


def read():
    with open('input.txt', 'r') as file:
        cups = [int(x) for x in file.read().strip()]

    return cups


input_cups = read()
input_cups_copy = input_cups.copy()

cups_str = move100(input_cups_copy)
multiply = move_millions(input_cups)

print(f"Part 1:\t{cups_str}\nPart 2:\t{multiply}")
