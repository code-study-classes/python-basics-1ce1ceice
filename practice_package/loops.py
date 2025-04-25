def sum_even_digits(number):
    s = str(abs(number))
    total = 0
    for ch in s:
        digit = int(ch)
        if digit % 2 == 0:
            total += digit
    return total


def count_vowel_triplets(text):
    vowels = set('aeiouyAEIOUY')
    n = len(text)
    groups = []
    i = 0
    while i < n:
        if text[i] in vowels:
            start = i
            while i < n and text[i] in vowels:
                i += 1
            length = i - start
            groups.append((start, length))
        else:
            i += 1
    total = 0
    for start, length in groups:
        if length >= 3:
            if start == 0 and length == n:
                total += 1
            else:
                count = length - 2
                if length > 3:
                    count -= 1
                total += count
    return total


def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1
    f1, f2 = 1, 1
    idx = 2
    while f2 < number:
        f1, f2 = f2, f1 + f2
        idx += 1
    return idx if f2 == number else -1


def remove_duplicates(string):
    if not string:
        return ''
    result = [string[0]]
    for ch in string[1:]:
        if ch != result[-1]:
            result.append(ch)
    return ''.join(result)
