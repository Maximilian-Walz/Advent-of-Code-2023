import re

line_pattern = r"Game (\d+): (.*)\n?"
hand_pattern = r"(\d+) (blue|red|green)"

games = []

def read_games():
    with open("input.txt", "r") as input:
        for line in input.readlines():
            match = re.match(line_pattern, line)
            if match:
                moves_strings = match.group(2).split(";")
                moves = [hands for hands in [re.findall(hand_pattern, move) for move in moves_strings] if len(hands) > 0]

                games.append({
                    "id": int(match.group(1)),
                    "moves": moves
                })


if __name__ == "__main__":
    cube_counts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    read_games()
    id_sum = 0
    for game in games:
        if len(game["moves"]) == 0:
            continue
        else:
            possible = True
            for move in game["moves"]:
                for hand in move:
                    if cube_counts[hand[1]] < int(hand[0]):
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                id_sum += game["id"]
    print(id_sum)
