def is_weekend(day):
    return day in (6, 7)


def get_discount(amount):
    if amount >= 5000:
        rate = 0.1
    elif amount >= 1000:
        rate = 0.05
    else:
        rate = 0
    return round(amount * rate, 2)


def describe_number(n):
    parity = 'четное' if n % 2 == 0 else 'нечетное'
    length = len(str(n))
    digits = {1: 'однозначное', 2: 'двузначное', 3: 'трехзначное'}.get(length, '')
    return f"{parity} {digits} число"


def convert_to_meters(unit_number, length_in_units):
    factors = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01,
    }
    return length_in_units * factors.get(unit_number, 1)


def describe_age(age):
    tens_map = {
        20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
        60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
        90: 'девяносто', 100: 'сто'
    }
    units_map = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    if age == 100:
        words = tens_map[100]
    else:
        ten = (age // 10) * 10
        unit = age % 10
        words = tens_map.get(ten, '') + (f" {units_map[unit]}" if unit else '')

    mod100 = age % 100
    if 11 <= mod100 <= 14:
        suffix = 'лет'
    else:
        suffix = {
            1: 'год',
            2: 'года',
            3: 'года',
            4: 'года'
        }.get(age % 10, 'лет')

    return f"{words} {suffix}"