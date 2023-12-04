import re

def read_numbers():
    part_number_pattern = r"(\d+)"

    with open("input.txt", "r") as input:
        lines = [line.strip() for line in input.readlines() if line.strip()]
        
        numbers = []
        for index ,line in enumerate(lines):
            for match in re.finditer(part_number_pattern, line):
                numbers.append({
                    "line": index,
                    "start": match.start(),
                    "end": match.end(),
                    "number": int(match.group(1))
                })
        return lines, numbers
    
if __name__ == "__main__":
    lines, numbers = read_numbers()
    
    special_chars = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    parts = []

    for number in numbers:
        is_part = False

        #Check left
        if number["start"] > 1:
            char_left = lines[number["line"]][number["start"] - 1]
            if char_left not in special_chars:
                parts.append(number)
                is_part = True

        #Check right
        if number["end"] < len(lines[number["line"]]) - 1 and not is_part:
            char_right = lines[number["line"]][number["end"]]
            if char_right not in special_chars:
                parts.append(number)
                is_part = True

        #Check above
        if number["line"] > 0 and not is_part:
            line_above = lines[number["line"] - 1]
            substring_above = line_above[max(number["start"]-1,0):min(number["end"] + 1, len(line_above))]
            for char in substring_above:
                if char not in special_chars:
                    parts.append(number)
                    is_part = True
                    break
        
        #Check below
        if number["line"] < len(lines) - 1 and not is_part:
            line_below = lines[number["line"] + 1]
            substring_below = line_below[max(number["start"]-1,0):min(number["end"] + 1, len(line_below))]
            for char in substring_below:
                if char not in special_chars:
                    parts.append(number)
                    is_part = True
                    break

    part_number_sum = sum([part["number"] for part in parts])
    print(part_number_sum)