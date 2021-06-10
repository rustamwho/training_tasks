import copy


def check_value(value):
    """Возвращает список полей, которым может соответствовать число"""
    valid_fields = []
    for n_rule, v_rule in rules.items():
        for start, end in v_rule:
            if start <= value <= end:
                valid_fields.append(n_rule)
    return valid_fields


def search_invalid_numbers():
    """Поиск значений, недопустимых для всех полей"""
    invalid_nums = []
    for number in [x for y in nearby_tickets for x in y]:
        if not check_value(number):
            invalid_nums.append(number)
    return sum(invalid_nums)


def determine_fields():
    """Определение полей"""
    help_nearby_tickets = copy.deepcopy(nearby_tickets)
    # удаление неправильных билетов
    # если хотя бы одно значение не подходит ни к одному полю
    for ticket in help_nearby_tickets:
        for number in ticket:
            if not check_value(number):
                nearby_tickets.remove(ticket)
                break

    # список билетов со словарями для каждого
    # словарь - индекс числа в билете : список его потенциальных полей
    tickets_fields = []
    for ticket in nearby_tickets:
        fields = {i: check_value(value) for i, value in enumerate(ticket)}
        tickets_fields.append(fields)

    # получение уникального возможного поля для позиций в билете путем
    # пересечения списка возможных полей для каждого числа билета
    # с аналогичным списком числа на той же позиции другого билета
    result = []
    # проход по всем 19 индексам каждого билета
    for i in tickets_fields[0].keys():
        # список возможных полей для индекса i первого билета
        field = tickets_fields[0][i]
        # пересечение со списками возможных полей всех билетов для индекса i
        for ticket in tickets_fields:
            field = list(set(field) & set(ticket[i]))
        result.append(field)

    # обнаружение позиции, которая удовлетворяет только одному полю
    # и удаление этого поля из всех остальных списков
    # до тех пор, пока для всех позиций не останется свое уникальное поле
    while [x for x in result if len(x) > 1]:
        for field in result:
            if len(field) == 1:
                for i in result:
                    if len(i) == 1:
                        continue
                    if field[0] in i:
                        i.remove(field[0])

    # список индексов нужных полей в билете
    indices = [result.index(x) for x in result if 'departure' in x[0]]

    multiply_values = 1
    for index in indices:
        multiply_values *= my_ticket[index]

    return multiply_values, result


with open('input.txt', 'r') as file:
    input_data = file.read().split('\n\n')

# словарь правил
rules = {}
# для каждого правила указываются начальные и конечные значения
for rule in input_data[0].split('\n'):
    name_rule, value_rule = rule.split(': ')
    values = []
    for val in value_rule.split(' or '):
        values.append(tuple([int(x) for x in val.split('-')]))
    rules[name_rule] = values

my_ticket = [int(x) for x in input_data[1].split('\n')[1].split(',')]

nearby_tickets = []
for tick in input_data[2].split('\n')[1:]:
    nearby_tickets.append(tuple([int(x) for x in tick.split(',')]))

sum_numbers = search_invalid_numbers()
mul_numbers, fields = determine_fields()
fields = [x[0] for x in fields]
print(
    f"Order the fields: {fields}\nPart 1: SUM invalid numbers {sum_numbers}\n"
    f"Part 2: MUL six fields with 'departure' {mul_numbers}")
