# source file (part 1):
# a   rock   x
# b   paper  y
# c scissors z

# source file (part 2):
# a   rock   x	lose
# b   paper  y	draw
# c scissors z	win

# points:
# 1 rock
# 2 paper
# 3 scissors
# 0 loss
# 3 draw
# 6 win
def rps_part1(other, me):
    value = me + 1
    if other == me:
        return 3 + value
    winner = (other + 1) % 3
    if me == winner:
        return 6 + value
    return 0 + value
    
# outcome:
# 0 - lose
# 1 - draw
# 2 - win
# points:
# 1 rock
# 2 paper
# 3 scissors
# 0 loss
# 3 draw
# 6 win
def rps_part2(other, outcome):
    if outcome == 0:
        me = (other + 2) % 3
    elif outcome == 1:
        me = other
    else:
        me = (other + 1) % 3
    value = me + 1
    return outcome * 3 + value

rounds_part1 = []
rounds_part2 = []
with open('input2.txt') as inp:
    for line in inp:
        line = line.strip()
        
        a, b = line.split(' ')
        a = ord(a) - ord('A')
        b = ord(b) - ord('X')
        
        rounds_part1.append(rps_part1(a, b))
        rounds_part2.append(rps_part2(a, b))

total_part1 = sum(rounds_part1)
print(f'Part 1 Total score: {total_part1}')
total_part2 = sum(rounds_part2)
print(f'Part 2 Total score: {total_part2}')
