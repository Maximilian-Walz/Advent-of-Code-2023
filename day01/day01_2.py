import regex as re

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

regex = r"one|two|three|four|five|six|seven|eight|nine|\d"

def getNumber(numberString: str) -> int:
    if numberString in digits:
        return digits[numberString]
    elif numberString.isdigit():
        return int(numberString)
    else:
        return 0

with open("input.txt", "r") as file:
    sum = 0
    for line in file.readlines():
        matches = re.findall(regex, line, overlapped=True)
        values = [getNumber(numberString) for numberString in matches]
        value = (values[0] * 10 + values[-1])
        sum += value
    print(sum)