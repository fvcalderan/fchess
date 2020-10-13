"""This a random-playing chess program.
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

import random
from ai.ai_generic import ai_generic


class AI(ai_generic):

    def set_difficulty(self, diff):
        """does nothing for this AI"""
        pass

    def move(self, board, player):
        """deals with ai input"""
        movelist = [i for i in board.legal_moves]
        move = movelist[random.randint(0, len(movelist)-1)]
        return move
