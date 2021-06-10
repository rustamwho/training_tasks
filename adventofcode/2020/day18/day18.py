def sum(a, b):
    return a + b


def mul(a, b):
    return a * b


def evaluate(line, part):
    result = 1
    operation = mul
    while line:
        value = line.pop()
        if value == '(':
            result = operation(result, evaluate(line, part))
        elif value == ')':
            return result
        elif value == '+':
            operation = sum
        elif value == '*':
            if part == 1:
                operation = mul
            else:
                result = mul(result, evaluate(line, part))
                return result
        else:
            result = operation(result, int(value))
    return result


def read():
    input_data = []
    with open('input.txt', 'r') as file:
        for line in file:
            input_data.append(list(line.strip().replace(' ', '')))
    return input_data


homework = read()
result1, result2 = 0, 0
for l in homework:
    # списки переворачиваются для работы с последними элементами
    result1 += evaluate(list(reversed(l)), 1)
    result2 += evaluate(list(reversed(l)), 2)

print(f"Part 1: {result1}\nPart 2: {result2}")
