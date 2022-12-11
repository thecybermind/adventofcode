# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.


# addx variable will contain the additions to X per cycle.
# every instruction means a 0 gets put in the list
# addx instructions get an additional value put in the list, the actual value to add
addx = []
with open('input10.txt') as inp:
    for line in inp:
        line = line.strip()
        addx.append(0)
        if line.startswith('addx '):
            addx.append(int(line[5:]))

def run_sim(addx):
    # register
    X = 1
    # total signal strength for part 1
    signal_strength = 0

    # i is 0-based index of addx[]
    for i in range(len(addx)):
        # cycle is 1-based
        cycle = i + 1
        # add signal strength of these cycles
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += (cycle * X)
        
        # if sprite is within 1 of column, print #
        if abs(i % 40 - X) <= 1:
            print('#', end='')
        else:
            print(' ', end='')
        # newline if end of row
        if cycle % 40 == 0:
            print('')

        # add value to register for this cycle
        X += addx[i]
    
    return signal_strength

print(f'Part 2:')
signal_strength_part1 = run_sim(addx)

print('')

print(f'Part 1 sum of signal strength: {signal_strength_part1}')
