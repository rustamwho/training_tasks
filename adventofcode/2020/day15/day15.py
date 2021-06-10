def search_number(numbers, end):
    """
    Вычисление числа на позиции end путем составления всего списка
    Если последнее число произносилось раньше, новое число равно разности
                        последних двух ходов, в которых оно произносилось
    """
    # словарь с номером последнего произношения каждого числа
    last_spoken = {}
    for number in numbers[:-1]:
        last_spoken[number] = numbers.index(number)

    for i in range(len(numbers), end):
        last_number = numbers[i - 1]

        if last_number in last_spoken.keys():
            new_number = i - 1 - last_spoken[last_number]
            numbers.append(new_number)
        else:
            numbers.append(0)

        last_spoken[last_number] = i - 1

    return numbers[-1]


def search_number_update(numbers, end):
    """
    Вычисление числа на позиции end без списка, только с переменными
    По сравнению с прошлой реализацией, дает прирост в 5сек при end=30000000
    """
    last_spoken = {}
    for number in numbers[:-1]:
        last_spoken[number] = numbers.index(number)
    last_number = numbers[-1]

    for i in range(len(numbers), end):

        if last_number in last_spoken.keys():
            new_number = i - 1 - last_spoken[last_number]
        else:
            new_number = 0

        last_spoken[last_number] = i-1
        last_number = new_number

    return last_number


input_numbers = [int(x) for x in '13,16,0,12,15,1'.split(',')]
part_one = search_number(input_numbers, 2020)
input_numbers = [int(x) for x in '13,16,0,12,15,1'.split(',')]
part_two = search_number_update(input_numbers, 30000000)

print(f"Part One: 2020th number is {part_one}\n"
      f"Part Two: 30000000th number is {part_two}")
