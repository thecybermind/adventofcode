import copy
import operator

monkeys = []
with open('input11.txt') as inp:
    monkey = {}
    for line in inp:
        line = line.strip()
        
        # Monkey 0:
        #   Starting items: 54, 61, 97, 63, 74
        #   Operation: new = old * 7    old + 2    old * old
        #   Test: divisible by 17
        #     If true: throw to monkey 5
        #     If false: throw to monkey 3        

        if line.startswith('Monkey '):
            line = line.rstrip(':')
            monkey['num'] = int(line[7:])
            monkey['inspects'] = 0
        elif line.startswith('Starting items: '):
            monkey['items'] = [int(n.strip()) for n in line[16:].split(',')]
        elif line.startswith('Operation: '):
            op = line.split(' ')[4]
            monkey['operator'] = operator.mul if op == '*' else operator.add
            # None = use old            
            operand1 = line.split(' ')[3]
            monkey['operand1'] = None if operand1 == 'old' else int(operand1)
            operand2 = line.split(' ')[5]
            monkey['operand2'] = None if operand2 == 'old' else int(operand2)
        elif line.startswith('Test: '):
            monkey['test'] = int(line.split(' ')[3])
        elif line.startswith('If true: '):
            monkey['if_true'] = int(line.split(' ')[5])
        elif line.startswith('If false: '):
            monkey['if_false'] = int(line.split(' ')[5])
            monkeys.append(monkey)
            monkey = {}

def get_lcm(monkeys):
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey['test']
    return lcm   

# monkey turn:
# inspects item (worry level)
# worry level operation
# bored: worry level = int(worry level / 3)
# test
# throw
def monkey_turn(monkeys, monkey_num, part2):
    lcm = get_lcm(monkeys)

    monkey = monkeys[monkey_num]
    
    for item in monkey['items']:
        worry = item
        
        # inspect
        monkey['inspects'] += 1

        # worry level operation
        # if stored value is None, then use existing value
        operand1 = monkey['operand1'] or worry
        operand2 = monkey['operand2'] or worry
        op = monkey['operator']
        worry = op(operand1, operand2)

        # bored
        if not part2:
            worry = int(worry / 3)
        worry %= lcm
        
        # test / throw
        newmonkey = monkey['if_false'] if worry % monkey['test'] else monkey['if_true']
        monkeys[newmonkey]['items'].append(worry)
    monkey['items'] = []

def monkey_round(monkeys, part2=False):
    for i in range(len(monkeys)):
        monkey_turn(monkeys, i, part2)

def get_monkey_business(monkeys):
    inspects = []
    for monkey in monkeys:
        inspects.append(monkey['inspects'])
    inspects.sort()    
    return inspects[-1] * inspects[-2]


# make a copy of the list for part 2
monkeys_part2 = copy.deepcopy(monkeys)

for i in range(20):
    monkey_round(monkeys)
part1 = get_monkey_business(monkeys)
print(f'Part 1 monkey business: {part1}')

for i in range(10000):
    monkey_round(monkeys_part2, True)
part2 = get_monkey_business(monkeys_part2)
print(f'Part 2 monkey business: {part2}')

