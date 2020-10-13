"""This is interactive terminal-based UI for fchess.
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
from ui.ui_generic import ui_generic


class illegal_move(Exception):
    pass


class ui_terminal(ui_generic):

    def get_possible_moves_str(self, board):
        """return string with possible moves"""
        possible_moves = ''
        for i, v in enumerate(board.legal_moves):
            possible_moves += str(v)+' '
            if (i+1) % 8 == 0:
                possible_moves += '\n'
        return possible_moves

    def ui_start(self):
        print("fchess terminal UI v1.0")

    def print_board(self, board):
        """print board in the terminal"""
        board = str(board)

        # replace white pieces
        board = board.replace('K', '\u2654')
        board = board.replace('Q', '\u2655')
        board = board.replace('R', '\u2656')
        board = board.replace('B', '\u2657')
        board = board.replace('N', '\u2658')
        board = board.replace('P', '\u2659')

        # replace black pieces
        board = board.replace('k', '\u265a')
        board = board.replace('q', '\u265b')
        board = board.replace('r', '\u265c')
        board = board.replace('b', '\u265d')
        board = board.replace('n', '\u265e')
        board = board.replace('p', '\u265f')

        # add letters and numbers references
        board = '{0} 8{1} 7{2} 6{3} 5{4} 4{5} 3{6} 2{7} 1\na b c d e f g h'.format(
            board[0:15], board[15:31], board[31:47], board[47:63],
            board[63:79], board[79:95], board[95:111], board[111:127])

        print(board)

    def get_end_game_status(self, board):
        """return possible end game status"""
        if board.is_stalemate():
            print(f'Stalemate! {board.result()}')
        elif board.is_insufficient_material():
            print(f'Insufficient material! {board.result()}')
        elif board.is_checkmate():
            print(f'Checkmate! {board.result()}')
        elif board.is_fivefold_repetition():
            print(f'Fivefold repetition! {board.result()}')
        elif board.is_seventyfive_moves():
            print(f'Seventy five moves! {board.result()}')
        else:
            print(f'Game ended! {board.result()}')

    def move(self, board, player):
        """deals with human input"""
        while (True):
            print('\nYour move:')
            move_str = input('>> ')
            try:
                move = chess.Move.from_uci(move_str)
                if move not in board.legal_moves:
                    raise illegal_move
                return move
            except illegal_move:
                print('Illegal move. List of possible moves:')
                print(self.get_possible_moves_str(board))
                continue

    def board_desc(self, string):
        """get board description and display it"""
        print(f'Board: {string}')

    def display_time_taken(self, turn, time_taken):
        """display time taken for a player to move"""
        pass

    def display_moves(self, moves):
        """display all the moves made in the game"""
        print("Game moves:")
        for i in range(len(moves)):
            if i % 2 == 0:
                print(moves[i], end=" ")
            else:
                print(moves[i])
