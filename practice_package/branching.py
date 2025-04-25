def is_weekend(day):
    match day:
        case 6 | 7:
            return True
        case _:
            return False


def get_discount(amount):
    match amount:
        case a if a >= 5000:
            rate = 0.1
        case a if a >= 1000:
            rate = 0.05
        case _:
            rate = 0
    return round(amount * rate, 2)


def describe_number(n):
    parity = {True: 'четное', False: 'нечетное'}[n % 2 == 0]
    digits = {1: 'однозначное', 2: 'двузначное', 3: 'трехзначное'}[len(str(n))]
    return f"{parity} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    factors = {
        1: 0.1, 
        2: 1000, 
        3: 1, 
        4: 0.001, 
        5: 0.01    
    }
    return lengthInUnits * factors.get(unitNumber, 1)


def describe_age(age):
    tens_map = {
        20: 'двадцать', 30: 'тридцать', 40: 'сорок',
        50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
        80: 'восемьдесят', 90: 'девяносто', 100: 'сто'
    }
    units_map = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь',
        8: 'восемь', 9: 'девять'
    }
    match age:
        case 100:
            words = tens_map[100]
        case a:
            ten = (a // 10) * 10
            unit = a % 10
            words = tens_map[ten] + (f" {units_map[unit]}" if unit else "")
    mod100 = age % 100
    match mod100:
        case m if 11 <= m <= 14:
            suffix = 'лет'
        case _:
            match age % 10:
                case 1:
                    suffix = 'год'
                case 2 | 3 | 4:
                    suffix = 'года'
                case _:
                    suffix = 'лет'
    return f"{words} {suffix}"
