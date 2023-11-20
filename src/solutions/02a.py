# https://adventofcode.com/2022/day/2

shapes = {
    'X': [
        1,
        {
            'A': 3,
            'B': 0,
            'C': 6
        }],
    'Y': [
        2,
        {
            'A': 6,
            'B': 3,
            'C': 0
        }],
    'Z': [
        3,
        {
            'A': 0,
            'B': 6,
            'C': 3
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

with open('src/outputs/02a.txt', 'w') as f:
    f.write(f'{score}')
