import re

with open('input_day1_1.txt') as fp:
    lines  = fp.readlines()


def transform_written_digits(line):
    written_digits = {
        'one': '1',
        'two': '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    } | {str(i) : i for i in range(1,10)}

    digit_pos = {}
    for digit, int_digit in written_digits.items():
        digit_pos |= {match.start() : int_digit for match in re.finditer(digit, line)}

    first_digit = digit_pos[min(digit_pos.keys())]
    last_digit = digit_pos[max(digit_pos.keys())]

    return int(str(first_digit)+str(last_digit))


total = 0
for line in lines:
    total += transform_written_digits(line)

print(total)
