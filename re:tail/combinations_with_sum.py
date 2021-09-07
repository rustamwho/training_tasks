"""
Для доставки посылок различной массы планируется использовать дрон.
Масса i-ой посылки равна parcels[i].  При этом, по летным правилам,
установленным компанией, для безопасности жителей дрон за один раз может
перевозить только две посылки, масса которых в сумме строго равна m.
Необходимо найти максимальное количество рейсов, которые дрон сможет
сделать с учетом условий.

На входе:

parcels - массив чисел ненулевой длины - массы посылок, кг
m - число, m > 0 - грузоподъемность дрона, кг
На выходе: число - максимальное количество доставок

Примечание:

дрон доставляет только по две посылки, с одной посылкой он не полетит
масса посылок в сумме должна быть строго равна грузоподъемности m

Пример:

parcels = [2,4,3,6,1]
m = 5
get_result(parcels, m) -> 2
// дрон сможет совершить две доставки по 5 кг: [2, 3] и [4, 1]
"""
from itertools import combinations


def get_sum(numbers: list, m):
    new_numbers = numbers.copy()
    for subset in combinations(new_numbers, 2):
        if sum(subset) == m:
            new_numbers.remove(subset[0])
            new_numbers.remove(subset[1])
            return new_numbers
    return new_numbers


def get_result(parcels, m):
    count = 0
    while True:
        new_parcels = get_sum(parcels, m)
        if new_parcels == parcels:
            break
        count += 1
        parcels = new_parcels.copy()
    return count


print(get_result([2, 4, 3, 6, 1], 5))
print(get_result([1, 2, 1, 5, 1, 3, 5, 2, 5, 5], 6))
