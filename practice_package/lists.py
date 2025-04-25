from functools import reduce
from itertools import takewhile


def square_odds(numbers):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 != 0, numbers)))


def normalize_names(names):
    return list(map(lambda s: s.capitalize(), names))


def remove_invalid_emails(emails):
    valid = lambda e: (e.count('@') == 1 and len(e) >= 5 and not e.startswith('@') and not e.endswith('@'))
    return list(filter(valid, emails))


def filter_palindromes(words):
    is_pal = lambda w: (w_lower := w.lower()) == w_lower[::-1]
    return list(filter(is_pal, words))


def calculate_factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)


def find_common_prefix(strings):
    if not strings:
        return ''
    pairs = zip(*strings)
    common = takewhile(lambda tpl: all(ch == tpl[0] for ch in tpl), pairs)
    return ''.join(map(lambda tpl: tpl[0], common))