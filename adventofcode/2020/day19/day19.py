def do_rule(number_of_rule, rules, main_options):
    possible = []
    count = 0
    rule = rules[number_of_rule]
    if type(rule) is not list:
        return rule
    if len(rule) > 1 and type(rule[0]) is tuple:
        for possible_option in rule:
            if len(possible_option) == 1:
                possible.append(
                    do_rule(possible_option[0], rules, main_options))
                continue
            num1, num2 = possible_option
            if num1 in main_options.keys():
                op1 = main_options[num1]
            else:
                count += 1
                op1 = do_rule(num1, rules, main_options)
                main_options[num1] = op1
            if num2 in main_options.keys():
                op2 = main_options[num2]
            else:
                count += 1
                op2 = do_rule(num2, rules, main_options)
                main_options[num2] = op2
            for o1 in op1:
                for o2 in op2:
                    possible.append(o1 + o2)
    else:
        for number in rule:
            help = []
            if number in main_options.keys():
                options = main_options[number]
            else:
                count += 1
                options = do_rule(number, rules, main_options)
                main_options[number] = options
            if not possible:
                possible.append(options)
            else:
                if len(possible) == 1 and type(possible[0]) is list:
                    while type(possible[0]) is list:
                        possible = possible[0]
                for pos1 in possible:
                    for pos2 in options:
                        help.append(pos1 + pos2)
                possible = help
    return possible


def calculate_possible_options(rules):
    # словарь со всеми вариантами сообщений, удовлетворяющих правилу
    options = {}
    for name, rule in rules.items():
        options[name] = do_rule(name, rules, options)
    # очень медленная проверка на наличие сообщения в списке возможных
    count = len([x for x in input_messages if x in options[0]])
    return count, options


def after_update_rules(possible_options, messages):
    """
    Проверка каждого сообщения на валидность, учитывая обновленные правила
    8: 42 | 42 8            -   8: повторение 42
    11: 42 31 | 42 11 31    -   11: 42 31 | 42 (42 (42 (...) 31) 31) 31
    0:  8 11    - 42 (42 31)    - 42(n раз) 31(<n раз)
    """
    len42 = len(possible_options[42][0])
    len31 = len(possible_options[31][0])
    count = 0
    for message in messages:
        count42, count31 = 0, 0
        # часть сообщения, удовл. правилу, удаляется
        while len(message) > len31:
            if message[:len42] not in possible_opt[42]:
                break
            count42 += 1
            message = message[len42:]
        while len(message) >= len31:
            if message[:len31] not in possible_opt[31]:
                break
            count31 += 1
            message = message[len31:]
        if len(message) == 0 and 0 < count31 < count42:
            count += 1
    return count


def read():
    rules = {}
    messages = []
    with open('input.txt', 'r') as file:
        data = file.read().split('\n\n')
    for rule in data[0].split('\n'):
        name_rule, values = rule.split(': ')
        if '|' in values:
            rules[int(name_rule)] = [tuple(int(x) for x in y.split(' ')) for y
                                     in values.split(' | ')]
        else:
            if '"a"' not in values and '"b"' not in values:
                rules[int(name_rule)] = [int(x) for x in values.split(' ')]
            else:
                rules[int(name_rule)] = values.replace('"', '')
    for message in data[1].split('\n'):
        messages.append(message)
    return rules, messages


input_rules, input_messages = read()
count1, possible_opt = calculate_possible_options(input_rules)
count2 = after_update_rules(possible_opt, input_messages)

print(f"Part 1:\t{count1}\nPart 2:\t{count2}")
