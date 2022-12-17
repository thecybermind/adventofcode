import pprint

test = False

# taxi cab distance between 2 points
def point_taxi_distance(point1, point2):
    p1_x, p1_y = point1
    p2_x, p2_y = point2
    return abs(p2_x - p1_x) + abs(p2_y - p1_y)

# sets points on grid within range of a given point
def set_grid_area(grid, point, distance, value, part1_need_row):
    # print(f'set_grid_area({point},{distance})')
    x, y = point
    for row in range(y - distance, y + distance + 1):
        if part1_need_row and row != part1_need_row:
            continue
        for col in range(x - distance, x + distance + 1):            
            check_point = (col, row)
            if get_grid_point(grid, check_point) != ' ':
                continue
            if point_taxi_distance(point, check_point) <= distance:
                set_grid_point(grid, check_point, value)

# sets a point on a grid to a specific value
def set_grid_point(grid, point, value):
    x, y = point
    grid.setdefault(y, {})[x] = value

# gets a point on a grid
def get_grid_point(grid, point):
    x, y = point
    return grid.get(y, {}).get(x, ' ')

def load_grid(part1_need_row, test):
    grid = {}
    # Sensor at x=3729579, y=1453415: closest beacon is at x=4078883, y=2522671
    with open('input15test.txt' if test else 'input15.txt') as inp:
        for line in inp:
            line = line.strip()
            words = line.split(' ')

            sensor = (int(words[2][2:-1]) , int(words[3][2:-1]) )
            beacon = (int(words[8][2:-1]) , int(words[9][2:]) )
            distance = point_taxi_distance(sensor, beacon)
            
            set_grid_point(grid, sensor, 'S')
            set_grid_point(grid, beacon, 'B')
            set_grid_area(grid, sensor, distance, '#', part1_need_row)

    return grid            

row_part1 = 10 if test else 2000000
grid_part1 = load_grid(row_part1, test)

blocked_part1 = len([value for value in grid_part1[row_part1].values() if value == '#'])
print(f'Part 1: {blocked_part1}')

grid_part2 = 0 # load_grid(False, test)
print(f'Part 2: {grid_part2}')
