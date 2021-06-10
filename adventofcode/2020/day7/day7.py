def sum_all_bags(bags, color):
    """Рекурсивное вычисление количества всех вложенных сумок"""
    sum = 0
    for bag in bags:
        bag_color, inside_bags = bag
        if bag_color == color:
            for col, amount in inside_bags.items():
                sum += amount + amount * sum_all_bags(bags, col)
    return sum


def bag_in_bag(bags, colors):
    """Поиск новых цветов сумок, которые содержат нужные цвета"""
    new_colors = []
    for bag in bags:
        color_bag, inside_bag_color = bag
        new_colors += [color_bag for x in inside_bag_color.keys() if
                       x in colors]
    return new_colors


def sum_bags(bags):
    """Поиск сумок с нужным цветом"""
    colors = []
    for i in bags:
        color_bag, inside_bag_color = i
        if "shiny gold" in inside_bag_color.keys():
            colors.append(color_bag)
    new_colors = bag_in_bag(bags, colors)
    while new_colors:
        colors += new_colors
        new_colors = bag_in_bag(bags, new_colors)
    return colors


def new_bag(line):
    """Выделение цвета сумки и вложенных сумок"""
    color = line[:line.find('bag') - 1]
    inside_bags = line[line.find('contain') + 8:]
    inside_colors = {}
    for bag in inside_bags.split(', '):
        if bag[0].isdigit():
            amount = int(bag[0])
            in_color = bag[2:bag.find('bag') - 1]
            inside_colors[in_color] = amount
        else:
            continue
    return color, inside_colors


def color_bags():
    bags = []
    with open("input.txt", "r") as file:
        for line in file:
            bag_color, inside_colors = new_bag(line)
            bags.append((bag_color, inside_colors))
    true_bags = set(sum_bags(bags))
    amount_bags = sum_all_bags(bags, 'shiny gold')
    return len(true_bags), amount_bags


part_one, part_two = color_bags()
print(f'Part One: {part_one}\nPart Two: {part_two}')
