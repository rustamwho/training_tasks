def get_result(cash: list[int], s: int) -> int:
    while s >= 3:
        minimum_index = cash.index(min(cash))
        cash[minimum_index] += 3
        s -= 3
    if s > 0:
        minimum_index = cash.index(min(cash))
        cash[minimum_index] += s
    max_prize = max(cash)
    result = sum(prize < max_prize for prize in cash)
    return result


print(get_result([57, 45, 54, 48, 23, 46, 89, 67, 25, 78, 59, 71], 611))
