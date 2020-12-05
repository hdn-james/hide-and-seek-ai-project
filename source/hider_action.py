import sight_processing
import collections
import random
import player


class HiderAction:
    def __init__(self, board=1, hx=0, hy=0):
        self.__board = board
        self.__map = []
        self.__hx = hx
        self.__hy = hy
        self.__path_to_result = 'raw_data/board_' + \
            str(self.__board) + '/result/result_' + str(player.state) + '.txt'
        with open(self.__path_to_result, 'r') as f:
            for line in f:
                self.__map.append([int(x) for x in line.split()])
            f.close()

    def __move_up(self):
        if self.__map[self.__hx-1][self.__hy] == 42 or self.__map[self.__hx-1][self.__hy] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx-1][self.__hy] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_down(self):
        if self.__map[self.__hx+1][self.__hy] == 42 or self.__map[self.__hx+1][self.__hy] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx+1][self.__hy] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_left(self):
        if self.__map[self.__hx][self.__hy-1] == 42 or self.__map[self.__hx][self.__hy-1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx][self.__hy-1] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_right(self):
        if self.__map[self.__hx][self.__hy+1] == 42 or self.__map[self.__hx][self.__hy+1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx][self.__hy+1] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_up_right(self):
        if self.__map[self.__hx-1][self.__hy+1] == 42 or self.__map[self.__hx-1][self.__hy+1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx-1][self.__hy+1] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_up_left(self):
        if self.__map[self.__hx-1][self.__hy-1] == 42 or self.__map[self.__hx-1][self.__hy-1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx-1][self.__hy-1] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_down_left(self):
        if self.__map[self.__hx+1][self.__hy-1] == 42 or self.__map[self.__hx+1][self.__hy-1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx+1][self.__hy-1] = 2
        self.__map[self.__hx][self.__hy] = 0

    def __move_down_right(self):
        if self.__map[self.__hx+1][self.__hy+1] == 42 or self.__map[self.__hx+1][self.__hy+1] == 2:
            player.hider -= 1
            print("hider count: {}".format(player.hider))
        self.__map[self.__hx+1][self.__hy+1] = 2
        self.__map[self.__hx][self.__hy] = 0

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

    def __move_decider(self, target):
        move = []
        path = player.bfs(self.__map, self.__hx, self.__hy, target, 'hider')
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
        print(move)
        return move

    def __move(self, target, state_cur):
        move = self.__move_decider(target)
        for i in range(len(move)):
            state_cur += 1
            if move[i] == 1:
                self.__move_right()
                self.__hy += 1
                self.__write_to_result(state_cur)
            elif move[i] == 2:
                self.__move_up_right()
                self.__hx -= 1
                self.__hy += 1
                self.__write_to_result(state_cur)
            elif move[i] == 3:
                self.__move_up()
                self.__hx -= 1
                self.__write_to_result(state_cur)
            elif move[i] == 4:
                self.__move_up_left()
                self.__hx -= 1
                self.__hy -= 1
                self.__write_to_result(state_cur)
            elif move[i] == 5:
                self.__move_left()
                self.__hy -= 1
                self.__write_to_result(state_cur)
            elif move[i] == 6:
                self.__move_down_left()
                self.__hx += 1
                self.__hy -= 1
                self.__write_to_result(state_cur)
            elif move[i] == 7:
                self.__move_down()
                self.__hx += 1
                self.__write_to_result(state_cur)
            elif move[i] == 8:
                self.__move_down_right()
                self.__hx += 1
                self.__hy += 1
                self.__write_to_result(state_cur)
        return state_cur

    def __get_to_target(self, target):
        player.state = self.__move(target, player.state)

    def announce(self):
        announced = False
        while not announced:
            pos = random.randint(0, 47)
            a_x = self.__hx + player.row_around[pos]
            a_y = self.__hy + player.col_around[pos]
            if player.is_safe_hider_announce(self.__map, a_x, a_y):
                player.state += 1
                self.__map[a_x][a_y] = 5
                self.__write_to_result(player.state)
                announced = True

    def __get_furthest(self, distance):
        max = 0
        index_max = 0
        for i in range(len(distance)):
            if distance[i] > max:
                max = distance[i]
                index_max = i
        return index_max

    def __find_furthest(self):
        targets = []
        row, col = 0, 0
        for i in range(player.row):
            for j in range(player.column):
                if self.__map[i][j] == 0:
                    targets.append((i, j))
                elif (self.__map[i][j] == 3):
                    row, col = i, j
        distance = []
        for target in targets:
            distance.append(abs(row-target[0]) + abs(col-target[1]))
        furthest = self.__get_furthest(distance)
        return targets[furthest]

    def go_hiding(self):
        target = self.__find_furthest()
        self.__get_to_target(target)
        print(self.__hx, self.__hy)
