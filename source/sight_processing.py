import player

class SightProcessing:
    def __init__(self, board=1, state=1):
        self.__board = board
        self.__map = []
        self.__state = state
        self.__seeker_sight = [
            [(0, -1), (0, -2), (0, -3)],
            [(0, 1), (0, 2), (0, 3)],
            [(-1, 0), (-2, 0), (-3, 0)],
            [(1, 0), (2, 0), (3, 0)],
            [(1, -1), (2, -2), (3, -3)],
            [(-1, -1), (-2, -2), (-3, -3)],
            [(-1, 1), (-2, 2), (-3, 3)],
            [(1, 1), (2, 2), (3, 3)]]
        self.__path_to_result_1 = 'raw_data/board_' + \
            str(self.__board) + '/result/result_' + str(self.__state) + '.txt'
        with open('raw_data/board_' + str(self.__board) + '/result/result_' + str(self.__state) + '.txt', 'r') as file:
            for line in file:
                self.__map.append([int(x) for x in line.split()])
            file.close()

    def __is_out_of_the_board(self, x, y):
        return (x < 0) or (y < 0) or (x >= player.row) or (y >= player.column)

    def __sight_check(self, x, y):
        for i in self.__seeker_sight:
            for j in i:
                if not self.__is_out_of_the_board(x+j[0], y+j[1]):
                    if self.__map[x+j[0]][y+j[1]] == 1 or self.__map[x+j[0]][y+j[1]] < 0:
                        break
                    else:
                        if self.__map[x+j[0]][y+j[1]] == 2 or self.__map[x+j[0]][y+j[1]] == 42:
                            self.__map[x+j[0]][y+j[1]] = 42
                        elif self.__map[x+j[0]][y+j[1]] == 5 or self.__map[x+j[0]][y+j[1]] == 45:
                            self.__map[x+j[0]][y+j[1]] = 45
                        else:
                            self.__map[x+j[0]][y+j[1]] = 4
        #   [(-1, 2), (-2, 1)]
        if not self.__is_out_of_the_board(x, y+1) and not self.__is_out_of_the_board(x-1, y+1):
            if not self.__is_out_of_the_board(x-1, y+2) and self.__map[x-1][y+2] != 1 and self.__map[x-1][y+2] >= 0:
                if (self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0) and (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0):
                    if self.__map[x-1][y+2] == 42 or self.__map[x-1][y+2] == 2:
                        self.__map[x-1][y+2] = 42
                    elif self.__map[x-1][y+2] == 45 or self.__map[x-1][y+2] == 5:
                        self.__map[x-1][y+2] = 45
                    else:
                        self.__map[x-1][y+2] = 4
                elif (self.__map[x][y+1] == 1 or self.__map[x][y+1] < 0) and (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0) or \
                    (self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0) and (self.__map[x-1][y+1] == 1 or self.__map[x-1][y+1] < 0):
                    if self.__map[x-1][y+2] == 42 or self.__map[x-1][y+2] == 2:
                        self.__map[x-1][y+2] = 42
                    elif self.__map[x-1][y+2] == 45 or self.__map[x-1][y+2] == 5:
                        self.__map[x-1][y+2] = 45
                    else:
                        self.__map[x-1][y+2] = 4
        if not self.__is_out_of_the_board(x-1, y) and not self.__is_out_of_the_board(x-1, y+1):
            if not self.__is_out_of_the_board(x-2, y+1) and self.__map[x-2][y+1] != 1 and self.__map[x-2][y+1] >= 0:
                if (self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0) and (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0):
                    if self.__map[x-2][y+1] == 42 or self.__map[x-2][y+1] == 2:
                        self.__map[x-2][y+1] = 42
                    elif self.__map[x-2][y+1] == 45 or self.__map[x-2][y+1] == 5:
                        self.__map[x-2][y+1] = 45
                    else:
                        self.__map[x-2][y+1] = 4
                elif (self.__map[x-1][y] == 1 or self.__map[x-1][y] < 0) and (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0) or \
                    (self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0) and (self.__map[x-1][y+1] == 1 or self.__map[x-1][y+1] < 0):
                    if self.__map[x-2][y+1] == 42 or self.__map[x-2][y+1] == 2:
                        self.__map[x-2][y+1] = 42
                    elif self.__map[x-2][y+1] == 45 or self.__map[x-2][y+1] == 5:
                        self.__map[x-2][y+1] = 45
                    else:
                        self.__map[x-2][y+1] = 4
        #   [(-2, -1), (-1, -2)]
        if not self.__is_out_of_the_board(x-1, y) and not self.__is_out_of_the_board(x-1, y-1):
            if not self.__is_out_of_the_board(x-2, y-1) and self.__map[x-2][y-1] != 1 and self.__map[x-2][y-1] >= 0:
                if (self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0) and (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0):
                    if self.__map[x-2][y-1] == 42 or self.__map[x-2][y-1] == 2:
                        self.__map[x-2][y-1] = 42
                    elif self.__map[x-2][y-1] == 45 or self.__map[x-2][y-1] == 5:
                        self.__map[x-2][y-1] = 45
                    else:
                        self.__map[x-2][y-1] = 4
                elif (self.__map[x-1][y] == 1 or self.__map[x-1][y] < 0) and (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0) or \
                    (self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0) and (self.__map[x-1][y-1] == 1 or self.__map[x-1][y-1] < 0):
                    if self.__map[x-2][y-1] == 42 or self.__map[x-2][y-1] == 2:
                        self.__map[x-2][y-1] = 42
                    elif self.__map[x-2][y-1] == 45 or self.__map[x-2][y-1] == 5:
                        self.__map[x-2][y-1] = 45
                    else:
                        self.__map[x-2][y-1] = 4
        if not self.__is_out_of_the_board(x, y-1) and not self.__is_out_of_the_board(x-1, y-1):
            if not self.__is_out_of_the_board(x-1, y-2) and self.__map[x-1][y-2] != 1 and self.__map[x-1][y-2] >= 0:
                if (self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0) and (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0):
                    if self.__map[x-1][y-2] == 42 or self.__map[x-1][y-2] == 2:
                        self.__map[x-1][y-2] = 42
                    elif self.__map[x-1][y-2] == 45 or self.__map[x-1][y-2] == 5:
                        self.__map[x-1][y-2] = 45
                    else:
                        self.__map[x-1][y-2] = 4
                elif (self.__map[x][y-1] == 1 or self.__map[x][y-1] < 0) and (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0) or \
                    (self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0) and (self.__map[x-1][y-1] == 1 or self.__map[x-1][y-1] < 0):
                    if self.__map[x-1][y-2] == 42 or self.__map[x-1][y-2] == 2:
                        self.__map[x-1][y-2] = 42
                    elif self.__map[x-1][y-2] == 45 or self.__map[x-1][y-2] == 5:
                        self.__map[x-1][y-2] = 45
                    else:
                        self.__map[x-1][y-2] = 4
        #   [(1, -2), (2, -1)]
        if not self.__is_out_of_the_board(x, y-1) and not self.__is_out_of_the_board(x+1, y-1):
            if not self.__is_out_of_the_board(x+1, y-2) and self.__map[x+1][y-2] != 1 and self.__map[x+1][y-2] >= 0:
                if (self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0) and (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0):
                    if self.__map[x+1][y-2] == 42 or self.__map[x+1][y-2] == 2:
                        self.__map[x+1][y-2] = 42
                    elif self.__map[x+1][y-2] == 45 or self.__map[x+1][y-2] == 5:
                        self.__map[x+1][y-2] = 45
                    else:
                        self.__map[x+1][y-2] = 4
                elif (self.__map[x][y-1] == 1 or self.__map[x][y-1] < 0) and (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0) or \
                    (self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0) and (self.__map[x+1][y-1] == 1 or self.__map[x+1][y-1] < 0):
                    if self.__map[x+1][y-2] == 42 or self.__map[x+1][y-2] == 2:
                        self.__map[x+1][y-2] = 42
                    elif self.__map[x+1][y-2] == 45 or self.__map[x+1][y-2] == 5:
                        self.__map[x+1][y-2] = 45
                    else:
                        self.__map[x+1][y-2] = 4
        if not self.__is_out_of_the_board(x+1, y) and not self.__is_out_of_the_board(x+1, y-1):
            if not self.__is_out_of_the_board(x+2, y-1) and self.__map[x+2][y-1] != 1 and self.__map[x+2][y-1] >= 0:
                if (self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0) and (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0):
                    if self.__map[x+2][y-1] == 42 or self.__map[x+2][y-1] == 2:
                        self.__map[x+2][y-1] = 42
                    elif self.__map[x+2][y-1] == 45 or self.__map[x+2][y-1] == 5:
                        self.__map[x+2][y-1] = 45
                    else:
                        self.__map[x+2][y-1] = 4
                elif (self.__map[x+1][y] == 1 or self.__map[x+1][y] < 0) and (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0) or \
                    (self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0) and (self.__map[x+1][y-1] == 1 or self.__map[x+1][y-1] < 0):
                    if self.__map[x+2][y-1] == 42 or self.__map[x+2][y-1] == 2:
                        self.__map[x+2][y-1] = 42
                    elif self.__map[x+2][y-1] == 45 or self.__map[x+2][y-1] == 5:
                        self.__map[x+2][y-1] = 45
                    else:
                        self.__map[x+2][y-1] = 4
        #   [(2, 1), (1, 2)]
        if not self.__is_out_of_the_board(x+1, y) and not self.__is_out_of_the_board(x+1, y+1):
            if not self.__is_out_of_the_board(x+2, y+1) and self.__map[x+2][y+1] != 1 and self.__map[x+1][y+1] >= 0:
                if (self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0) and (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0):
                    if self.__map[x+2][y+1] == 42 or self.__map[x+2][y+1] == 2:
                        self.__map[x+2][y+1] = 42
                    elif self.__map[x+2][y+1] == 45 or self.__map[x+2][y+1] == 5:
                        self.__map[x+2][y+1] = 45
                    else:
                        self.__map[x+2][y+1] = 4
                elif (self.__map[x+1][y] == 1 or self.__map[x+1][y] < 0) and (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0) or \
                    (self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0) and (self.__map[x+1][y+1] == 1 or self.__map[x+1][y+1] < 0):
                    if self.__map[x+2][y+1] == 42 or self.__map[x+2][y+1] == 2:
                        self.__map[x+2][y+1] = 42
                    elif self.__map[x+2][y+1] == 45 or self.__map[x+2][y+1] == 5:
                        self.__map[x+2][y+1] = 45
                    else:
                        self.__map[x+2][y+1] = 4
        if not self.__is_out_of_the_board(x, y+1) and not self.__is_out_of_the_board(x+1, y+1):
            if not self.__is_out_of_the_board(x+1, y+2) and self.__map[x+1][y+2] != 1 and self.__map[x+1][y+2] >= 0:
                if (self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0) and (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0):
                    if self.__map[x+1][y+2] == 42 or self.__map[x+1][y+2] == 2:
                        self.__map[x+1][y+2] = 42
                    elif self.__map[x+1][y+2] == 45 or self.__map[x+1][y+2] == 5:
                        self.__map[x+1][y+2] = 45
                    else:
                        self.__map[x+1][y+2] = 4
                elif (self.__map[x][y+1] == 1 or self.__map[x][y+1] < 0) and (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0) or \
                    (self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0) and (self.__map[x+1][y+1] == 1 or self.__map[x+1][y+1] < 0):
                    if self.__map[x+1][y+2] == 42 or self.__map[x+1][y+2] == 2:
                        self.__map[x+1][y+2] = 42
                    elif self.__map[x+1][y+2] == 45 or self.__map[x+1][y+2] == 5:
                        self.__map[x+1][y+2] = 45
                    else:
                        self.__map[x+1][y+2] = 4
        # right_sight_1 [(0, 1), (-1, 3), (1, 3)]
        if not self.__is_out_of_the_board(x, y+1):
            if not self.__is_out_of_the_board(x-1, y+3) and self.__map[x-1][y+3] != 1 and self.__map[x-1][y+3] >= 0:
                if self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0:
                    if (self.__map[x][y+2] != 1 and self.__map[x][y+2] >= 0) and (self.__map[x-1][y+2] != 1 and self.__map[x-1][y+2] >= 0):
                        if self.__map[x-1][y+3] == 2 or self.__map[x-1][y+3] == 42:
                            self.__map[x-1][y+3] = 42  # right sight 1 up
                        elif self.__map[x-1][y+3] == 5 or self.__map[x-1][y+3] == 45:
                            self.__map[x-1][y+3] = 45
                        else:
                            self.__map[x-1][y+3] = 4
                    elif (self.__map[x][y+2] == 1 or self.__map[x][y+2] < 0) and (self.__map[x-1][y+2] != 1 and self.__map[x-1][y+2] >= 0) or \
                            (self.__map[x][y+2] != 1 and self.__map[x][y+2] >= 0) and (self.__map[x-1][y+2] == 1 or self.__map[x-1][y+2] < 0):
                        if self.__map[x-1][y+3] == 2 or self.__map[x-1][y+3] == 42:
                            self.__map[x-1][y+3] = 42  # right sight 1 up
                        elif self.__map[x-1][y+3] == 5 or self.__map[x-1][y+3] == 45:
                            self.__map[x-1][y+3] = 45
                        else:
                            self.__map[x-1][y+3] = 4
            if not self.__is_out_of_the_board(x+1, y+3) and self.__map[x+1][y+3] != 1 and self.__map[x+1][y+3] >= 0:
                if self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0:
                    if (self.__map[x][y+2] != 1 and self.__map[x][y+2] >= 0) and (self.__map[x+1][y+2] != 1 and self.__map[x+1][y+2] >= 0):
                        if self.__map[x+1][y+3] == 2 or self.__map[x+1][y+3] == 42:
                            self.__map[x+1][y+3] = 42  # right sight 1 down
                        elif self.__map[x+1][y+3] == 5 or self.__map[x+1][y+3] == 45:
                            self.__map[x+1][y+3] = 45
                        else:
                            self.__map[x+1][y+3] = 4
                    elif (self.__map[x][y+2] == 1 or self.__map[x][y+2] < 0) and (self.__map[x+1][y+2] != 1 and self.__map[x+1][y+2] >= 0) or \
                            (self.__map[x][y+2] != 1 and self.__map[x][y+2] >= 0) and (self.__map[x+1][y+2] == 1 or self.__map[x+1][y+2] < 0):
                        if self.__map[x+1][y+3] == 2 or self.__map[x+1][y+3] == 42:
                            self.__map[x+1][y+3] = 42  # right sight 1 down
                        elif self.__map[x+1][y+3] == 5 or self.__map[x+1][y+3] == 45:
                            self.__map[x+1][y+3] = 45
                        else:
                            self.__map[x+1][y+3] = 4
        # left_sight_1 [(0, -1), (-1, -3), (1, -3)]
        if not self.__is_out_of_the_board(x, y-1):
            if not self.__is_out_of_the_board(x-1, y-3) and self.__map[x-1][y-3] != 1 and self.__map[x-1][y-3] >= 0:
                if self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0:
                    if (self.__map[x][y-2] != 1 and self.__map[x][y-2] >= 0) and (self.__map[x-1][y-2] != 1 and self.__map[x-1][y-2] >= 0):
                        if self.__map[x-1][y-3] == 2 or self.__map[x-1][y-3] == 42:
                            self.__map[x-1][y-3] = 42  # left sight 1 up
                        elif self.__map[x-1][y-3] == 5 or self.__map[x-1][y-3] == 45:
                            self.__map[x-1][y-3] = 45
                        else:
                            self.__map[x-1][y-3] = 4
                    elif (self.__map[x][y-2] == 1 or self.__map[x][y-2] < 0) and (self.__map[x-1][y-2] != 1 and self.__map[x-1][y-2] >= 0) or \
                            (self.__map[x][y-2] != 1 and self.__map[x][y-2] >= 0) and (self.__map[x-1][y-2] == 1 or self.__map[x-1][y-2] < 0):
                        if self.__map[x-1][y-3] == 2 or self.__map[x-1][y-3] == 42:
                            self.__map[x-1][y-3] = 42  # left sight 1 up
                        elif self.__map[x-1][y-3] == 5 or self.__map[x-1][y-3] == 45:
                            self.__map[x-1][y-3] = 45
                        else:
                            self.__map[x-1][y-3] = 4
            if not self.__is_out_of_the_board(x+1, y-3) and self.__map[x+1][y-3] != 1 and self.__map[x+1][y-3] >= 0:
                if self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0:
                    if (self.__map[x][y-2] != 1 and self.__map[x][y-2] >= 0) and (self.__map[x+1][y-2] != 1 and self.__map[x+1][y-2] >= 0):
                        if self.__map[x+1][y-3] == 2 or self.__map[x+1][y-3] == 42:
                            self.__map[x+1][y-3] = 42  # left sight 1 down
                        elif self.__map[x+1][y-3] == 5 or self.__map[x+1][y-3] == 45:
                            self.__map[x+1][y-3] = 45
                        else:
                            self.__map[x+1][y-3] = 4
                    elif (self.__map[x][y-2] != 1 and self.__map[x][y-2] >= 0) and (self.__map[x+1][y-2] == 1 or self.__map[x+1][y-2] < 0) or \
                            (self.__map[x][y-2] == 1 or self.__map[x][y-2] < 0) and (self.__map[x+1][y-2] != 1 and self.__map[x+1][y-2] >= 0):
                        if self.__map[x+1][y-3] == 2 or self.__map[x+1][y-3] == 42:
                            self.__map[x+1][y-3] = 42  # left sight 1 down
                        elif self.__map[x+1][y-3] == 5 or self.__map[x+1][y-3] == 45:
                            self.__map[x+1][y-3] = 45
                        else:
                            self.__map[x+1][y-3] = 4
        # up sight 1 [(-1, 0), (-3, -1), (-3, 1)]
        if not self.__is_out_of_the_board(x-1, y):
            if not self.__is_out_of_the_board(x-3, y-1) and self.__map[x-3][y-1] != 1 and self.__map[x-3][y-1] >= 0:
                if self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0:
                    if (self.__map[x-2][y] != 1 and self.__map[x-2][y] >= 0) and (self.__map[x-2][y-1] != 1 and self.__map[x-2][y-1] >= 0):
                        if self.__map[x-3][y-1] == 2 or self.__map[x-3][y-1] == 42:
                            self.__map[x-3][y-1] = 42  # up sight 1 left
                        elif self.__map[x-3][y-1] == 5 or self.__map[x-3][y-1] == 45:
                            self.__map[x-3][y-1] = 45
                        else:
                            self.__map[x-3][y-1] = 4
                    elif (self.__map[x-2][y] == 1 or self.__map[x-2][y] < 0) and (self.__map[x-2][y-1] != 1 and self.__map[x-2][y-1] >= 0) or \
                            (self.__map[x-2][y] != 1 and self.__map[x-2][y] >= 0) and (self.__map[x-2][y-1] == 1 or self.__map[x-2][y-1] < 0):
                        if self.__map[x-3][y-1] == 2 or self.__map[x-3][y-1] == 42:
                            self.__map[x-3][y-1] = 42  # up sight 1 left
                        elif self.__map[x-3][y-1] == 5 or self.__map[x-3][y-1] == 45:
                            self.__map[x-3][y-1] = 45
                        else:
                            self.__map[x-3][y-1] = 4
            if not self.__is_out_of_the_board(x-3, y+1) and self.__map[x-3][y+1] != 1 and self.__map[x-3][y+1] >= 0:
                if self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0:
                    if (self.__map[x-2][y] != 1 and self.__map[x-2][y] >= 0) and (self.__map[x-2][y+1] != 1 and self.__map[x-2][y+1] >= 0):
                        if self.__map[x-3][y+1] == 2 or self.__map[x-3][y+1] == 42:
                            self.__map[x-3][y+1] = 42  # up sight 1 right
                        elif self.__map[x-3][y+1] == 5 or self.__map[x-3][y+1] == 45:
                            self.__map[x-3][y+1] = 45
                        else:
                            self.__map[x-3][y+1] = 4
                    elif (self.__map[x-2][y] == 1 or self.__map[x-2][y] < 0) and (self.__map[x-2][y+1] != 1 and self.__map[x-2][y+1] >= 0) or \
                            (self.__map[x-2][y] != 1 and self.__map[x-2][y] >= 0) and (self.__map[x-2][y+1] == 1 or self.__map[x-2][y+1] < 0):
                        if self.__map[x-3][y+1] == 2 or self.__map[x-3][y+1] == 42:
                            self.__map[x-3][y+1] = 42  # up sight 1 right
                        elif self.__map[x-3][y+1] == 5 or self.__map[x-3][y+1] == 45:
                            self.__map[x-3][y+1] = 45
                        else:
                            self.__map[x-3][y+1] = 4
        # down sight 1 [(1, 0), (3, -1), (3, 1)]
        if not self.__is_out_of_the_board(x+1, y):
            if not self.__is_out_of_the_board(x+3, y-1) and self.__map[x+3][y-1] != 1 and self.__map[x+3][y-1] >= 0:
                if self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0:
                    if (self.__map[x+2][y] != 1 and self.__map[x+2][y] >= 0) and (self.__map[x+2][y-1] != 1 and self.__map[x+2][y-1] >= 0):
                        if self.__map[x+3][y-1] == 2 or self.__map[x+3][y-1] == 42:
                            self.__map[x+3][y-1] = 42  # down sight 1 left
                        elif self.__map[x+3][y-1] == 5 or self.__map[x+3][y-1] == 45:
                            self.__map[x+3][y-1] = 45
                        else:
                            self.__map[x+3][y-1] = 4
                    elif (self.__map[x+2][y] == 1 or self.__map[x+2][y] < 0) and (self.__map[x+2][y-1] != 1 and self.__map[x+2][y-1] >= 0) or \
                            (self.__map[x+2][y] != 1 and self.__map[x+2][y] >= 0) and (self.__map[x+2][y-1] == 1 or self.__map[x+2][y-1] < 0):
                        if self.__map[x+3][y-1] == 2 or self.__map[x+3][y-1] == 42:
                            self.__map[x+3][y-1] = 42  # down sight 1 left
                        elif self.__map[x+3][y-1] == 5 or self.__map[x+3][y-1] == 45:
                            self.__map[x+3][y-1] = 45
                        else:
                            self.__map[x+3][y-1] = 4
            if not self.__is_out_of_the_board(x+3, y+1) and self.__map[x+3][y+1] != 1 and self.__map[x+3][y+1] >= 0:
                if self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0:
                    if (self.__map[x+2][y] != 1 and self.__map[x+2][y] >= 0) and (self.__map[x+2][y+1] != 1 and self.__map[x+2][y+1] >= 0):
                        if self.__map[x+3][y+1] == 2 or self.__map[x+3][y+1] == 42:
                            self.__map[x+3][y+1] = 42  # down sight 1 right
                        elif self.__map[x+3][y+1] == 5 or self.__map[x+3][y+1] == 45:
                            self.__map[x+3][y+1] = 45
                        else:
                            self.__map[x+3][y+1] = 4
                    elif (self.__map[x+2][y] == 1 or self.__map[x+2][y] < 0) and (self.__map[x+2][y+1] != 1 and self.__map[x+2][y+1] >= 0) or \
                            (self.__map[x+2][y] != 1 and self.__map[x+2][y] >= 0) and (self.__map[x+2][y+1] == 1 or self.__map[x+2][y+1] < 0):
                        if self.__map[x+3][y+1] == 2 or self.__map[x+3][y+1] == 42:
                            self.__map[x+3][y+1] = 42  # down sight 1 right
                        elif self.__map[x+3][y+1] == 5 or self.__map[x+3][y+1] == 45:
                            self.__map[x+3][y+1] = 45
                        else:
                            self.__map[x+3][y+1] = 4
        # up right sight 2 [(-1, 1), (-3, 2), (-2, 3)]
        if not self.__is_out_of_the_board(x-1, y+1):
            if (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0):
                if not self.__is_out_of_the_board(x-3, y+2) and self.__map[x-3][y+2] != 1 and self.__map[x-3][y+2] >= 0:
                    if (self.__map[x-2][y+1] != 1 and self.__map[x-2][y+1] >= 0) and (self.__map[x-2][y+2] != 1 and self.__map[x-2][y+2] >= 0):
                        if self.__map[x-3][y+2] == 2 or self.__map[x-3][y+2] == 42:
                            self.__map[x-3][y+2] = 42
                        elif self.__map[x-3][y+2] == 5 or self.__map[x-3][y+2] == 45:
                            self.__map[x-3][y+2] = 45
                        else:
                            self.__map[x-3][y+2] = 4
                    elif (self.__map[x-2][y+1] != 1 and self.__map[x-2][y+1] >= 0) and (self.__map[x-2][y+2] == 1 or self.__map[x-2][y+2] < 0) or \
                            (self.__map[x-2][y+1] == 1 or self.__map[x-2][y+1] < 0) and (self.__map[x-2][y+2] != 1 and self.__map[x-2][y+2] >= 0):
                        if self.__map[x-3][y+2] == 2 or self.__map[x-3][y+2] == 42:
                            self.__map[x-3][y+2] = 42
                        elif self.__map[x-3][y+2] == 5 or self.__map[x-3][y+2] == 45:
                            self.__map[x-3][y+2] = 45
                        else:
                            self.__map[x-3][y+2] = 4
                if not self.__is_out_of_the_board(x-2, y+3) and self.__map[x-2][y+3] != 1 and self.__map[x-2][y+3] >= 0:
                    if (self.__map[x-2][y+2] != 1 and self.__map[x-2][y+2] >= 0) and (self.__map[x-1][y+2] != 1 and self.__map[x-1][y+2] >= 0):
                        if self.__map[x-2][y+3] == 2 or self.__map[x-2][y+3] == 42:
                            self.__map[x-2][y+3] = 42
                        elif self.__map[x-2][y+3] == 5 or self.__map[x-2][y+3] == 45:
                            self.__map[x-2][y+3] = 45
                        else:
                            self.__map[x-2][y+3] = 4
                    elif (self.__map[x-2][y+2] == 1 or self.__map[x-2][y+2] < 0) and (self.__map[x-1][y+2] != 1 and self.__map[x-1][y+2] >= 0) or \
                            (self.__map[x-2][y+2] != 1 and self.__map[x-2][y+2] >= 0) and (self.__map[x-1][y+2] == 1 or self.__map[x-1][y+2] < 0):
                        if self.__map[x-2][y+3] == 2 or self.__map[x-2][y+3] == 42:
                            self.__map[x-2][y+3] = 42
                        elif self.__map[x-2][y+3] == 5 or self.__map[x-2][y+3] == 45:
                            self.__map[x-2][y+3] = 45
                        else:
                            self.__map[x-2][y+3] = 4
        # up left sight 2 [(-1, -1), (-3, -2), (-2, -3)]
        if not self.__is_out_of_the_board(x-1, y-1):
            if (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0):
                if not self.__is_out_of_the_board(x-3, y-2) and self.__map[x-3][y-2] != 1 and self.__map[x-3][y-2] >= 0:
                    if (self.__map[x-2][y-2] != 1 and self.__map[x-2][y-2] >= 0) and (self.__map[x-2][y-1] != 1 and self.__map[x-2][y-1] >= 0):
                        if self.__map[x-3][y-2] == 2 or self.__map[x-3][y-2] == 42:
                            self.__map[x-3][y-2] = 42
                        elif self.__map[x-3][y-2] == 5 or self.__map[x-3][y-2] == 45:
                            self.__map[x-3][y-2] = 45
                        else:
                            self.__map[x-3][y-2] = 4
                    elif (self.__map[x-2][y-2] != 1 and self.__map[x-2][y-2] >= 0) and (self.__map[x-2][y-1] == 1 or self.__map[x-2][y-1] < 0) or \
                            (self.__map[x-2][y-2] == 1 or self.__map[x-2][y-2] < 0) and (self.__map[x-2][y-1] != 1 and self.__map[x-2][y-1] >= 0):
                        if self.__map[x-3][y-2] == 2 or self.__map[x-3][y-2] == 42:
                            self.__map[x-3][y-2] = 42
                        elif self.__map[x-3][y-2] == 5 or self.__map[x-3][y-2] == 45:
                            self.__map[x-3][y-2] = 45
                        else:
                            self.__map[x-3][y-2] = 4
                if not self.__is_out_of_the_board(x-2, y-3) and self.__map[x-2][y-3] != 1 and self.__map[x-2][y-3] >= 0:
                    if (self.__map[x-2][y-2] != 1 and self.__map[x-2][y-2] >= 0) and (self.__map[x-1][y-2] != 1 and self.__map[x-1][y-2] >= 0):
                        if self.__map[x-2][y-3] == 2 or self.__map[x-2][y-3] == 42:
                            self.__map[x-2][y-3] = 42
                        elif self.__map[x-2][y-3] == 5 or self.__map[x-2][y-3] == 45:
                            self.__map[x-2][y-3] = 45
                        else:
                            self.__map[x-2][y-3] = 4
                    elif (self.__map[x-2][y-2] != 1 and self.__map[x-2][y-2] >= 0) and (self.__map[x-1][y-2] == 1 or self.__map[x-1][y-2] < 0) or \
                            (self.__map[x-2][y-2] == 1 or self.__map[x-2][y-2] < 0) and (self.__map[x-1][y-2] != 1 and self.__map[x-1][y-2] >= 0):
                        if self.__map[x-2][y-3] == 2 or self.__map[x-2][y-3] == 42:
                            self.__map[x-2][y-3] = 42
                        elif self.__map[x-2][y-3] == 5 or self.__map[x-2][y-3] == 45:
                            self.__map[x-2][y-3] = 45
                        else:
                            self.__map[x-2][y-3] = 4
        # down left sight 2 [(1, -1), (3, -2), (2, -3)]
        if not self.__is_out_of_the_board(x+1, y-1):
            if (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0):
                if not self.__is_out_of_the_board(x+3, y-2) and self.__map[x+3][y-2] != 1 and self.__map[x+3][y-2] >= 0:
                    if (self.__map[x+2][y-2] != 1 and self.__map[x+2][y-2] >= 0) and (self.__map[x+2][y-1] != 1 and self.__map[x+2][y-1] >= 0):
                        if self.__map[x+3][y-2] == 2 or self.__map[x+3][y-2] == 42:
                            self.__map[x+3][y-2] = 42
                        elif self.__map[x+3][y-2] == 5 or self.__map[x+3][y-2] == 45:
                            self.__map[x+3][y-2] = 45
                        else:
                            self.__map[x+3][y-2] = 4
                    elif (self.__map[x+2][y-2] != 1 and self.__map[x+2][y-2] >= 0) and (self.__map[x+2][y-1] == 1 or self.__map[x+2][y-1] < 0) or \
                            (self.__map[x+2][y-2] == 1 or self.__map[x+2][y-2] < 0) and (self.__map[x+2][y-1] != 1 and self.__map[x+2][y-1] >= 0):
                        if self.__map[x+3][y-2] == 2 or self.__map[x+3][y-2] == 42:
                            self.__map[x+3][y-2] = 42
                        elif self.__map[x+3][y-2] == 5 or self.__map[x+3][y-2] == 45:
                            self.__map[x+3][y-2] = 45
                        else:
                            self.__map[x+3][y-2] = 4
                if not self.__is_out_of_the_board(x+2, y-3) and self.__map[x+2][y-3] != 1 and self.__map[x+2][y-3] >= 0:
                    if (self.__map[x+2][y-2] != 1 and self.__map[x+2][y-2] >= 0) and (self.__map[x+1][y-2] != 1 and self.__map[x+1][y-2] >= 0):
                        if self.__map[x+2][y-3] == 2 or self.__map[x+2][y-3] == 42:
                            self.__map[x+2][y-3] = 42
                        elif self.__map[x+2][y-3] == 5 or self.__map[x+2][y-3] == 45:
                            self.__map[x+2][y-3] = 45
                        else:
                            self.__map[x+2][y-3] = 4
                    elif (self.__map[x+2][y-2] != 1 and self.__map[x+2][y-2] >= 0) and (self.__map[x+1][y-2] == 1 or self.__map[x+1][y-2] < 0) or \
                            (self.__map[x+2][y-2] == 1 or self.__map[x+2][y-2] < 0) and (self.__map[x+1][y-2] != 1 and self.__map[x+1][y-2] >= 0):
                        if self.__map[x+2][y-3] == 2 or self.__map[x+2][y-3] == 42:
                            self.__map[x+2][y-3] = 42
                        elif self.__map[x+2][y-3] == 5 or self.__map[x+2][y-3] == 45:
                            self.__map[x+2][y-3] = 45
                        else:
                            self.__map[x+2][y-3] = 4
        # down right sight 2 [(1, 1), (3, 2), (2, 3)]
        if not self.__is_out_of_the_board(x+1, y+1):
            if (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0):
                if not self.__is_out_of_the_board(x+3, y+2) and self.__map[x+3][y+2] != 1 and self.__map[x+3][y+2] >= 0:
                    if (self.__map[x+2][y+2] != 1 and self.__map[x+2][y+2] >= 0) and (self.__map[x+2][y+1] != 1 and self.__map[x+2][y+1] >= 0):
                        if self.__map[x+3][y+2] == 2 or self.__map[x+3][y+2] == 42:
                            self.__map[x+3][y+2] = 42
                        elif self.__map[x+3][y+2] == 5 or self.__map[x+3][y+2] == 45:
                            self.__map[x+3][y+2] = 45
                        else:
                            self.__map[x+3][y+2] = 4
                    elif (self.__map[x+2][y+2] != 1 and self.__map[x+2][y+2] >= 0) and (self.__map[x+2][y+1] == 1 or self.__map[x+2][y+1] < 0) or \
                            (self.__map[x+2][y+2] == 1 or self.__map[x+2][y+2] < 0) and (self.__map[x+2][y+1] != 1 and self.__map[x+2][y+1] >= 0):
                        if self.__map[x+3][y+2] == 2 or self.__map[x+3][y+2] == 42:
                            self.__map[x+3][y+2] = 42
                        elif self.__map[x+3][y+2] == 5 or self.__map[x+3][y+2] == 45:
                            self.__map[x+3][y+2] = 45
                        else:
                            self.__map[x+3][y+2] = 4
                if not self.__is_out_of_the_board(x+2, y+3) and self.__map[x+2][y+3] != 1 and self.__map[x+2][y+3] >= 0:
                    if (self.__map[x+2][y+2] != 1 and self.__map[x+2][y+2] >= 0) and (self.__map[x+1][y+2] != 1 and self.__map[x+1][y+2] >= 0):
                        if self.__map[x+2][y+3] == 2 or self.__map[x+2][y+3] == 42:
                            self.__map[x+2][y+3] = 42
                        elif self.__map[x+2][y+3] == 5 or self.__map[x+2][y+3] == 45:
                            self.__map[x+2][y+3] = 45
                        else:
                            self.__map[x+2][y+3] = 4
                    elif (self.__map[x+2][y+2] != 1 and self.__map[x+2][y+2] >= 0) and (self.__map[x+1][y+2] == 1 or self.__map[x+1][y+2] < 0) or \
                            (self.__map[x+2][y+2] == 1 or self.__map[x+2][y+2] < 0) and (self.__map[x+1][y+2] != 1 and self.__map[x+1][y+2] >= 0):
                        if self.__map[x+2][y+3] == 2 or self.__map[x+2][y+3] == 42:
                            self.__map[x+2][y+3] = 42
                        elif self.__map[x+2][y+3] == 5 or self.__map[x+2][y+3] == 45:
                            self.__map[x+2][y+3] = 45
                        else:
                            self.__map[x+2][y+3] = 4

    def sight_process(self):
        for i in range(player.row):
            for j in range(player.column):
                if (self.__map[i][j] == 3):
                    self.__sight_check(i, j)
        file = open(self.__path_to_result_1, 'w')
        for i in range(player.row):
            for j in range(player.column):
                file.write('{} '.format(self.__map[i][j]))
            file.write('\n')
        file.close()
