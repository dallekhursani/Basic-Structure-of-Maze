# Maze representation
# 0 - path
# 1 - wall
# S - start (we'll mark it as 2)
# E - end (we'll mark it as 3)

maze = [
    [2, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 3]
]

# Dimensions
rows = len(maze)
cols = len(maze[0])

# Direction vectors: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Find start and end positions
start = end = None
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 2:
            start = (i, j)
        elif maze[i][j] == 3:
            end = (i, j)

# DFS to find path
path = []
visited = set()

def dfs(x, y):
    if (x, y) == end:
        path.append((x, y))
        return True
    if (x < 0 or x >= rows or y < 0 or y >= cols or
        maze[x][y] == 1 or (x, y) in visited):
        return False

    visited.add((x, y))
    path.append((x, y))

    for dx, dy in directions:
        if dfs(x + dx, y + dy):
            return True

    path.pop()
    return False

# Run DFS
if dfs(*start):
    print("Path found:")
    print(path)
else:
    print("No path found.")

