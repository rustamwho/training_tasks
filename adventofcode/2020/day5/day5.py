def calculate_row(binary):
    rows = [i for i in range(0, 128)]
    for bin in binary:
        if bin == 'F':
            del rows[int(len(rows) / 2):]
        else:
            del rows[:int(len(rows) / 2)]
    return rows[0]


def calculate_column(binary):
    columns = [0, 1, 2, 3, 4, 5, 6, 7]
    for bin in binary:
        if bin == 'L':
            del columns[int(len(columns) / 2):]
        else:
            del columns[:int(len(columns) / 2)]
    return columns[0]


def calculate_id(binary_seat):
    row = calculate_row(binary_seat[:7])
    column = calculate_column(binary_seat[7:])
    id = row * 8 + column
    print(f"{binary_seat}\nRow: {row}\nColumn: {column}\nID: {id}")
    return id


busy_seats = set()


def search_max_id():
    max_id = 0
    with open("input.txt", "r") as file:
        for binary_seat in file:
            id = calculate_id(binary_seat.strip())
            busy_seats.add(id)
            if max_id < id:
                max_id = id
    return max_id


def search_my_seat():
    all_seats = set(range(min(busy_seats), max(busy_seats) + 1))
    my_seat = all_seats.difference(busy_seats)
    return my_seat


print(f"\n\nMAX ID: {search_max_id()}")
print(f"MY_SEAT: {[i for i in search_my_seat()][0]}")
