# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def check_bags(first, second):
    for c in first:
        if c in second:
            return c
    raise Exception()
    
def priority(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    raise Exception()

def find_badge(bags):
    first = bags[0]
    second = bags[1]
    third = bags[2]
    for c in first:
        if c in second and c in third:
            return c
    
    raise Exception()

total_part1 = 0
total_part2 = 0
group_bags = []
with open('input3.txt') as inp:
    for line in inp:
        line = line.strip()
        
        # part 1
        half = int(len(line) / 2)
        first = line[0:half]
        second = line[half:]
        
        duplicate = check_bags(first, second)
        
        total_part1 += priority(duplicate)
        
        # part 2
        group_bags.append(line)
        if len(group_bags) == 3:
            badge = find_badge(group_bags)
            total_part2 += priority(badge)
            group_bags = []

print(f'Part 1 Total priority: {total_part1}')
print(f'Part 2 Total priority: {total_part2}')
