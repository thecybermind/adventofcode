import heapq

heightmap = []
start = None
end = None
with open('input12.txt') as inp:
    for row, line in enumerate(inp.readlines()):
        heightline = []
        for col, letter in enumerate(line.rstrip()):
            if letter == 'S':
                start, letter = (row, col), 'a'
            if letter == 'E':
                end, letter = (row, col), 'z'
            value = ord(letter) - ord('a')
            heightline.append(value)
        heightmap.append(heightline)

if not start or not end:
    print('Map missing start/end')
    raise Exception()

# make sure point is a valid location in grid
def is_valid(grid, point):
    row, col = point
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False
    return True

# taxi cab distance between 2 points
def point_taxi_distance(point1, point2):
    p1_row, p1_col = point1
    p2_row, p2_col = point2
    return abs(p2_row - p1_row) + abs(p2_col - p1_col)

# return all neighbors you can climb to (max of 1 higher elevation)
def get_neighbors(grid, point):
    row, col = point

    # direction adjustments
    # up, right, down, left
    d_row = [ -1, 0, 1, 0 ];
    d_col = [ 0, 1, 0, -1 ];

    neighbors = []
    for i in range(len(d_row)):
        adjrow = row + d_row[i]
        adjcol = col + d_col[i]
        adjpoint = (adjrow, adjcol)
        # if neighbor is out of bounds, skip it
        if not is_valid(grid, adjpoint):
            continue
        # if neighbor is too high, skip it
        if grid[adjrow][adjcol] > grid[row][col] + 1:
            continue
        
        neighbors.append(adjpoint)

    return neighbors

# find a path on grid from start to end
def navigate(grid, start, end):
    # distance keeps track of known distances of points from start
    distance = {start: 0}
    # to_visit is the priority queue of locations to visit
    to_visit = [(distance[start], start)]
 
    while to_visit:
        _, pos = heapq.heappop(to_visit)

        # if this is the end location, exit
        if pos == end:        
            break

        row, col = pos

        # neighbors to this location will be 1 away
        neighbor_distance = distance.get(pos, 0) + 1
        
        # visit all valid neighbors
        for neighbor in get_neighbors(grid, pos):
            # if new location is not visited or this way is closer, add neighbor to queue
            if neighbor not in distance or neighbor_distance < distance[neighbor]:
                # set the neighbor's distance value
                distance[neighbor] = neighbor_distance
                # priority will be neighbor's distance plus the taxi distance to end, the minimum possible distance passing through this location
                priority = neighbor_distance + point_taxi_distance( neighbor, end )
                # add to priority queue
                heapq.heappush(to_visit, (priority, neighbor))

    return distance.get(end, -1)

# find all 'a' locations that neighbor a 'b' and try to navigate from there. find shortest
def find_best_start(grid, end):
    # all valid start locations ('a' neighboring 'b')
    starts = []

    for row, heightline in enumerate(grid):
        for col, value in enumerate(heightline):
            # if this isn't an 'a' location, skip it
            if value != 0:
                continue
            # check neighbors
            for n_row, n_col in get_neighbors(grid, (row, col)):
                # if neighbor is a b, add this 'a' location to start list
                if grid[n_row][n_col] == 1:
                    starts.append((row, col))
                    break

    # run navigate on each start location
    results = map(lambda start: navigate(grid, start, end), starts)

    return min(results)

part1_distance = navigate(heightmap, start, end)
print(f'Part 1: {part1_distance}')

part2_distance = find_best_start(heightmap, end)
print(f'Part 2: {part2_distance}')
