import os


class Input:
    def __init__(self, board=1):
        self.__board = board
        self.__result_count = 1
        self.__row, self.__col = 0, 0
        self.__map = []
        self.__obstacle = []
        self.__path_to_map = 'raw_data/board_' + str(board) + '/map.txt'
        self._path_to_result = 'raw_data/board_' + \
            str(board) + '/result/result_'
        with open(self.__path_to_map, 'r') as f:
            self.__row, self.__col = [int(x) for x in next(f).split()]
            for i in range(self.__row):
                line = f.readline()
                self.__map.append([int(x) for x in line.split()])
            for line in f:
                self.__obstacle = [int(x) for x in line.split()]
            f.close()
        self.__windows_size = (10 * 2 + 50 * self.__row,
                               10 * 2 + 50 * self.__col)
        self.__hider = 0
        for i in self.__map:
            for j in i:
                if j == 2:
                    self.__hider += 1

    # GET

    def get_board_id(self):
        return self.__board

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__col

    def get_number_of_obstacle(self):
        return int(len(self.__obstacle) / 4)

    def get_windows_size(self, type):
        if type == 'width':
            return self.__windows_size[0]
        elif type == 'height':
            return self.__windows_size[1]
        elif type == 'both':
            return self.__windows_size

    def get_obstacles(self):
        return self.__obstacle

    def get_hider_count(self):
        return self.__hider

    def map_calibration(self):
        obstacle_index = -1
        obstacle_item = []
        for i in range(int(len(self.__obstacle) / 4)):
            temp = []
            temp.append(self.__obstacle[0 + i * 4])
            temp.append(self.__obstacle[1 + i * 4])
            temp.append(self.__obstacle[2 + i * 4])
            temp.append(self.__obstacle[3 + i * 4])
            obstacle_item.append(temp)
        for item in obstacle_item:
            for i in range(item[1], item[3] + 1):
                for j in range(item[0], item[2] + 1):
                    self.__map[i][j] = obstacle_index
            obstacle_index -= 1
        
        sx, sy, dx, dy = 0, 0, 0, 0
        for i in range(self.__row):
            for j in range(self.__col):
                if self.__map[i][j] == 3:
                    sx, sy = i, j

        # calling isPath method
        for i in range(self.__row):
            for j in range(self.__col):
                if self.__map[i][j] == 0:
                    dx, dy = i, j
                    if not self.isPath(sx, sy, dx, dy):
                        self.__map[i][j] = 1

    def isSafe(self, i, j):
        if (i >= 0 and i < self.__row) and j >= 0 and j < self.__col:
            return True
        return False

    def isPath(self, sx, sy, dx, dy):
        # Defining visited array to keep
        # track of already visited indexes
        visited = [
            [False for x in range(self.__row)]
            for y in range(self.__col)]
        # Flag to indicate whether the
        # path exists or not
        flag = False
        for i in range(self.__row):
            for j in range(self.__col):
                # If matrix[i][j] is source
                # and it is not visited
                if (self.__map[i][j] == 3 and visited[i][j] == False):
                    # Starting from i, j and
                    # then finding the path
                    if (self.checkPath(i, j, visited, dx, dy)):
                        # If path exists
                        flag = True
                        break
        if (flag):
            return True
        return False

    def checkPath(self, i, j, visited, dx, dy):
        # Checking the boundries, walls and
        # whether the cell is unvisited
        if (self.isSafe(i, j) and self.__map[i][j] != 1 and not visited[i][j]):
            # Make the cell visited
            visited[i][j] = True
            # If the cell is the required
            # destination then return true
            if (i == dx and j == dy):
                return True
            # traverse up
            up = self.checkPath(i - 1, j, visited, dx, dy)
            # If path is found in up
            # direction return true
            if (up):
                return True
            # Traverse left
            left = self.checkPath(i, j - 1, visited, dx, dy)
            # If path is found in left
            # direction return true
            if (left):
                return True
            # Traverse down
            down = self.checkPath(i + 1, j, visited, dx, dy)
            # If path is found in down
            # direction return true
            if (down):
                return True
            # Traverse right
            right = self.checkPath(i, j + 1, visited, dx, dy)
            # If path is found in right
            # direction return true
            if (right):
                return True
        # No path has been found
        return False

    def output_to_result(self):
        try:
            os.mkdir('raw_data/board_'+str(self.__board)+'/result')
        except:
            print("Directory exist!")
        self.map_calibration()
        with open(self._path_to_result + str(self.__result_count) + '.txt', 'w') as file:
            self.__result_count += 1
            for i in range(self.__row):
                for j in range(self.__col):
                    file.write("{} ".format(self.__map[i][j]))
                file.write("\n")
            file.close()
