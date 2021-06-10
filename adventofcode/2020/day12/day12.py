def read_commands():
    commands = []
    with open('input.txt', 'r') as file:
        for line in file:
            input = line.strip()
            commands.append((input[:1], int(input[1:])))
    distance1 = manhattan_distance(commands)
    distance2 = real_manhattan_distance(commands)
    print(f'Part 1: {distance1}\nPart 2: {distance2}')


def change_direction(cur_direction, command, value):
    """Поворот корабля"""
    directions = ['East', 'South', 'West', 'North']
    if command == 'L':
        index = int(directions.index(cur_direction) - value / 90)
    else:
        index = int(directions.index(cur_direction) + value / 90)
    while index < 0 or index > 3:
        if index > 3:
            index -= 4
        else:
            index += 4
    return directions[index]


def change_waypoint(x, y, command, value):
    """Изменение положения точки относительно корабля"""
    while 0 < value:
        if command == 'L':
            x2 = y
            y = x
            x = -x2
            value -= 90
        else:
            y2 = x
            x = y
            y = -y2
            value -= 90
    return x, y


def manhattan_distance(commands):
    """Выполнение команд для корабля"""
    position = {'x': 0, 'y': 0}
    # направления корабля. Для вычисления позиции при движении вперед
    directions = {'North': [0, 1], 'South': [0, -1], 'East': [1, 0],
                  'West': [-1, 0]}
    direction = 'East'
    for command, value in commands:
        if command == 'N':
            position['y'] += value
        elif command == 'S':
            position['y'] -= value
        elif command == 'E':
            position['x'] += value
        elif command == 'W':
            position['x'] -= value
        elif command == 'L' or command == 'R':
            direction = change_direction(direction, command, value)
        else:
            dx, dy = directions[direction]
            position['x'] += dx * value
            position['y'] += dy * value
    distance = abs(position['x']) + abs(position['y'])
    return distance


def real_manhattan_distance(commands):
    """Выполнение команд с учетом waypoint"""
    ship = {'x': 0, 'y': 0}
    waypoint = {'x': 10, 'y': 1}
    for command, value in commands:
        if command == 'N':
            waypoint['y'] += value
        elif command == 'S':
            waypoint['y'] -= value
        elif command == 'E':
            waypoint['x'] += value
        elif command == 'W':
            waypoint['x'] -= value
        elif command == 'L' or command == 'R':
            waypoint['x'], waypoint['y'] = change_waypoint(waypoint['x'],
                                                           waypoint['y'],
                                                           command, value)
        else:
            ship['x'] += waypoint['x'] * value
            ship['y'] += waypoint['y'] * value
    distance = abs(ship['x']) + abs(ship['y'])
    return distance


read_commands()
