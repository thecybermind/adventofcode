# this is a list of lines, each represented by a tuple of points (each point represented by a single tuple)
# i.e.    [ ( (1,2),(10,2) ), (10,2),(10,5) ) ]
rocklines = []
with open('input14.txt') as inp:
    for line in inp:
        line = line.strip()

        # path will contains a list of points (as tuples) directly from input
        path = []
        for point in line.split(' -> '):
            for x,y in [point.split(',')]:
                path.append( (int(x),int(y)) )

        # zip up the list with itself (offset by 1) to get a list of two-point tuples
        rocklines.extend( zip(path[:-1], path[1:]) )

# returns a list of points for each spot along the line
def get_line_points(point1, point2):
    p1_x, p1_y = point1
    p2_x, p2_y = point2
    # vertical line
    if p1_x == p2_x:
        return [(p1_x, y) for y in range( min(p1_y, p2_y), max(p1_y, p2_y)+1 )]
    # horizontal line
    if p1_y == p2_y:
        return [(x, p1_y) for x in range( min(p1_x, p2_x), max(p1_x, p2_x)+1 )]

# sets a point on a grid to a specific value
def set_grid_point(grid, point, value):
    x, y = point
    grid.setdefault(y, {})[x] = value

# gets a point on a grid
def get_grid_point(grid, point):
    x, y = point
    return grid.get(y, {}).get(x, ' ')

# return a dict of rows, where each row is a dict of columns with what is in that position
def make_grid(lines, part2=False):
    grid = {}
    for p1, p2 in lines:
        points = get_line_points(p1, p2)
        for point in points:
            set_grid_point(grid, point, '#')

    # didn't feel like checking "infinite floor" logic in every condition of drop_sand() so let's just make an actual floor
    if part2:
        floor_y = max(grid) + 2
        for x in range(-10000,10000):
            set_grid_point(grid, (x, floor_y), '#')

    return grid

# drops a single piece of sand starting at point
# part 1:
# returns False if continued on into the abyss, True if stopped
# part 2:
# returns False if sand has stacked up to the origin, True if stopped
def drop_sand(grid, point, part2=False):
    # if we are doing part 2 and the starting spot is sand, return False
    if part2 and get_grid_point(grid, point) == 'o':
        return False

    x, y = point
    # find highest row in grid (lowest visually), anything past this is falling into the abyss
    bottom = max(grid)

    while True:
        # if part1, just end as soon as the sand falls off the edge
        if y >= bottom + 2:
            return False

        # check below
        below = get_grid_point(grid, (x, y + 1))
        # if open, continue
        if below == ' ':
            y += 1
            continue
        # not open, check left then right
        else:
            # check left
            below_left = get_grid_point(grid, (x - 1, y + 1))
            # if open, continue
            if below_left == ' ':
                x, y = x - 1, y + 1
                continue
            # check right
            below_right = get_grid_point(grid, (x + 1, y + 1))
            # if open, continue
            if below_right == ' ':
                x, y = x + 1, y + 1
                continue
            # at this point, we are blocked. change to sand and exit
            set_grid_point(grid, (x, y), 'o')
            return True

origin = (500,0)

grid_part1 = make_grid(rocklines)
set_grid_point(grid_part1, origin, '+')
stopped_part1 = 0
while True:
    res = drop_sand(grid_part1, origin)
    stopped_part1 += res
    if not res:
        break
print(f'Part 1: {stopped_part1}')

grid_part2 = make_grid(rocklines, part2=True)
set_grid_point(grid_part2, origin, '+')
stopped_part2 = 0
while True:
    res = drop_sand(grid_part2, origin, part2=True)
    stopped_part2 += res
    if not res:
        break
print(f'Part 2: {stopped_part2}')
