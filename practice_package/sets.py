from functools import reduce


def find_common_elements(set1, set2):
    return set1 & set2


def is_superset(set_a, set_b):
    return set_b <= set_a


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    return len(set(text.lower().split()))


def find_shared_items(*sets_):
    if not sets_:
        return set()
    return reduce(set.intersection, sets_)