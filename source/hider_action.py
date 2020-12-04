import sight_processing
import collections
import player


class HiderAction:
    def __init__(self, board=1, row=0, column=0, hider=1):
        self.__board = board
        self.__hider = hider
        self.__row = row
        self.__col = column
        self.__map = []
        self.__path_to_result = 'raw_data/board_' + \
            str(self.__board) + '/result/result_' + str(player.state) + '.txt'
        with open(self.__path_to_result, 'r') as f:
            for line in f:
                self.__map.append([int(x) for x in line.split()])
            f.close()

    def __move_up(self, x, y):
        if self.__map[x-1][y] == 42 or self.__map[x-1][y] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x-1][y] = 2
        self.__map[x][y] = 0

    def __move_down(self, x, y):
        if self.__map[x+1][y] == 42 or self.__map[x+1][y] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x+1][y] = 2
        self.__map[x][y] = 0

    def __move_left(self, x, y):
        if self.__map[x][y-1] == 42 or self.__map[x][y-1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x][y-1] = 2
        self.__map[x][y] = 0

    def __move_right(self, x, y):
        if self.__map[x][y+1] == 42 or self.__map[x][y+1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x][y+1] = 2
        self.__map[x][y] = 0

    def __move_up_right(self, x, y):
        if self.__map[x-1][y+1] == 42 or self.__map[x-1][y+1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x-1][y+1] = 2
        self.__map[x][y] = 0

    def __move_up_left(self, x, y):
        if self.__map[x-1][y-1] == 42 or self.__map[x-1][y-1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x-1][y-1] = 2
        self.__map[x][y] = 0

    def __move_down_left(self, x, y):
        if self.__map[x+1][y-1] == 42 or self.__map[x+1][y-1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x+1][y-1] = 2
        self.__map[x][y] = 0

    def __move_down_right(self, x, y):
        if self.__map[x+1][y+1] == 42 or self.__map[x+1][y+1] == 2:
            self.__hider -= 1
            print("hider count: {}".format(self.__hider))
        self.__map[x+1][y+1] = 2
        self.__map[x][y] = 0

    def __write_to_result(self, state):
        file = open('raw_data/board_' + str(self.__board) +
                    '/result/result_' + str(state) + '.txt', 'w')
        for i in range(self.__row):
            for j in range(self.__col):
                file.write('{} '.format(self.__map[i][j]))
            file.write('\n')
        file.close()

    def __read_from_current_state(self, state):
        self.__map.clear()
        with open('raw_data/board_' + str(self.__board) + '/result/result_' + str(state) + '.txt', 'r') as f:
            for line in f:
                self.__map.append([int(x) for x in line.split()])
            f.close()

    def __move_decider(self, x, y, target):
        move = []
        path = player.bfs(self.__map, self.__row, self.__col, x, y, target)
        for i in range(len(path)-1):
            if path[i+1][0] - path[i][0] == 0 and path[i+1][1] - path[i][1] == 1:
                move.append(1)
            elif path[i+1][0] - path[i][0] == -1 and path[i+1][1] - path[i][1] == 1:
                move.append(2)
            elif path[i+1][0] - path[i][0] == -1 and path[i+1][1] - path[i][1] == 0:
                move.append(3)
            elif path[i+1][0] - path[i][0] == -1 and path[i+1][1] - path[i][1] == -1:
                move.append(4)
            elif path[i+1][0] - path[i][0] == 0 and path[i+1][1] - path[i][1] == -1:
                move.append(5)
            elif path[i+1][0] - path[i][0] == 1 and path[i+1][1] - path[i][1] == -1:
                move.append(6)
            elif path[i+1][0] - path[i][0] == 1 and path[i+1][1] - path[i][1] == 0:
                move.append(7)
            elif path[i+1][0] - path[i][0] == 1 and path[i+1][1] - path[i][1] == 1:
                move.append(8)
        return move

    def __move(self, x, y, target, state_cur):
        move = self.__move_decider(x, y, target)
        for m in move:
            state_cur += 1
            if m == 1:
                self.__move_right(x, y)
                y += 1
                self.__write_to_result(state_cur)
            elif m == 2:
                self.__move_up_right(x, y)
                x -= 1
                y += 1
                self.__write_to_result(state_cur)
            elif m == 3:
                self.__move_up(x, y)
                x -= 1
                self.__write_to_result(state_cur)
            elif m == 4:
                self.__move_up_left(x, y)
                x -= 1
                y -= 1
                self.__write_to_result(state_cur)
            elif m == 5:
                self.__move_left(x, y)
                y -= 1
                self.__write_to_result(state_cur)
            elif m == 6:
                self.__move_down_left(x, y)
                x += 1
                y -= 1
                self.__write_to_result(state_cur)
            elif m == 7:
                self.__move_down(x, y)
                x += 1
                self.__write_to_result(state_cur)
            elif m == 8:
                self.__move_down_right(x, y)
                x += 1
                y += 1
                self.__write_to_result(state_cur)
            self.__read_from_current_state(player.state)
        return state_cur, x, y

    def __get_to_target(self, x, y, target):
        move = self.__move(x, y, target, player.state)
        player.state, x, y = move[0], move[1], move[2]
        return (x, y)
