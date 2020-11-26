from collections import defaultdict
import sys

board = []
ROW = 4
COL = 10

sys.setrecursionlimit(9000)


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.paths = []

    # function to add an edge to graph
    def add_edged(self, u, v):
        self.graph[u].append(v)

    # Use BFS to check path between s and d
    def is_reachable(self, s, d):
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue
            n = queue.pop(0)
            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True
            #  Else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # If BFS is complete without visited d
        return False

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            self.paths.append([int(x) for x in path])
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

    def print_path(self):
        print(self.paths)

    def print_shortest_path(self):
        if len(self.paths) > 0:
            min_len = 999999
            index = 0
            for i in range(len(self.paths)):
                l = len(self.paths[i])
                if l < min_len:
                    min_len = l
                    index = i
            print(self.paths[index])
        else:
            print("No path found")


def is_in_the_board(x, y):
    return x >= 0 and x < ROW and y >= 0 and y < COL


def can_move_up(x, y):
    if is_in_the_board(x-1, y):
        if board[x-1][y] >= 0 and board[x-1][y] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_down(x, y):
    if is_in_the_board(x+1, y):
        if board[x+1][y] >= 0 and board[x+1][y] != 1:
            return True
    else:
        return False


def can_move_left(x, y):
    if is_in_the_board(x, y-1):
        if board[x][y-1] >= 0 and board[x][y-1] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_right(x, y):
    if is_in_the_board(x, y+1):
        if board[x][y+1] >= 0 and board[x][y+1] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_up_right(x, y):
    if is_in_the_board(x-1, y+1):
        if board[x-1][y+1] >= 0 and board[x-1][y+1] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_up_left(x, y):
    if is_in_the_board(x-1, y-1):
        if board[x-1][y-1] >= 0 and board[x-1][y-1] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_down_left(x, y):
    if is_in_the_board(x+1, y-1):
        if board[x+1][y-1] >= 0 and board[x+1][y-1] != 1:
            return True
        else:
            return False
    else:
        return False


def can_move_down_right(x, y):
    if is_in_the_board(x+1, y+1):
        if board[x+1][y+1] >= 0 and board[x+1][y+1] != 1:
            return True
        else:
            return False
    else:
        return False


def test():
    file = open('test_data.txt', 'r')
    for line in file:
        board.append([int(x) for x in line.split()])
    file.close()
    print(board)
    gr = Graph(ROW*COL)
    for row in range(ROW):
        for col in range(COL):
            print(row, col, (row*(ROW+1)+col))
            if (board[row][col] < 0 or board[row][col] == 1):
                continue
            if (can_move_left(row, col)):
                print("left")
                gr.add_edged(
                    row*(ROW+1) + col,
                    row*(ROW+1) + col-1)
                gr.add_edged(
                    row*(ROW+1) + col-1,
                    row*(ROW+1) + col)
            if (can_move_up(row, col)):
                print("up")
                gr.add_edged(
                    (row-1)*(ROW+1) + col,
                    row*(ROW+1) + col)
                gr.add_edged(
                    (row)*(ROW+1) + col,
                    (row-1)*(ROW+1) + col)
            if (can_move_right(row, col)):
                print("right")
                gr.add_edged(
                    row*(ROW+1) + col,
                    row*(ROW+1) + col+1)
                gr.add_edged(
                    row*(ROW+1) + col+1,
                    row*(ROW+1) + col)
            if (can_move_down(row, col)):
                print("down")
                gr.add_edged(
                    (row+1)*(ROW+1) + col,
                    row*(ROW+1) + col)
                gr.add_edged(
                    (row)*(ROW+1) + col,
                    (row+1)*(ROW+1) + col)
            if (can_move_up_right(row, col)):
                print("up-right")
                gr.add_edged(
                    row*(ROW+1) + col,
                    (row-1)*(ROW+1) + col+1)
                gr.add_edged(
                    (row-1)*(ROW+1) + col+1,
                    row*(ROW+1) + col)
            if (can_move_up_left(row, col)):
                print("up-left")
                gr.add_edged(
                    row*(ROW+1) + col,
                    (row-1)*(ROW+1) + col-1)
                gr.add_edged(
                    (row-1)*(ROW+1) + col-1,
                    row*(ROW+1) + col)
            if (can_move_down_left(row, col)):
                print("down_left")
                gr.add_edged(
                    row*(ROW+1) + col,
                    (row+1)*(ROW+1) + col-1)
                gr.add_edged(
                    (row+1)*(ROW+1) + col-1,
                    row*(ROW+1) + col)
            if (can_move_down_right(row, col)):
                print("down_right")
                gr.add_edged(
                    row*(ROW+1) + col,
                    (row+1)*(ROW+1) + col+1)
                gr.add_edged(
                    (row+1)*(ROW+1) + col+1,
                    row*(ROW+1) + col)
    s = 0
    d = 9
    print("Shortest path from ({},{}) to ({},{}) is:".format(
        s % COL, int(s/(ROW+1)), d % COL, int(d/(ROW+1))))
    gr.printAllPaths(s, d)
    # gr.print_path()
    gr.print_shortest_path()


if __name__ == '__main__':
    test()
