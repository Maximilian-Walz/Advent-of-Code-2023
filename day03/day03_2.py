import day03_1

gear_pattern = r"\*"

lines, numbers = day03_1.read_numbers()

number_adjacent_fields = {}

def addToNumberAdjacentFields(line, pos, number):
    if line < 0 or line >= len(lines):
        return
    key = f"{line}:{pos}"
    if key not in number_adjacent_fields:
        number_adjacent_fields[key] = []
    number_adjacent_fields[key].append(number)


for number in numbers:
    for pos in range(number["start"] - 1, number["end"] + 1):
        addToNumberAdjacentFields(number["line"] - 1, pos, number["number"]) # Above
        addToNumberAdjacentFields(number["line"] + 1, pos, number["number"]) # Below

    addToNumberAdjacentFields(number["line"], number["start"] - 1, number["number"]) # Left
    addToNumberAdjacentFields(number["line"], number["end"], number["number"]) # Right

gears = []
for key in number_adjacent_fields.keys():
    if len(number_adjacent_fields[key]) == 2:
        coords = key.split(":")
        if lines[int(coords[0])][int(coords[1])] == "*":
            gears.append(key)

gear_ratios = [number_adjacent_fields[key][0] * number_adjacent_fields[key][1] for key in gears]
print(sum(gear_ratios))
