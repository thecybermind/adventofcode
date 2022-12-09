def is_visible(row, col):
    global grid

    height = grid[row][col]
    blocked = 0
    # up
    for y in range(0, row):
        if grid[y][col] >= height:
            blocked += 1
            break
    # down
    for y in range(row + 1, len(grid)):
        if grid[y][col] >= height:
            blocked += 1
            break
    # left
    for x in range(0, col):
        if grid[row][x] >= height:
            blocked += 1
            break
    # right
    for x in range(col + 1, len(grid[row])):
        if grid[row][x] >= height:
            blocked += 1
            break

    return blocked < 4

def scenic_score(row, col):
    global grid
    
    height = grid[row][col]
    up = 0
    for r in range(row - 1, -1, -1):
        if grid[r][col] <= height:
            up += 1
            if grid[r][col] == height:
                break
    down = 0
    for r in range(row + 1, len(grid)):
        if grid[r][col] <= height:
            down += 1
            if grid[r][col] == height:
                break
    left = 0
    for c in range(col - 1, -1, -1):
        if grid[row][c] <= height:
            left += 1
            if grid[row][c] == height:
                break
    right = 0
    for c in range(col + 1, len(grid[row])):
        if grid[row][c] <= height:
            right += 1
            if grid[row][c] == height:
                break

    return up * down * left * right

grid = []
with open('input8.txt') as inp:
    for line in inp:
        line = line.strip()
        grid.append(line)

# start out including the entire top and bottom rows
total_visible = len(grid[0]) * 2
# add in 2 (left edge and right edge) for every line in the grid not including the top and bottom
total_visible += (len(grid) - 2) * 2

scenic_scores = []
# loop through all the non-edge locations
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        total_visible += is_visible(row, col)
        scenic_scores.append(scenic_score(row, col))

print(f'Part 1 total visible: {total_visible}')
max_scenic_score = max(scenic_scores)
print(f'Part 2 max scenic score: {max_scenic_score}')
