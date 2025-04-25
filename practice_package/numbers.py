calculate_distance = lambda x1, x2: abs(x1 - x2)


calculate_segments = lambda length_a, length_b: length_a // length_b


calculate_digit_sum = lambda number: sum(int(digit) for digit in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)


def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple