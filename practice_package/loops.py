def sum_even_digits(number):
    return sum(int(ch) for ch in str(abs(number)) if int(ch) % 2 == 0)


def count_vowel_triplets(text):
    vowels = set('aeiouyAEIOUY')
    n = len(text)
    i = 0
    total = 0

    while i < n:
        if text[i] in vowels:
            start = i
            while i < n and text[i] in vowels:
                i += 1
            length = i - start
            if length >= 3:
                total += max(1, length - 2 if length > 3 else 1)
        else:
            i += 1
    return total


def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1
    f1, f2, idx = 1, 1, 2
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