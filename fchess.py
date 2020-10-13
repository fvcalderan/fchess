"""This is fchess' main file.
   Copyright (C) 2020 Felipe V. Calderan <fvcalderan@gmail.com>
 
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
 
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
 
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import chess
import sys
import timeit

import ai.ai00_random as ai00
import ai.ai01_pvals as ai01
import ai.ai02_bvals as ai02
import ai.ai03_pvals_no_ab as ai03
import ui.ui_terminal as ui_term
import ui.ui_non_interactive as ui_non_interactive


def print_params():
    """Print all the parameters for future reference"""
    print("Parameters for this match:")
    for i in sys.argv:
        print(i, end=' ')
    print("\n")


def get_ui_mode():
    ui = 'term'

    if len(sys.argv) != 7:
        print('Usage: python3 fchess.py board ui white wdiff black bdiff')
        print('board: board file in Forsyth-Edwards Notation (FEN)')
        print('ui:    which UI will be used? [term / nint]')
        print('white: who will play as white? [human, ai00, ..., ai03]')
        print('wdiff: white AI difficulty (irrelevant for human and ai00)')
        print('black: who will play as black? [human, ai00, ..., ai03]')
        print('bdiff: black AI difficulty (irrelevant for human and ai00)')
        print('\nExample 1: python3 fchess.py boards/default term human 0 ai02 3')
        print('Example 2: python3 fchess.py boards/default nint ai01 3 ai02 3 > out.txt')
        exit()

    if sys.argv[2] == 'term':
        ui = ui_term.ui_terminal()
    elif sys.argv[2] == 'nint':
        ui = ui_non_interactive.ui_non_interactive()
    else:
        print("Invalid UI option. Please choose one of the options:")
        print("term: For interactive terminal based UI")
        print("nint: For non-interactive terminal based UI (AIs only)")

    return ui


def get_match(ui_con):
    white = ui_con
    black = ui_con

    if sys.argv[3] == 'ai00':
        white = ai00.AI()
        white.set_difficulty(int(sys.argv[4]))
    elif sys.argv[3] == 'ai01':
        white = ai01.AI()
        white.set_difficulty(int(sys.argv[4]))
    elif sys.argv[3] == 'ai02':
        white = ai02.AI()
        white.set_difficulty(int(sys.argv[4]))
    elif sys.argv[3] == 'ai03':
        white = ai03.AI()
        white.set_difficulty(int(sys.argv[4]))
    else:
        white = ui_con

    if sys.argv[5] == 'ai00':
        black = ai00.AI()
        black.set_difficulty(int(sys.argv[6]))
    elif sys.argv[5] == 'ai01':
        black = ai01.AI()
        black.set_difficulty(int(sys.argv[6]))
    elif sys.argv[5] == 'ai02':
        black = ai02.AI()
        black.set_difficulty(int(sys.argv[6]))
    elif sys.argv[5] == 'ai03':
        black = ai03.AI()
        black.set_difficulty(int(sys.argv[6]))
    else:
        black = ui_con

    return white, black


def new_game(ui_con):
    ui_con.ui_start()
    white, black = get_match(ui_con)

    with open(sys.argv[1], "r") as board_file:
        board = board_file.readlines()

    try:
        ui_con.board_desc(board[0])
        board = chess.Board(board[1])
    except FileNotFoundError:
        print('Invalid board file')
        exit()

    return white, black, board


def play_turn(ui_con, board, white, black, turn):
    """get whose turn it is"""
    if turn == 'w':
        move = white.move(board, turn)
        turn = 'b'
    else:
        move = black.move(board, turn)
        turn = 'w'

    board.push(move)
    return board, move, turn


def main():
    print_params()
    ui_con = get_ui_mode()
    white, black, board = new_game(ui_con)
    moves = []
    if board.turn == chess.WHITE:
        turn = 'w'
    else:
        turn = 'b'

    while (not board.is_game_over()):
        ui_con.print_board(board)
        t_start = timeit.default_timer()
        board, move, turn = play_turn(ui_con, board, white, black, turn)
        t_stop = timeit.default_timer()
        moves.append(move)
        ui_con.display_time_taken(turn, t_stop-t_start)

    ui_con.print_board(board)
    ui_con.get_end_game_status(board)
    ui_con.display_moves(moves)


if __name__ == '__main__':
    main()
