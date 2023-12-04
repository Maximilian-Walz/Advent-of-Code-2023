import day02_1

day02_1.read_games()
sum = 0
for game in day02_1.games:
    cubes_needed = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for move in game["moves"]:
        for hand in move:
            cubes_needed[hand[1]] = max(cubes_needed[hand[1]], int(hand[0]))

    game["power"] = cubes_needed["red"] * cubes_needed["green"] * cubes_needed["blue"]
    sum += game["power"]

print(sum)