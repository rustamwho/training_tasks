def valid_bieyr(value, type):
    """проверка валидности значения годов рождения, выпуска и срока действия"""
    if value.isdigit() and len(value) == 4:
        if type == 'byr':
            if 1920 <= int(value) <= 2002:
                return True
            else:
                return False
        elif type == 'iyr':
            if 2010 <= int(value) <= 2020:
                return True
            else:
                return False
        else:
            if 2020 <= int(value) <= 2030:
                return True
            else:
                return False
    else:
        return False


def valid_hgt(value):
    """проверка на валидность роста"""
    height = ''
    type = ''
    if value.isalnum():
        for i in value:
            if i.isdigit():
                height += i
            else:
                type += i
    if height and type:
        if (type == 'cm' and 150 <= int(height) <= 193) or (
                type == 'in' and 59 <= int(height) <= 76):
            return True
        else:
            return False
    else:
        False


def valid_hcl(value):
    """проверка на валидность значения цвета волос"""
    if (value[0] == '#') and (len(value) == 7):
        for i in value[1:]:
            if (i.isdigit() == True) or (i in 'abcdef'):
                continue
            else:
                return False
        return True
    else:
        return False


def valid_ecl(value):
    """проверка на валидность значения цвета глаз"""
    if value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True
    else:
        return False


def valid_pid(value):
    """проверка на валидность id паспорта"""
    if len(value) == 9 and value.isdigit():
        return True
    else:
        return False


def valid_passport(passport):
    for field in ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']:
        if field in passport:
            continue
        else:
            return None
    # разделение на атрибуты входного паспорта
    found_fields = passport.split()
    for field in found_fields:
        if "byr:" in field:
            if valid_bieyr(field.split(':')[1], 'byr'):
                continue
            else:
                return 0
        elif "iyr:" in field:
            if valid_bieyr(field.split(':')[1], 'iyr'):
                continue
            else:
                return 0
        elif "eyr:" in field:
            if valid_bieyr(field.split(':')[1], 'eyr'):
                continue
            else:
                return 0
        elif "hgt:" in field:
            if valid_hgt(field.split(':')[1]):
                continue
            else:
                return 0
        elif "hcl:" in field:
            if valid_hcl(field.split(':')[1]):
                continue
            else:
                return 0
        elif "ecl:" in field:
            if valid_ecl(field.split(':')[1]):
                continue
            else:
                return 0
        elif "cid:" in field:
            continue
        else:
            if valid_pid(field.split(':')[1]):
                continue
            else:
                return 0
    return 1


def verification_passport():
    count = 0
    count_invalid_passports = 0
    count_valid_passports2 = 0

    with open("input.txt", "r") as file:
        for pas in file.read().split('\n\n'):
            count+=1
            # 1 - правильные данные паспорта, 0 - неправильное значение поля
            # None - какого-то поля нет
            ver_pass = valid_passport(pas)
            if ver_pass is None:
                count_invalid_passports += 1
            else:
                count_valid_passports2 += ver_pass

    # первая часть: количество паспортов - кол-во паспортов без какого-то поля
    count_valid_passports1 = count - count_invalid_passports
    return count_valid_passports1, count_valid_passports2


count1, count2 = verification_passport()
print(f"Part 1: {count1}\nPart 2: {count2}")
