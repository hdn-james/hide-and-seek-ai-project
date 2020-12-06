import collections

row_num = [0, -1, -1, -1, 0, 1, 1, 1]
col_num = [1, 1, 0, -1, -1, -1, 0, 1]

row_around = [
    0, 0, 0, 0, 0, 0, -1, -2, -1, 1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1, 1, 2, 3, -2, -2, -2, -2, -3, -3, -3, -3, -1, -1, -1, -1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1]
col_around = [
    -1, -2, -1, 1, 2, 3, 0, 0, 0, 0, 0, 0, -3, -2, -1, -3, -2, -1, 1, 2, 3, 1, 2, 3, 1, 3, -1, -3, 1, 2, -1, -2, 2, 3, -2, -3, 1, 3, -1, -3, 1, 2, -1, -2, 2, 3, -2, -3]

state = 1
hider = 0
row = 0
column = 0
step_limit = 500
level = 0


def is_safe(maps, x, y):
    return x >= 0 and x < row and y >= 0 and y < column and maps[x][y] >= 0 and maps[x][y] != 1


def is_safe_hider(maps, x, y):
    return x >= 0 and x < row and y >= 0 and y < column and maps[x][y] >= 0 and maps[x][y] != 1 and maps[x][y] != 2 and maps[x][y] != 42 and maps[x][y] != 3

def is_safe_hider_announce(maps, x, y):
    return x >= 0 and x < row and y >= 0 and y < column and maps[x][y] >= 0 and maps[x][y] != 1 and maps[x][y] != 2 and maps[x][y] != 42 and maps[x][y] != 5 and maps[x][y] != 45 and maps[x][y] != 3


def bfs(maps, x, y, target, mode):
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
            if mode == 'seeker':
                if is_safe(maps, x2, y2) and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.append((x2, y2))
            elif mode == 'hider':
                if is_safe_hider(maps, x2, y2) and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.append((x2, y2))
    return seen
