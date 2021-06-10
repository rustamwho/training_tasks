def count_safe_ingredients(allergens, all_ingredients):
    """Количество повторений безопасных ингредиентов"""
    # список уникальных опасных ингредиентов
    unique = set()
    finish = False
    while not finish:
        for allergen, ingredients in allergens.items():
            if len(ingredients) == 1:
                unique.update(ingredients)
            else:
                allergens[allergen].difference_update(unique)
                if len(allergens[allergen]) == 1:
                    unique.update(allergens[allergen])
        if all(len(x) == 1 for _, x in allergens.items()):
            finish = True

    safe_ingredients = set(all_ingredients) - unique
    count_ingredients = sum(all_ingredients.count(x) for x in safe_ingredients)
    return count_ingredients


def get_str(allergens):
    """Строка из отсортированного словаря"""
    result_str = ''
    for allergen in sorted(allergens):
        result_str += list(allergens[allergen])[0] + ','
    result_str = result_str.strip(',')
    return result_str


def read():
    with open('input.txt', 'r') as file:
        data = file.read()
    all_ingredients = []
    allergens = {}

    for line in data.split('\n'):
        ingredients_str, names_allergen = line.split(' (contains ')
        ingredients = ingredients_str.split()
        all_ingredients.extend(ingredients)
        ingredients = set(ingredients)
        names_allergen = [x.strip(',') for x in
                          names_allergen.strip(')').split()]

        for name in names_allergen:
            if name in allergens:
                allergens[name] = allergens[name] & ingredients
            else:
                allergens[name] = ingredients

    return all_ingredients, allergens


ingredients_all, all_allergens = read()
# Part 1
safe_ingredients_count = count_safe_ingredients(all_allergens, ingredients_all)
# Part 2
dangerous_ingredients = get_str(all_allergens)
print(f"Safe ingredients are repeated:\t{safe_ingredients_count}\n"
      f"Dangerous ingredients str:\t\t{dangerous_ingredients}")
