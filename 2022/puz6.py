#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

def is_marker(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return len(s) == len(d)

def find_marker(stream, length):
    for c in range(length, len(stream)):
        last = stream[c - length:c]
        if is_marker(last):
            return c


stream = ''
with open('input6.txt') as inp:
    for line in inp:
        stream += line.strip()

start_of_packet = find_marker(stream, 4)
print(f'Part 1 start of packet marker ends: {start_of_packet}')
message = find_marker(stream, 14)
print(f'Part 1 message marker ends: {message}')

# total_part1 = 0
# total_part2 = 0
# print(f'Part 1 : {total_part1}')  
# print(f'Part 2 : {total_part2}')
