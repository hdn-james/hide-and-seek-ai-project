from easygraphics import *
import os
import fnmatch

cell_size = 30


class DrawFromResult:
    def __init__(self, board=1, width=0, height=0, column=0, row=0, obstacles=[]):
        self.__board = board
        self.__width = width
        self.__height = height
        self.__row = row
        self.__col = column
        self.__obstacle = obstacles
        self.__maps = []
        self.__path_to_result_directory = 'raw_data/board_' + \
            str(board) + '/result'
        self.__result_files_count = 0
        for file in os.listdir(self.__path_to_result_directory):
            if fnmatch.fnmatch(file, 'result_*.txt'):
                self.__result_files_count += 1
        for i in range(1, self.__result_files_count + 1):
            temp = []
            with open(self.__path_to_result_directory + '/result_' + str(i) + '.txt', 'r') as file:
                for line in file:
                    temp.append([int(x) for x in line.split()])
                file.close()
            self.__maps.append(temp)
        init_graph(self.__height, self.__width)

    def __del__(self):
        close_graph()

    def __draw_background(self):
        background = create_image(self.__height, self.__width)
        set_background_color(Color.WHITE)
        return background

    def __draw_base_lines(self):
        for i in range(self.__col + 1):
            # vertical lines
            set_color(Color.LIGHT_BLUE)
            draw_line(
                10 + cell_size * i,
                10,
                10 + cell_size * i,
                10 + cell_size * self.__row)
        for i in range(self.__row + 1):
            # horizontal lines
            set_color(Color.LIGHT_BLUE)
            draw_line(10,
                      10 + cell_size * i,
                      10 + cell_size * self.__col,
                      10 + cell_size * i)

    def __draw_wall(self, map):
        set_fill_color(Color.DARK_GRAY)
        set_color(Color.DARK_GRAY)
        for i in range(self.__row):
            for j in range(self.__col):
                if map[i][j] == 1:
                    draw_rect(10 + cell_size * j,
                              10 + cell_size * i,
                              10 + cell_size * (j + 1),
                              10 + cell_size * (i + 1))

    def __draw_obstacles(self, map):
        set_color(Color.DARK_BLUE)
        set_fill_color(Color.LIGHT_YELLOW)
        for i in range(int(len(self.__obstacle) / 4)):
            draw_rect(10 + cell_size * self.__obstacle[0 + i * 4],
                      10 + cell_size * self.__obstacle[1 + i * 4],
                      10 + cell_size * (self.__obstacle[2 + i * 4] + 1),
                      10 + cell_size * (self.__obstacle[3 + i * 4] + 1))

    def __draw_hider(self, map):
        img = load_image('graphics/hider.png')
        img1 = load_image('graphics/hider_founded.png')
        for i in range(self.__row):
            for j in range(self.__col):
                if (map[i][j] == 2):
                    draw_image(
                        10 + (cell_size * j + (int(cell_size - img.get_width()) / 2)),
                        10 + (cell_size * i + (int(cell_size - img.get_width()) / 2)),
                        img, img.get_width(), img.get_height())
                elif map[i][j] == 42:
                    set_color(Color.DARK_BLUE)
                    rect(10 + cell_size * j, 10 + cell_size * i, 10 +
                         cell_size * (j + 1), 10 + cell_size * (i+1))
                    draw_image(
                        10 + cell_size * j + (int(cell_size - img1.get_width()) / 2),
                        10 + cell_size * i + (int(cell_size - img1.get_width()) / 2),
                        img1, img1.get_width(), img1.get_height())
        img.close()
        img1.close()

    def __draw_seeker(self, map):
        img = load_image('graphics/seeker.png')
        for i in range(self.__row):
            for j in range(self.__col):
                if (map[i][j] == 3):
                    draw_image(
                        10 + cell_size * j + ((cell_size - img.get_width()) / 2),
                        10 + cell_size * i +
                        ((cell_size - img.get_width()) / 2),
                        img, img.get_width(), img.get_width())
        img.close()

    def __draw_seeker_sight(self, map):
        set_fill_color('#fdbec8')
        set_color(Color.DARK_BLUE)
        for i in range(self.__row):
            for j in range(self.__col):
                if (map[i][j] == 4):
                    draw_rect(10 + cell_size * j,
                              10 + cell_size * i,
                              10 + cell_size * (j + 1),
                              10 + cell_size * (i + 1))
    
    def __draw_seen(self, map):
        set_fill_color(Color.LIGHT_CYAN)
        for i in range(self.__row):
            for j in range(self.__col):
                if (map[i][j] == 6):
                    draw_rect(10 + cell_size * j,
                              10 + cell_size * i,
                              10 + cell_size * (j + 1),
                              10 + cell_size * (i + 1))
    
    def __draw_announce(self, map):
        set_fill_color(Color.DARK_RED)
        for i in range(self.__row):
            for j in range(self.__col):
                if (map[i][j] == 45 or map[i][j] == 5):
                    draw_rect(10 + cell_size * j,
                              10 + cell_size * i,
                              10 + cell_size * (j + 1),
                              10 + cell_size * (i + 1))

    def draw_board(self):
        for map in self.__maps:
            pause()
            set_background_color(Color.WHITE)
            clear_device()
            self.__draw_base_lines()
            self.__draw_wall(map)
            self.__draw_obstacles(map)
            self.__draw_seeker(map)
            self.__draw_seeker_sight(map)
            self.__draw_announce(map)
            self.__draw_hider(map)
            self.__draw_seen(map)
            pause()
