from easygraphics import *
import argparse
from timeit import default_timer as timer
import input_raw_data
from graphics import draw_from_result
import sight_processing
import seeker_action


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-board_id', '--board_id', type=int, help = 'Choose one board to run 1 - 6')
    args = parser.parse_args()
    board = args.board_id

    choose = board
    start = timer()
    board_1 = input_raw_data.Input(choose)
    board_1.output_to_result()
    data = sight_processing.SightProcessing(choose,board_1.get_row(),board_1.get_column())
    data.sight_process()
    end = timer()

    sa = seeker_action.SeekerAction(choose,1,board_1.get_row(), board_1.get_column(),board_1.get_hider_count())
    sa.start()

    t = draw_from_result.DrawFromResult(choose,board_1.get_windows_size('width'),board_1.get_windows_size('height'),board_1.get_column(),board_1.get_row(),board_1.get_obstacles())
    t.draw_board()

    pause()
    print((end - start) * 1000)


easy_run(main)