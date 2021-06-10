from itertools import product


def do_program(commands):
    """Выполнение команд программы для первой части"""
    memory = {}
    for command in commands:
        if type(command) is str:
            mask = command
        else:
            adress, value = command
            # перевод в двоичную систему с 36 символами
            value = format(value, '036b')
            new_value = list(value)
            for i, bit in enumerate(mask):
                # если в маске не Х, в новое число вписывается этот бит маски
                if bit != 'X':
                    new_value[i] = bit
            memory[adress] = int(''.join(new_value), 2)
    return memory


def do_update_program(commands):
    """
    Выполнение команд при работе с перебором адресов
    Если в маске 0 - бит адреса не меняется
    Если в маске 1 - бит адреса меняется на 1
    Если в маске Х - бит адреса может быть 0 и 1
    """
    memory = {}
    for command in commands:
        if type(command) is str:
            mask = command
        else:
            adress, value = command
            adress = format(adress, '036b')
            preadress = ''
            adresses = []
            for i, bit in enumerate(mask):
                if bit == '0':
                    preadress += adress[i]
                elif bit == '1':
                    preadress += '1'
                else:
                    preadress += 'X'
            # таплы комбинаций из 0 и 1, длиной в количество Х в преадресе
            zeroones = product(('0', '1'), repeat=preadress.count('X'))
            for combination in zeroones:
                new_adress = ''
                i = 0
                for bit in preadress:
                    if bit != 'X':
                        new_adress += bit
                    else:
                        new_adress += combination[i]
                        i += 1
                #  список возможных адресов
                adresses.append(new_adress)
            # запись в память числа по всем адресам
            for ad in adresses:
                memory[ad] = value
    return memory


def read_commands():
    commands = []
    with open('input.txt', 'r') as file:
        for line in file:
            if 'mask' in line:
                mask = line.strip().split(' = ')[1]
                commands.append(mask)
            else:
                adress = int(line.split('] = ')[0].split('[')[1])
                value = int(line.strip().split(' = ')[1])
                commands.append((adress, value))
    memory = do_program(commands)
    sum_memory = sum(memory.values())
    memory2 = do_update_program(commands)
    sum_memory2 = sum(memory2.values())
    print(f"Sum of all values in memory:\nPart 1: {sum_memory}\n"
          f"Part 2: {sum_memory2}")


read_commands()
