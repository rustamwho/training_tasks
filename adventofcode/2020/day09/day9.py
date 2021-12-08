def check_next_number(encrypted, index):
    """
    Проверка следующего числа в списке
    Оно должно быть суммой любых двух чисел из преамбулы
    Длина преамбулы - 25 чисел
    """
    preamble = encrypted[index - 25:index]
    next_number = encrypted[index]
    for first_number in preamble[:-1]:
        for second_number in preamble[preamble.index(first_number) + 1:]:
            result = first_number + second_number
            if result == next_number:
                return True
    return False


def search_list_numbers(encrypted_data, result_number):
    """
    Поиск подряд идущих чисел, сумма которых равна ошибочному числу
    """
    for i in range(0, len(encrypted_data)):
        sum_numbers = encrypted_data[i]
        j = 1
        while sum_numbers < result_number:
            sum_numbers += encrypted_data[i + j]
            j += 1
        if sum_numbers != result_number:
            continue
        list_numbers = encrypted_data[i:i + j]
        return list_numbers


def hack_xmas():
    """Поиск первого неправильного числа"""
    encrypted_data = []
    with open('input.txt', 'r') as file:
        for line in file:
            encrypted_data.append(int(line.strip()))
    index = 24
    correct_next_number = True
    while correct_next_number and index < len(encrypted_data) - 1:
        index += 1
        correct_next_number = check_next_number(encrypted_data, index)
    return encrypted_data, index


def hack_xmas_part_two(encrypted_data, index):
    """
    Поиск слабости шифрования
    Она равна сумме мин и макс чисел из списка
    """
    incorrect = encrypted_data[index]
    found_list = search_list_numbers(encrypted_data, incorrect)
    sum_min_max = min(found_list) + max(found_list)
    return found_list, sum_min_max


data, index = hack_xmas()
incorrect_number = data[index]
xmas_list, encryption_weakness = hack_xmas_part_two(data, index)
print(f"First incorrect number: {incorrect_number}\n"
      f"Encryption weakness: {encryption_weakness}\n"
      f"Encryption weakness list: {xmas_list}")
