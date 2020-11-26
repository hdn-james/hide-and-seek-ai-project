import sight_processing


class SeekerAction:
    def __init__(self, board=1, state=1, row=0, column=0):
        self.__board = board
        self.__state = state
        self.__row = row
        self.__col = column
        self.__map = []
        # 1 = right; 2 = up-right; 3 = up; 4 = up-left; 5 = left; 6 = down-left; 7 = down; 8 = down-right
        self.__action = []
        self.__path_to_result = 'raw_data/board_' + \
            str(self.__board) + '/result/result_' + str(self.__state) + '.txt'
        with open(self.__path_to_result, 'r') as f:
            for line in f:
                self.__map.append([int(x) for x in line.split()])
            f.close()

    def __can_move_up(self, x, y):
        return (x-1 >= 0 and x-1 < self.__col) and (y >= 0 and y < self.__row) and \
            (self.__map[x-1][y] != 1 and self.__map[x-1][y] >= 0)

    def __can_move_down(self, x, y):
        return (x+1 >= 0 and x+1 < self.__col) and (y >= 0 and y < self.__row) and \
            (self.__map[x+1][y] != 1 and self.__map[x+1][y] >= 0)

    def __can_move_left(self, x, y):
        return (x >= 0 and x < self.__col) and (y-1 >= 0 and y-1 < self.__row) and \
            (self.__map[x][y-1] != 1 and self.__map[x][y-1] >= 0)

    def __can_move_right(self, x, y):
        return (x >= 0 and x < self.__col) and (y+1 >= 0 and y+1 < self.__row) and \
            (self.__map[x][y+1] != 1 and self.__map[x][y+1] >= 0)

    def __can_move_up_right(self, x, y):
        return (x-1 >= 0 and x-1 < self.__col) and (y+1 >= 0 and y+1 < self.__row) and \
            (self.__map[x-1][y+1] != 1 and self.__map[x-1][y+1] >= 0)

    def __can_move_up_left(self, x, y):
        return (x-1 >= 0 and x-1 < self.__col) and (y-1 >= 0 and y-1 < self.__row) and \
            (self.__map[x-1][y-1] != 1 and self.__map[x-1][y-1] >= 0)

    def __can_move_down_left(self, x, y):
        return (x+1 >= 0 and x+1 < self.__col) and (y-1 >= 0 and y-1 < self.__row) and \
            (self.__map[x+1][y-1] != 1 and self.__map[x+1][y-1] >= 0)

    def __can_move_down_right(self, x, y):
        return (x+1 >= 0 and x+1 < self.__col) and (y+1 >= 0 and y+1 < self.__row) and \
            (self.__map[x+1][y+1] != 1 and self.__map[x+1][y+1] >= 0)

    def __move_up(self, x, y):
        self.__map[x-1][y] = 3
        self.__map[x][y] = 4

    def __move_down(self, x, y):
        self.__map[x+1][y] = 3
        self.__map[x][y] = 4

    def __move_left(self, x, y):
        self.__map[x][y-1] = 3
        self.__map[x][y] = 4

    def __move_right(self, x, y):
        self.__map[x][y+1] = 3
        self.__map[x][y] = 4

    def __move_up_right(self, x, y):
        self.__map[x-1][y+1] = 3
        self.__map[x][y] = 4

    def __move_up_left(self, x, y):
        self.__map[x-1][y-1] = 3
        self.__map[x][y] = 4

    def __move_down_left(self, x, y):
        self.__map[x+1][y-1] = 3
        self.__map[x][y] = 4

    def __move_down_right(self, x, y):
        self.__map[x+1][y+1] = 3
        self.__map[x][y] = 4

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

    def __get_closest(self, distance):
        min = 9999
        index_min = 0
        for i in range(len(distance)):
            if distance[i] < min:
                min = distance[i]
                index_min = i
        return index_min

    def __reset_sight(self):
        for i in range(self.__row):
            for j in range(self.__col):
                if self.__map[i][j] == 4:
                    self.__map[i][j] = 0
                elif self.__map[i][j] == 42:
                    self.__map[i][j] = 2
                elif self.__map[i][j] == 45:
                    self.__map[i][j] = 5

    def __get_to_target(self, x, y, target):
        state_cur = self.__state
        while (target[0] - x) != 0 or (target[1] - y) != 0:
            self.__reset_sight()
            if ((target[0] - x) == 0 and (target[1]-y) > 0):
                state_cur += 1
                if self.__can_move_right(x, y):
                    self.__move_right(x, y)
                    y += 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) < 1 and (target[1] - y) > 0:
                state_cur += 1
                if self.__can_move_up_right(x, y):
                    self.__move_up_right(x, y)
                    x -= 1
                    y += 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) < 0 and (target[1] - y) == 0:
                state_cur += 1
                if self.__can_move_up(x, y):
                    self.__move_up(x, y)
                    x -= 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) < 0 and (target[1] - y) < 0:
                state_cur += 1
                if self.__can_move_up_left(x, y):
                    self.__move_up_left(x, y)
                    x -= 1
                    y -= 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) == 0 and (target[1] - y) < 0:
                state_cur += 1
                if self.__can_move_left(x, y):
                    self.__move_left(x, y)
                    y -= 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) > 0 and (target[1] - y) < 0:
                state_cur += 1
                if self.__can_move_down_left(x, y):
                    self.__move_down_left(x, y)
                    x += 1
                    y -= 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    
                    sight.sight_process()
            elif (target[0] - x) > 0 and (target[1] - y) == 0:
                state_cur += 1
                if self.__can_move_down(x, y):
                    self.__move_down(x, y)
                    x += 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
            elif (target[0] - x) > 0 and (target[1] - y) > 0:
                state_cur += 1
                if self.__can_move_down_right(x, y):
                    self.__move_down_right(x, y)
                    x += 1
                    y += 1
                    self.__write_to_result(state_cur)
                    sight = sight_processing.SightProcessing(
                        self.__board, self.__row, self.__col, state_cur)
                    sight.sight_process()
        self.__state = state_cur
        return (x, y)

    def __detect_target(self, x, y, targets):
        distance = []
        for target in targets:
            distance.append(abs(x-target[0]) + abs(y-target[1]))
        while len(distance) > 0:
            closest = self.__get_closest(distance)
            new_pos = self.__get_to_target(x, y, targets[closest])
            x = new_pos[0]
            y = new_pos[1]
            distance.remove(distance[closest])
            targets.remove(targets[closest])

    def get_something(self):
        targets = []
        found = True
        while found:
            n = 0
            targets.clear()
            row, col = 0, 0
            for i in range(self.__row):
                for j in range(self.__col):
                    if (self.__map[i][j] == 3):
                        row, col = i, j
                    elif (self.__map[i][j] == 42):
                        targets.append((i, j))
                        n += 1
            if n == 0:
                found = False
            self.__detect_target(row, col, targets)
            self.__read_from_current_state(self.__state)
