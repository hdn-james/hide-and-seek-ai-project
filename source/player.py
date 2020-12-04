import collections

row_num = [0, -1, -1, -1, 0, 1, 1, 1]
col_num = [1, 1, 0, -1, -1, -1, 0, 1]

state = 1

def is_safe(maps, row, col, x, y):
        return x >= 0 and x < row and y >= 0 and y < col and maps[x][y] >= 0 and maps[x][y] != 1

def bfs(maps, row, col, x, y, target):
    queue = collections.deque([[(x, y)]])
    seen = [(x, y)]
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if target[0] - x == 0 and target[1] - y == 0:
            return path
        for i in range(8):
            x2 = x + row_num[i]
            y2 = y + col_num[i]
            if is_safe(maps, row, col, x2, y2) and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.append((x2, y2))
    return seen
