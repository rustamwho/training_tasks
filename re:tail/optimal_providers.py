class Provider:
    def __init__(self, id, price, amount, count, delivery):
        """
        price - цена за одну партию продукции
        amount - количество продукции в одной партии продукции
        count - количество партий продукции в наличии
        delivery - стоимости доставки для всех поставщиков
        """
        self.id = id
        self.price = price
        self.amount = amount
        self.count = count
        self.delivery = delivery
        self.price_one_product = (self.price + self.delivery) / self.amount
        self.price_one_party = self.price + self.delivery
        self.all_products = self.amount * self.count
        self.medium = self.medium()

    def __str__(self):
        return str(self.id)

    def medium(self):
        all_sum = self.count * self.price + self.delivery
        return all_sum / self.all_products


def get_result(n, price, amount, count, delivery):
    providers = []

    for i in range(len(price)):
        providers.append(
            Provider(i, price[i], amount[i], count[i], delivery[i]))
    providers = sorted(providers, key=lambda x: x.medium)

    count_products = 0
    result_ids = []
    cash = []

    for i, provider in enumerate(providers):
        if (provider.all_products > n - count_products
                and
                sum(x.all_products for x in
                    providers[i + 1:]) + count_products >= n):
            cash.append(provider)
            continue
        while count_products < n and provider.count:
            count_products += provider.amount
            provider.count -= 1
        result_ids.append(provider.id)
        if count_products >= n:
            break

    if count_products < n and cash:
        for provider in cash:
            while count_products < n and provider.count:
                count_products += provider.amount
                provider.count -= 1
            result_ids.append(provider.id)
            if count_products >= n:
                break

    return ','.join(str(x) for x in result_ids)


print(get_result(1000, [100, 200, 300, 400], [50, 100, 500, 100], [4, 5, 7, 3],
                 [0, 100, 5000, 1000]))
print(get_result(1000, [100, 200, 300, 400], [50, 100, 500, 100], [4, 5, 7, 3],
                 [1000, 100, 5000, 1000]))
print(get_result(28000, [500, 200, 3000, 400], [50, 100, 500, 100],
                 [17, 36, 70, 45], [1000, 500, 5000, 0]))
print(get_result(80000, [100, 200, 300, 400], [50, 100, 500, 100],
                 [17, 36, 70, 45], [1000, 500, 5000, 1000]))
