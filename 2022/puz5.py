#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

stacks_part1 = []
stacks_part2 = []
moves = False
with open('input5.txt') as inp:
    for line in inp:
        line = line.rstrip('\r\n')
        # create initial empty stacks
        if not stacks_part1:
            numstacks = int((len(line) + 1) / 4)
            stacks_part1.extend([] for i in range(0, numstacks))
            stacks_part2.extend([] for i in range(0, numstacks))
        
        # skip blank line
        if not line:
            continue

        # stack definitions
        if not moves:
            # loop through each stack
            for i in range(1, len(line), 4):
                # stack number line, set flag and exit loop
                if line[i].isnumeric():
                    moves = True
                    break
                if line[i] != ' ':
                    pos = int((i - 1) / 4)
                    stacks_part1[pos].insert(0, line[i])
                    stacks_part2[pos].insert(0, line[i])
        # moves
        else:
            _, count, _, src, _, dest = line.split(' ')
            count = int(count)
            src = int(src) - 1
            dest = int(dest) - 1
            # part 1: move <count> boxes from src to dest
            for i in range(0, count):
                stacks_part1[dest].append(stacks_part1[src].pop())
            # part 2: move <count> boxes all at once from src to dest
            stacks_part2[dest].extend(stacks_part2[src][-count:])
            stacks_part2[src] = stacks_part2[src][:-count]


stack_tops_part1 = ''.join([s[-1] for s in stacks_part1])
stack_tops_part2 = ''.join([s[-1] for s in stacks_part2])
print(f'Part 1 stack tops: {stack_tops_part1}')  
print(f'Part 2 stack tops: {stack_tops_part2}')
