import itertools

expenses = set(
    int(line)
    for line
    in open('input.txt')
)

for e1, e2 in itertools.combinations(expenses, 2):
    if (e3 := 2020 - e1 - e2) in expenses:
        print(e1 * e2 * e3)
        break