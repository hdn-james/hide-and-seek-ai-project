import sys
import threading


class Backtracking:
    def __init__(self, px=0, py=0, row=0, col=0, state=1, board_id=1):
        self.state = state
        self.board_id = board_id
        self.counter = 0
        self.px = px
        self.py = py
        self.move_x = [0, -1, -1, -1, 0, 1, 1, 1]
        self.move_y = [1, 1, 0, -1, -1, -1, 0, 1]
        self.board = []
        with open('raw_data/board_'+str(self.board_id)+'/result/result_'+str(self.state)+'.txt', 'r') as file:
            for line in file:
                self.board.append([int(x) for x in line.split()])
            file.close()
        self.row = len(self.board)
        self.col = len(self.board[0])
        for row in range(self.row):
            for col in range(self.col):
                if self.board[row][col] == 3:
                    self.px = row
                    self.py = col
        print(self.row, self.col, self.px, self.py)
        print(self.board)

    def is_safe(self, x, y):
        return x >= 0 and x < self.row and y >= 0 and y < self.col and self.board[x][y] >= 0 and self.board[x][y] != 1

    def outputSolution(self):
        self.state += 1
        with open('raw_data/board_'+str(self.board_id)+'/result/result_'+str(self.state)+'.txt', 'w') as file:
            for i in range(self.row):
                for j in range(self.col):
                    file.write("{} ".format(self.board[i][j]))
                file.write('\n')
            file.close()

    def solutions(self):
        self.board[self.px][self.py] = 100
        pos = 101
        if(not self.solutionUtil(self.px, self.py, pos)):
            return False
        else:
            return True

    def solutionUtil(self, curr_x, curr_y, pos):
        # for row in range(self.row):
        #     for col in range(self.col):
        #         if (self.board[row][col] == 42):
        #             return True
        if (pos == 150):
            return True
        for i in range(8):
            new_x = curr_x + self.move_x[i]
            new_y = curr_y + self.move_y[i]
            if self.is_safe(new_x, new_y):
                self.counter += 1
                self.board[new_x][new_y] = pos
                if self.solutionUtil(new_x, new_y, pos+1):
                    return True
                self.board[new_x][new_y] = 0
        return False

    def load_from_current_state(self):
        self.board.clear()
        with open('raw_data/board_'+str(self.board_id)+'/result/result_'+str(self.state)+'txt', 'r') as file:
            for line in file:
                self.board.append([int(x) for x in line.split()])
            file.close()


def main():
    backtrack = Backtracking(0,0,8,10,1,1)
    found = backtrack.solutions()
    if found:
        backtrack.outputSolution()


if __name__ == '__main__':
    sys.setrecursionlimit(50000)
    main()
