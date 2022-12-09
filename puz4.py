# 51-88,52-87

def make_range(r):
    first, last = r.split('-')
    return list(range(int(first), int(last) + 1))
    
def range_in_range(r1, r2):
    small = r1
    big = r2
    if len(small) > len(big):
        big = r1
        small = r2

    for c in small:
        if c not in big:
            return 0
    return 1

def range_overlaps(r1, r2):
    for c in r1:
        if c in r2:
            return 1
    return 0    

total_part1 = 0
total_part2 = 0
with open('input4.txt') as inp:
    for line in inp:
        line = line.strip()

        first, second = line.split(',')
        first = make_range(first)
        second = make_range(second)
        total_part1 += range_in_range(first, second)
        total_part2 += range_overlaps(first, second)

print(f'Part 1 Total full overlaps: {total_part1}')  
print(f'Part 2 Total partial+ overlaps: {total_part2}')  
