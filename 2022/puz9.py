movements = []
with open('input9.txt') as inp:
    for line in inp:
        line = line.strip()
        dir, count = line.split(' ')
        count = int(count)
        movements.append( (dir, count) )

# part 2 increases number of segments to 10, but rules for moving towards previous segments are the same as part 1 head/tail rules
def run_sim(movements, snake_len):
    tail_index = snake_len - 1
    # x/y coords for each segment... (x[0], y[0]) is head, (x[1], y[1]) is next segment, (x[tail_index], y[tail_index]) is final tail segment
    x = [0] * snake_len
    y = [0] * snake_len
    visited = {(x[tail_index], y[tail_index]): True}

    # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
    # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
    def move_tails():
        # move through each non-head segment and move it towards the previous one using above rules
        
        # for simplification of steps,
        # "tail" is the segment currently moving    
        # "head" is the previous segment
        for tail in range(1, snake_len):
            head = tail - 1        
        
            # if tail is touching head, don't do anything
            if abs(x[head] - x[tail]) <= 1 and abs(y[head] - y[tail]) <= 1:
                return

            # same column
            if x[head] == x[tail]:
                movex = 0
                movey = (y[head] - y[tail]) / 2
            # same row
            elif y[head] == y[tail]:
                movex = (x[head] - x[tail]) / 2
                movey = 0
            # 1 column left/right, 2 rows up/down
            elif abs(x[head] - x[tail]) == 1:
                movex = x[head] - x[tail]
                movey = (y[head] - y[tail]) / 2
            # 1 row up/down, 2 cols left/right
            elif abs(y[head] - y[tail]) == 1:
                movex = (x[head] - x[tail]) / 2
                movey = y[head] - y[tail]

            x[tail] += int(movex)
            y[tail] += int(movey)

        visited[(x[tail_index], y[tail_index])] = True

    # go through all movements from input
    for dir, count in movements:
        if dir == 'D':
            for move in range(0, count):
                y[0] += 1
                move_tails()
        elif dir == 'U':
            for move in range(0, count):
                y[0] -= 1
                move_tails()
        elif dir == 'L':
            for move in range(0, count):
                x[0] -= 1
                move_tails()
        elif dir == 'R':
            for move in range(0, count):
                x[0] += 1
                move_tails()

    return visited

tail_visited_part1 = len(run_sim(movements, 2))
print(f'Part 1 # spaces tail visited: {tail_visited_part1}')

tail_visited_part2 = len(run_sim(movements, 10))
print(f'Part 2 # spaces tail visited: {tail_visited_part2}')
