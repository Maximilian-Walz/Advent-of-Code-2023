with open("input.txt", "r") as input:
    sum = 0
    for line in input.readlines():
        digits = [int(digit) for digit in line.strip() if digit.isdigit()]
        value = digits[0] * 10 + digits[-1]
        sum += value
    print(sum)