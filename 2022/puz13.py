import functools
import itertools
import json

# each entry is a zip of each pair of lines
packet_pairs = []

# each original packet from file (for part 2)
packets_part2 = []

with open('input13.txt') as inp:
    for line1 in inp:
        line1 = line1.strip()
        if not line1:
            continue
        line2 = inp.readline().strip()
        
        packet1 = json.loads(line1.strip())
        packet2 = json.loads(line2.strip())

        # save all original packets for part 2
        packets_part2.append(packet1)
        packets_part2.append(packet2)
        
        # zip up both packets together
        packet_pairs.append( list(itertools.zip_longest(packet1, packet2)) )

    packets_part2.append([[2]])
    packets_part2.append([[6]])

# compare a single value pair
def compare_values(pair):
    first, second = pair
    
    # If the left list runs out of items first, the inputs are in the right order
    if first is None:
        return -1
    # If the right list runs out of items first, the inputs are not in the right order
    if second is None:
        return 1
    
    # if both are integers, leave with simple comparison (base case)
    if not isinstance(first, list) and not isinstance(second, list):
        # standard -1,0,1 universal comparison result
        cmp = (first > second) - (first < second)
        return cmp

    # If exactly one value is an integer, convert the integer to a list which contains
    # that integer as its only value, then retry the comparison
    if not isinstance(first, list):
        first = [first]
    if not isinstance(second, list):
        second = [second]
    
    # loop through every item in each list and recursively compare those values
    for pair in itertools.zip_longest(first, second):
        cmp = compare_values(pair)
        if cmp != 0:
            return cmp
    
    # if we reached here, the first and second lists are equal
    return 0

# compare a zipped packet pair
def compare_zipped_packet_pair(zipped_packet_pair):
    # loop through each pair of values in those packets
    for values in zipped_packet_pair:
        # if first value is less than second value, they are in the correct order
        cmp = compare_values(values)
        if cmp != 0:
            return cmp
    return 0

# comparison-style function for sorting 2 packets
def sort_packet(packeta, packetb):
    zipped = itertools.zip_longest(packeta, packetb)
    return compare_zipped_packet_pair(zipped)

# find the (1-based) indexes of the part 2 divider packets in the packet list
def find_dividers(packets):
    two = packets.index([[2]]) + 1
    six = packets.index([[6]]) + 1
    return two * six

part1 = 0
# loop through each pair of packets from input
for num, packet_pair in enumerate(packet_pairs):
    num += 1
    cmp = compare_zipped_packet_pair(packet_pair)
    if cmp < 0:
        part1 += num
 
print(f'Part 1: {part1}')

packets_part2.sort(key=functools.cmp_to_key(sort_packet))
part2 = find_dividers(packets_part2)

print(f'Part 2: {part2}')
