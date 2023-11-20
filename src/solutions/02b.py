# https://adventofcode.com/2022/day/2

shapes = {
    'X': [
        0,
        {
            'A': 3,
            'B': 1,
            'C': 2
        }],
    'Y': [
        3,
        {
            'A': 1,
            'B': 2,
            'C': 3
        }],
    'Z': [
        6,
        {
            'A': 2,
            'B': 3,
            'C': 1
        }]
}

score = 0

with open('src/inputs/02a.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        opp, plr = line.split()

        score += shapes[plr][0]
        score += shapes[plr][1][opp]

with open('src/outputs/02b.txt', 'w') as f:
    f.write(f'{score}')
