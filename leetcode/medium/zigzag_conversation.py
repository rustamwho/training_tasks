def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    result = [''] * num_rows
    index, step = 0, 1

    # Move from zero row to num_rows-1 row
    # then back to zero and so to the end
    for x in s:
        result[index] += x
        if index == 0:
            step = 1
        elif index == num_rows - 1:
            step = -1
        index += step

    return ''.join(result)


print(convert('PAYPALISHIRING', 3))
