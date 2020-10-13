"""This is a simple AI that uses Point Value as a heuristic to play.
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
import sys
from ai.ai_generic import ai_generic


class AI(ai_generic):

    G_DEPTH = 4

    def set_difficulty(self, diff):
        """set depth level for minimax"""
        self.G_DEPTH = diff

    def static_board_eval(self, board):
        """Return board evaluation"""
        piece_score = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 1000,
                       'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -1000}
        board = str(board)
        board = board.replace(' ', '')
        board = board.replace('.', '')
        board = board.replace('\n', '')

        board_score = 0
        for i in board:
            board_score += piece_score[i]

        return board_score

    def minimax(self, board, depth, alpha, beta, player, argmove):
        """minimax with alpha-beta pruning"""

        if depth == 0 or board.is_game_over():
            if board.result() == '1-0':
                return 10000-(self.G_DEPTH-depth), argmove
            elif board.result() == '0-1':
                return -10000+(self.G_DEPTH-depth), argmove
            elif player == 'w' and board.result() == '1/2-1/2':
                return -10000, argmove
            elif player == 'b' and board.result() == '1/2-1/2':
                return 10000, argmove
            else:
                return self.static_board_eval(board), argmove

        movelist = [i for i in board.legal_moves]
        random.shuffle(movelist)

        if player == 'w':
            best_eval = -sys.maxsize
            for move in movelist:
                board.push(move)
                p_eval, _ = self.minimax(
                    board, depth-1, alpha, beta, 'b', move)
                board.pop()
                if p_eval > best_eval:
                    best_eval = p_eval
                    best_move = move
                alpha = max(alpha, p_eval)
                if alpha >= beta:
                    break
            return best_eval, best_move

        else:
            best_eval = sys.maxsize
            for move in movelist:
                board.push(move)
                p_eval, _ = self.minimax(
                    board, depth-1, alpha, beta, 'w', move)
                board.pop()
                if p_eval < best_eval:
                    best_eval = p_eval
                    best_move = move
                beta = min(beta, p_eval)
                if beta <= alpha:
                    break
            return best_eval, best_move

    def move(self, board, player):
        """deals with ai input"""
        final_eval, final_move = self.minimax(board, self.G_DEPTH,
                                              -sys.maxsize, sys.maxsize,
                                              player, None)
        return final_move
