elves = []
elftotal = 0
with open('input1.txt') as inp:
    for line in inp:
        line = line.strip()
        if not line:
            elves.append(elftotal)
            elftotal = 0            
        else:
            elftotal += int(line)

elves.sort()

maxelf = elves[-1]
print(f'Top elf calories: {maxelf}')

total = sum(elves[-3:])
print(f'Total of top 3 calories: {total}')
