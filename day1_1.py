# input_test = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""
#
# lines = input_test.split('\n')


with open('input_day1_1.txt') as fp:
    lines  = fp.readlines()


total = 0
for line in lines:
    first = None
    last = None

    for char in line:
        if char.isdigit():
            if first == None:
                first = char
            last = char

    sum_thisline = int(first+last)
    total += sum_thisline

print(total)

    