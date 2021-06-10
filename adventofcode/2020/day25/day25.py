def find_loop(public):
    """Количество циклов"""
    count, value = 0, 1
    while value != public:
        count += 1
        value = value * 7 % 20201227
    return count


def read():
    with open('input.txt', 'r') as file:
        card, door = map(int, file.read().splitlines())
    return card, door


public_card, public_door = read()
card_loop = find_loop(public_card)

encryption_key = pow(public_door, card_loop, 20201227)
print(f"Encryption Key:\t{encryption_key}")
