"""
Для рекламы продукта было решено использовать блогеров, однако денег на рекламу
выделили ограниченное количество. Поэтому для каждого блогера в массиве nums
написали числовое значение - стоимость покупки рекламы у него. Стоимость может
быть и отрицательной, значит блогер еще и доплатит нам за рекламу.
Рекламу нужно заказать ровно у трёх блогеров. При этом сумма их значений должна
быть наиболее близкой к целевому значению target. На выходе нужно получить
сумму значений стоимости у выбранных блогеров.

На входе:

nums - массив чисел, определяющих стоимость рекламы каждого блогера
target - целевое значение
На выходе: число - сумма трех чисел из массива nums, наиболее близкая к target
"""

from itertools import combinations


def closest_sum(nums, target):
    result = []
    for subset in combinations(nums, 3):
        result.append(target - sum(subset))
    nearest_sum = min(result, key=abs)
    return target-nearest_sum


print(closest_sum([-1, 2, 1, -4], 1))
