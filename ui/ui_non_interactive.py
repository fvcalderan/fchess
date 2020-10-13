"""This is a non-interactive UI for fchess.
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

from ui.ui_generic import ui_generic


class human_detected(Exception):
    pass


class ui_non_interactive(ui_generic):

    def ui_start(self):
        print("fchess non-interactive UI v1.0")

    def print_board(self, board):
        """print board in the terminal"""
        pass

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
        raise human_detected

    def board_desc(self, string):
        """get board description and display it"""
        print(f'Board: {string}')

    def display_time_taken(self, turn, time_taken):
        """display time taken for a player to move"""
        if turn == "b":
            display_string = "White_move_time:"
        else:
            display_string = "Black_move_time:"
        print(display_string, time_taken, "s")

    def display_moves(self, moves):
        """display all the moves made in the game"""
        print("Game moves:")
        for i in range(len(moves)):
            if i % 2 == 0:
                print(moves[i], end=" ")
            else:
                print(moves[i])
