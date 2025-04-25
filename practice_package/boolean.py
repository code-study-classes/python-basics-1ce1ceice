check_between_numbers = lambda a, b, c: (a < b < c) or (c < b < a)

check_odd_three = lambda number: 100 <= abs(number) <= 999 and number % 2 != 0

check_unique_digits = lambda number: (
    100 <= abs(number) <= 999 and len(set(str(abs(number)))) == 3
)


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


check_ascending_digits = lambda number: (
    (lambda s: len(s) == 3 and s[0] < s[1] < s[2])(str(abs(number)))
)