from easygraphics import *
import argparse
import os
from timeit import default_timer as timer
import input_raw_data
from graphics import draw_from_result
import sight_processing
import seeker_action


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-board_id', '--board_id', type=int,
                        help='Choose one board to run 1 - 6')
    args = parser.parse_args()
    board = args.board_id

    path = 'raw_data/'

    listdirs = os.listdir(path)
    number_dirs = len(listdirs)

    if board in range(1, number_dirs):
        choose = board
        start = timer()
        board_1 = input_raw_data.Input(choose)
        board_1.output_to_result()

        data = sight_processing.SightProcessing(
            choose,
            board_1.get_row(),
            board_1.get_column())
        data.sight_process()

        sa = seeker_action.SeekerAction(
            choose,
            board_1.get_row(),
            board_1.get_column(),
            board_1.get_hider_count()
        )
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
    else:
        print("Wrong input")
        init_graph(400, 300)
        draw_rect(50, 50, 350, 250)  # draw a border to better see the result
        draw_rect_text(
            50, 50, 300, 200, "Invalid board ID",
            flags=TextFlags.TEXT_WORD_WRAP | TextFlags.ALIGN_CENTER)
    pause()
    close_graph()


easy_run(main)
