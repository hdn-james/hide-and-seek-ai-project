from easygraphics import *
import argparse
import os
from timeit import default_timer as timer
import input_raw_data
from graphics import draw_from_result
import sight_processing
import seeker_action
import hider_action
import player


def Error(message):
    init_graph(400, 300)
    draw_rect(50, 50, 350, 250)
    draw_rect_text(
        50, 50, 300, 200, message,
        flags=TextFlags.TEXT_WORD_WRAP | TextFlags.ALIGN_CENTER)
    pause()
    close_graph()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-board_id', '--board_id', type=int,
                        help='Choose a board to run')
    parser.add_argument('-level', '--level', type=int,
                        help='Select a level')
    try:
        args = parser.parse_args()
        board = args.board_id
        player.level = args.level

        path = 'raw_data/'
        listdirs = os.listdir(path)
        number_dirs = len(listdirs)

        if board in range(1, number_dirs):
            choose = board
            start = timer()
            board_1 = input_raw_data.Input(choose)
            board_1.output_to_result()

            data = sight_processing.SightProcessing(choose)
            data.sight_process()

            if player.level == 3:
                hider_list = board_1.get_hider_list()
                for hider in hider_list:
                    hider_begin = hider_action.HiderAction(
                        choose, hider[0], hider[1])
                    hider_begin.go_hiding()

            sa = seeker_action.SeekerAction(choose)
            sa.start()
            end = timer()

            t = draw_from_result.DrawFromResult(
                choose,
                board_1.get_windows_size('width'),
                board_1.get_windows_size('height'),
                board_1.get_column(),
                board_1.get_row(),
                board_1.get_obstacles()
            )
            t.draw_board()
            print('%.4f ms' % ((end-start)*1000))
            pause()
            close_graph()
        else:
            print("Invalid board ID")
            Error("Invalid board ID")
        os.system("python3 clean_result.py")
    except:
        print("Invalid argument")
        Error("Invalid argument")


easy_run(main)
