import copy


def how_seat(matrix, row, column):
    """Возвращает 1, если место занято и 0, если свободно"""
    seat = matrix[row][column]
    if seat == '#':
        return 1
    return 0


def count_occupied_adjacent(matrix, row, column):
    """Подсчет количества занятых смежных мест"""
    count = 0
    for i in (row - 1, row, row + 1):
        for j in (column - 1, column, column + 1):
            if (i == row and j == column) or i < 0 or j < 0 or i >= len(
                    matrix) or j >= len(matrix[0]):
                continue
            count += how_seat(matrix, i, j)
    return count


def count_occupied_firsts_seats(matrix, row, column):
    """Подсчет количества занятых первых увиденных мест по 8 направлениям"""
    count = 0
    deltas = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
              [1, 1], [1, 0], [1, -1], [0, -1]]
    for dx, dy in deltas:
        x = row + dx
        y = column + dy
        if x < 0 or y < 0 or x >= len(
                matrix) or y >= len(matrix[0]):
            continue
        while matrix[x][y] == '.':
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= len(
                    matrix) or y >= len(matrix[0]):
                x -= dx
                y -= dy
                break
        count += how_seat(matrix, x, y)
    return count


def do_rules(matrix):
    """Выполнение правил первой части"""
    new_matrix = copy.deepcopy(matrix)
    modified = False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            count_adjacent = count_occupied_adjacent(matrix, i, j)
            if matrix[i][j] == 'L' and count_adjacent == 0:
                new_matrix[i][j] = '#'
                modified = True
                continue
            if matrix[i][j] == '#' and count_adjacent >= 4:
                new_matrix[i][j] = 'L'
                modified = True
    return new_matrix, modified


def do_new_rules(matrix):
    """Выполнение правил второй части"""
    new_matrix = copy.deepcopy(matrix)
    modified = False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            count_adjacent = count_occupied_firsts_seats(matrix, i, j)
            if matrix[i][j] == 'L' and count_adjacent == 0:
                new_matrix[i][j] = '#'
                modified = True
                continue
            if matrix[i][j] == '#' and count_adjacent >= 5:
                new_matrix[i][j] = 'L'
                modified = True
    return new_matrix, modified


def ferry_seats():
    seats_matrix = []
    with open("input.txt", 'r') as file:
        for line in file:
            seats_matrix.append(list(line.strip()))
    modified = True
    new_seats_matrix = copy.deepcopy(seats_matrix)
    while modified:
        new_seats_matrix, modified = do_rules(new_seats_matrix)
    # количество занятых мест
    count1 = sum(row.count('#') for row in new_seats_matrix)
    modified = True
    while modified:
        seats_matrix, modified = do_new_rules(seats_matrix)
    count2 = sum(row.count('#') for row in seats_matrix)
    print(f"Part 1: {count1} occupied seats\nPart 2: {count2} occupied seats")


ferry_seats()
