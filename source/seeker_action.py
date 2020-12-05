import sight_processing
import collections
import player
import hider_action


class SeekerAction():
    def __init__(self, board=1):
        self.__board = board
        self.__map = []
        self.__start_state = player.state
        self.__path_to_result = 'raw_data/board_' + \
            str(self.__board) + '/result/result_' + str(player.state) + '.txt'
        with open(self.__path_to_result, 'r') as f:
            for line in f:
                self.__map.append([int(x) for x in line.split()])
            f.close()

    def __move_up(self, x, y):
        if self.__map[x-1][y] == 42 or self.__map[x-1][y] == 2:
            player.hider -= 1
        self.__map[x-1][y] = 3
        self.__map[x][y] = 4

    def __move_down(self, x, y):
        if self.__map[x+1][y] == 42 or self.__map[x+1][y] == 2:
            player.hider -= 1
        self.__map[x+1][y] = 3
        self.__map[x][y] = 4

    def __move_left(self, x, y):
        if self.__map[x][y-1] == 42 or self.__map[x][y-1] == 2:
            player.hider -= 1
        self.__map[x][y-1] = 3
        self.__map[x][y] = 4

    def __move_right(self, x, y):
        if self.__map[x][y+1] == 42 or self.__map[x][y+1] == 2:
            player.hider -= 1
        self.__map[x][y+1] = 3
        self.__map[x][y] = 4

    def __move_up_right(self, x, y):
        if self.__map[x-1][y+1] == 42 or self.__map[x-1][y+1] == 2:
            player.hider -= 1
        self.__map[x-1][y+1] = 3
        self.__map[x][y] = 4

    def __move_up_left(self, x, y):
        if self.__map[x-1][y-1] == 42 or self.__map[x-1][y-1] == 2:
            player.hider -= 1
        self.__map[x-1][y-1] = 3
        self.__map[x][y] = 4

    def __move_down_left(self, x, y):
        if self.__map[x+1][y-1] == 42 or self.__map[x+1][y-1] == 2:
            player.hider -= 1
        self.__map[x+1][y-1] = 3
        self.__map[x][y] = 4

    def __move_down_right(self, x, y):
        if self.__map[x+1][y+1] == 42 or self.__map[x+1][y+1] == 2:
            player.hider -= 1
        self.__map[x+1][y+1] = 3
        self.__map[x][y] = 4

    def __write_to_result(self, state):
        file = open('raw_data/board_' + str(self.__board) +
                    '/result/result_' + str(state) + '.txt', 'w')
        for i in range(player.row):
            for j in range(player.column):
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
        for i in range(player.row):
            for j in range(player.column):
                if self.__map[i][j] == 4:
                    self.__map[i][j] = 6
                elif self.__map[i][j] == 42:
                    self.__map[i][j] = 2
                elif self.__map[i][j] == 45:
                    self.__map[i][j] = 5
    
    def get_hider_list(self):
        hider_list = []
        for i in range(player.row):
            for j in range(player.column):
                if (self.__map[i][j] == 2 or self.__map[i][j] == 42):
                    hider_list.append((i,j))
        return hider_list

    def __move_decider(self, x, y, target):
        move = []
        path = player.bfs(self.__map, x, y, target, 'seeker')
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

    def __sight_process(self, state_cur):
        sight = sight_processing.SightProcessing(
            self.__board, state_cur)
        sight.sight_process()

    def __move(self, x, y, target, state_cur, mode):
        move = self.__move_decider(x, y, target)
        for i in range(len(move)):
            self.__reset_sight()
            state_cur += 1
            if player.state > self.__start_state and player.state % 5 == 0:
                print("hider turn")
                hider_list = self.get_hider_list()
                for hider in hider_list:
                    hider_announce = hider_action.HiderAction(self.__board, hider[0], hider[1])
                    hider_announce.announce()
                    self.__start_state += 1
                break
            else:
                if move[i] == 1:
                    self.__move_right(x, y)
                    y += 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 2:
                    self.__move_up_right(x, y)
                    x -= 1
                    y += 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 3:
                    self.__move_up(x, y)
                    x -= 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 4:
                    self.__move_up_left(x, y)
                    x -= 1
                    y -= 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 5:
                    self.__move_left(x, y)
                    y -= 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 6:
                    self.__move_down_left(x, y)
                    x += 1
                    y -= 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 7:
                    self.__move_down(x, y)
                    x += 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                elif move[i] == 8:
                    self.__move_down_right(x, y)
                    x += 1
                    y += 1
                    self.__write_to_result(state_cur)
                    self.__sight_process(state_cur)
                self.__read_from_current_state(state_cur)
                if mode == 2:
                    found = False
                    for i in range(player.row):
                        for j in range(player.column):
                            if self.__map[i][j] == 42 or self.__map[target[0]][target[1]] == 4:
                                found = True
                    if found:
                        break
            self.__read_from_current_state(state_cur)
        return state_cur, x, y

    def __get_to_target(self, x, y, target, mode):
        move = self.__move(x, y, target, player.state, mode)
        player.state, x, y = move[0], move[1], move[2]
        return (x, y)

    def __detect_target(self, x, y, targets):
        distance = []
        for target in targets:
            distance.append(abs(x-target[0]) + abs(y-target[1]))
        while len(distance) > 0:
            closest = self.__get_closest(distance)

            new_pos = self.__get_to_target(x, y, targets[closest], 1)
            x = new_pos[0]
            y = new_pos[1]

            distance.remove(distance[closest])
            targets.remove(targets[closest])

    def __lock_target(self, x, y, targets):
        distance = []
        for target in targets:
            distance.append(abs(x-target[0]) + abs(y-target[1]))
        closest = self.__get_closest(distance)
        self.__get_to_target(x, y, targets[closest], 2)

    def __found_something(self):
        targets = []
        found = True
        while found:
            n = 0
            targets.clear()
            row, col = 0, 0
            for i in range(player.row):
                for j in range(player.column):
                    if (self.__map[i][j] == 3):
                        row, col = i, j
                    elif (self.__map[i][j] == 42):
                        targets.append((i, j))
                        n += 1
            if n == 0:
                found = False
            self.__detect_target(row, col, targets)

    def __go_finding(self):
        targets = []
        row, col = 0, 0
        for i in range(player.row):
            for j in range(player.column):
                if self.__map[i][j] == 42:
                    targets.append((i, j))
                elif (self.__map[i][j] == 3):
                    row, col = i, j
        if len(targets) == 0:
            for i in range(player.row):
                for j in range(player.column):
                    if self.__map[i][j] == 5 or self.__map[i][j] == 45:
                        targets.append((i, j))
                    elif (self.__map[i][j] == 3):
                        row, col = i, j
        if len(targets) == 0:
            for i in range(player.row):
                for j in range(player.column):
                    if self.__map[i][j] == 0:
                        targets.append((i, j))
                    elif (self.__map[i][j] == 3):
                        row, col = i, j
        if len(targets) == 0:
            for i in range(player.row):
                for j in range(player.column):
                    if self.__map[i][j] == 2 or self.__map[i][j] == 42:
                        targets.append((i, j))
                    elif (self.__map[i][j] == 3):
                        row, col = i, j
        self.__lock_target(row, col, targets)

    def start(self):
        while player.hider > 0 and (player.state-1 - self.__start_state) < player.step_limit:
            hider_found = 0
            for i in self.__map:
                for j in i:
                    if j == 42:
                        hider_found += 1
            if hider_found > 0:
                self.__found_something()
            else:
                self.__go_finding()
        print("{} steps".format(player.state - 1))
