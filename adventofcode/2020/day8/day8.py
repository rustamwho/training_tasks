import copy


def do_command(acc, index, command, value):
    """Выполнение полученной команды и вычисление следующего индекса"""
    if command == 'nop':
        index += 1
    elif command == 'acc':
        acc += int(value)
        index += 1
    elif command == 'jmp':
        index += int(value)
    else:
        print('Unknown command!')
    return acc, index


def change_nop_jmp(command):
    """Замена nop на jmp и наоборот"""
    if command == 'nop':
        return 'jmp'
    return 'nop'


def do_program(commands):
    """
    Выполнить код программы.

    Возвращает acc и False, если какая-либо команда выполняется повторно
    Возвращает acc и True, если программа завершила работу правильно
    """
    index = 0
    # список выполненных команд
    executed_indexes = []
    acc = 0
    while index not in executed_indexes and index < len(commands):
        command, value = commands[index]
        executed_indexes.append(index)
        acc, index = do_command(acc, index, command, value)
    if index in executed_indexes:
        return acc, False
    return acc, True


def game_console():
    """Первая часть задачи"""
    commands = []
    with open('input.txt', 'r') as file:
        for line in file:
            command, value = line.strip().split()
            commands.append([command, value])
    acc, _ = do_program(commands)
    return acc, commands


def game_console_part_two(commands):
    """Вторая часть задачи, поиск неправильной комманды"""
    for i in range(0, len(commands)):
        com, val = commands[i]
        if com != 'jmp' and com != 'nop':
            continue
        # новая копия программы
        new_commands = copy.deepcopy(commands)
        # замена команды в копии программы
        new_commands[i][0] = change_nop_jmp(com)
        # выполнение измененной копии программы
        acc, result = do_program(new_commands)
        if result is True:
            return acc, i, new_commands
    return "Error"


part_one_acc, all_commands = game_console()
part_two_acc, changed_index, new_all_commands = game_console_part_two(
    all_commands)
print(f"Part one acc: {part_one_acc}\nPart two acc: {part_two_acc}\n"
      f"Changed command: index {changed_index} - {all_commands[changed_index]} "
      f"to {new_all_commands[changed_index]}")
