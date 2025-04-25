
check_between_numbers = lambda A, B, C: (B > A and B < C) or (B > C and B < A)

check_odd_three = lambda number: (100 <= abs(number) <= 999) and (number % 2 != 0)

check_unique_digits = lambda number: (
    True if 100 <= abs(number) <= 999 and len({d for d in str(abs(number))}) == 3 else False
)


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


check_ascending_digits = lambda number: (
    (lambda s: len(s) == 3 and s[0] < s[1] < s[2])(str(abs(number)))
)
