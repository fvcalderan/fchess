"""This is a generic file to implement a UI for fchess.
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

class ui_generic:
    """generic ui class for reference"""

    def ui_start(self):
        """start necessary components for the UI"""
        raise NotImplementedError

    def print_board(self, board):
        """print current board state"""
        raise NotImplementedError

    def get_end_game_status(self, board):
        """check for: checkmate, stalemate, insufficient material,
        fivefold repetition, seventy five moves and other"""
        raise NotImplementedError

    def move(self, board, player):
        """deals with human input.
        return chess.Move.from_uci(move_str)"""
        raise NotImplementedError

    def board_desc(self, string):
        """receive loaded board description"""
        raise NotImplementedError

    def display_time_taken(self, turn, time_taken):
        """display time taken for a player to move"""
        raise NotImplementedError

    def display_moves(self, moves):
        """display all the moves made in the game"""
        raise NotImplementedError
