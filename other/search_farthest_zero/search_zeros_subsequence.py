"""
Виталий тщательно следит за соблюдением социальной дистанции поэтому в любом
общественном месте он старается выбрать места подальше от других посетителей.
Сейчас он выбирает места на представлении в театре. Ему принципипально сидеть
на первом ряду. Так что можно считать что в театре только один ряд.

Информация о местах записана строкой: если на. i-ом месте в строке 0, то i-ое
место слева свободно, если стоит 1 -- значит занято. Необходимо указать номер
сидения, которое необходимо купить Виталию, чтоб минимальное расстояние до
соседа было максимальным.

Выведите номер сидения, считая что нумерация кресел идет с единицы.
"""

import random
import re


def get_best_seat(sequence: str) -> int:
    print(f'Последовательность: {sequence}')
    # Поиск самой длинной подпоследовательности нулей
    all_subsequences = re.findall(r'[0]+', sequence)
    if not all_subsequences:
        return 0
    max_zeros_subsequence = max(all_subsequences, key=len)
    print(f'Максимальная последовательность нулей:\n'
          f'Длина = {len(max_zeros_subsequence)}\t'
          f'Последовательность:{max_zeros_subsequence}')

    # Индексы начала и конца найденной подпоследовательности
    position_of_subsequence = re.search(max_zeros_subsequence, sequence)
    start_index = position_of_subsequence.start()
    end_index = position_of_subsequence.end()
    nearest_neighbor = round((end_index - start_index) / 2) - 1
    print(f'Индекс начала: {start_index}\t'
          f'Индекс конца: {end_index}')

    # Строка начинается или заканчивается нулями
    seq_start = re.match(r'[0]+', sequence)
    seq_end = re.match(r'[0]+', sequence[::-1])

    if start_index == 0:
        return 1
    elif end_index == len(sequence):
        return end_index
    else:
        result = (start_index + end_index) // 2 + 1

    # В концах ряда количество нулей меньше, но до первого соседа дальше
    if seq_start and seq_start.end() - seq_start.start() > nearest_neighbor:
        result = 1
    if seq_end and seq_end.end() - seq_end.start() > nearest_neighbor:
        result = len(sequence)

    return result


def test():
    assert get_best_seat('0001000010') in [1]
    assert get_best_seat('0100001000') in [10]
    assert get_best_seat('00010000010') in [1, 7]
    assert get_best_seat('01000001000') in [5, 11]
    assert get_best_seat('000100000010') in [1, 7, 8]
    assert get_best_seat('010000001000') in [5, 6, 12]
    assert get_best_seat('000100100') in [1]
    assert get_best_seat('001001000') in [9]
    assert get_best_seat('0000100100000') in [13]
    assert get_best_seat('000100100000') in [12]
    assert get_best_seat('00100100000') in [11]
    assert get_best_seat('000010010000') in [1, 12]
    assert get_best_seat('00001001000') in [1]
    assert get_best_seat('0000100100') in [1]
    assert get_best_seat('00000')
    assert get_best_seat('11111') == 0
    assert get_best_seat('0111') == 1
    assert get_best_seat('11011') == 3
    assert get_best_seat('1110') == 4


if __name__ == '__main__':
    input_seq = ''.join(str(random.randint(0, 1)) for _ in range(0, 2000))
    best_seat = get_best_seat(input_seq)
    print(f'Лучшее место для Виталия: {best_seat}')
    test()
