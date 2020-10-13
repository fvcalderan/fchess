"""This is a simple AI that uses Piece-Square Table as a heuristic to play.
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

    # evaluation depending on the square
    piece_square = {'P':
                    (0,  0,  0,  0,  0,  0,  0,  0,
                     50, 50, 50, 50, 50, 50, 50, 50,
                     10, 10, 20, 30, 30, 20, 10, 10,
                     5,  5, 10, 25, 25, 10,  5,  5,
                     0,  0,  0, 20, 20,  0,  0,  0,
                     5, -5, -10,  0,  0, -10, -5,  5,
                     5, 10, 10, -20, -20, 10, 10,  5,
                     0,  0,  0,  0,  0,  0,  0,  0),
                    'p':
                    (0,  0,  0,  0,  0,  0,  0,  0,
                     -5, -10, -10, 20, 20, -10, -10, -5,
                        -5,  5, 10,  0,  0, 10,  5, -5,
                     0,  0,  0, -20, -20,  0,  0,  0,
                     -5, -5, -10, -25, -25, -10, -5, -5,
                     -10, -10, -20, -30, -30, -20, -10, -10,
                     -50, -50, -50, -50, -50, -50, -50, -50,
                        0,  0,  0,  0,  0,  0,  0,  0),
                    'N':
                    (-50, -40, -30, -30, -30, -30, -40, -50,
                        -40, -20,  0,  0,  0,  0, -20, -40,
                        -30,  0, 10, 15, 15, 10,  0, -30,
                        -30,  5, 15, 20, 20, 15,  5, -30,
                        -30,  0, 15, 20, 20, 15,  0, -30,
                        -30,  5, 10, 15, 15, 10,  5, -30,
                        -40, -20,  0,  5,  5,  0, -20, -40,
                     -50, -40, -30, -30, -30, -30, -40, -50),
                    'n':
                    (50, 40, 30, 30, 30, 30, 40, 50,
                        40, 20,  0, -5, -5,  0, 20, 40,
                        30, -5, -10, -15, -15, -10, -5, 30,
                        30, 0, -15, -20, -20, -15, 0, 30,
                        30, -5, -15, -20, -20, -15, -5, 30,
                        30, 0, -10, -15, -15, -10, 0, 30,
                        40, 20,  0,  0,  0,  0, 20, 40,
                        50, 40, 30, 30, 30, 30, 40, 50),
                    'B':
                    (-20, -10, -10, -10, -10, -10, -10, -20,
                        -10,  0,  0,  0,  0,  0,  0, -10,
                        -10,  0,  5, 10, 10,  5,  0, -10,
                        -10,  5,  5, 10, 10,  5,  5, -10,
                        -10,  0, 10, 10, 10, 10,  0, -10,
                        -10, 10, 10, 10, 10, 10, 10, -10,
                        -10,  5,  0,  0,  0,  0,  5, -10,
                        -20, -10, -10, -10, -10, -10, -10, -20),
                    'b':
                    (20, 10, 10, 10, 10, 10, 10, 20,
                        10, -5,  0,  0,  0,  0, -5, 10,
                        10, -10, -10, -10, -10, -10, -10, 10,
                        10,  0, -10, -10, -10, -10,  0, 10,
                        10, -5, -5, -10, -10, -5, -5, 10,
                        10,  0, -5, -10, -10, -5,  0, 10,
                        10,  0,  0,  0,  0,  0,  0, 10,
                        20, 10, 10, 10, 10, 10, 10, 20),
                    'R':
                    (0,  0,  0,  0,  0,  0,  0,  0,
                        5, 10, 10, 10, 10, 10, 10,  5,
                        -5,  0,  0,  0,  0,  0,  0, -5,
                        -5,  0,  0,  0,  0,  0,  0, -5,
                        -5,  0,  0,  0,  0,  0,  0, -5,
                        -5,  0,  0,  0,  0,  0,  0, -5,
                        -5,  0,  0,  0,  0,  0,  0, -5,
                        0,  0,  0,  5,  5,  0,  0,  0),
                    'r':
                    (0,  0,  0, -5, -5,  0,  0,  0,
                        5,  0,  0,  0,  0,  0,  0,  5,
                        5,  0,  0,  0,  0,  0,  0,  5,
                        5,  0,  0,  0,  0,  0,  0,  5,
                        5,  0,  0,  0,  0,  0,  0,  5,
                        5,  0,  0,  0,  0,  0,  0,  5,
                        -5, -10, -10, -10, -10, -10, -10, -5,
                        0,  0,  0,  0,  0,  0,  0,  0),
                    'Q':
                    (-20, -10, -10, -5, -5, -10, -10, -20,
                        -10,  0,  0,  0,  0,  0,  0, -10,
                        -10,  0,  5,  5,  5,  5,  0, -10,
                        -5,  0,  5,  5,  5,  5,  0, -5,
                        0,  0,  5,  5,  5,  5,  0, -5,
                        -10,  5,  5,  5,  5,  5,  0, -10,
                        -10,  0,  5,  0,  0,  0,  0, -10,
                        -20, -10, -10, -5, -5, -10, -10, -20),
                    'q':
                    (20, 10, 10,  5,  5, 10, 10, 20,
                        10,  0, -5,  0,  0,  0,  0, 10,
                        10, -5, -5, -5, -5, -5,  0, 10,
                        0,  0, -5, -5, -5, -5,  0,  5,
                        5,  0, -5, -5, -5, -5,  0,  5,
                        10,  0, -5, -5, -5, -5,  0, 10,
                        10,  0,  0,  0,  0,  0,  0, 10,
                        20, 10, 10,  5,  5, 10, 10, 20),
                    'K':
                    (-30, -40, -40, -50, -50, -40, -40, -30,
                        -30, -40, -40, -50, -50, -40, -40, -30,
                        -30, -40, -40, -50, -50, -40, -40, -30,
                        -30, -40, -40, -50, -50, -40, -40, -30,
                        -20, -30, -30, -40, -40, -30, -30, -20,
                        -10, -20, -20, -20, -20, -20, -20, -10,
                        20, 20,  0,  0,  0,  0, 20, 20,
                        20, 30, 10,  0,  0, 10, 30, 20),
                    'k':
                    (-20, -30, -10,  0,  0, -10, -30, -20,
                        -20, -20,  0,  0,  0,  0, -20, -20,
                        10, 20, 20, 20, 20, 20, 20, 10,
                        20, 30, 30, 40, 40, 30, 30, 20,
                        30, 40, 40, 50, 50, 40, 40, 30,
                        30, 40, 40, 50, 50, 40, 40, 30,
                        30, 40, 40, 50, 50, 40, 40, 30,
                        30, 40, 40, 50, 50, 40, 40, 3)
                    }

    G_DEPTH = 4

    def set_difficulty(self, diff):
        """set depth level for minimax"""
        self.G_DEPTH = diff

    def static_board_eval(self, board):
        """Return board evaluation"""
        piece_score = {'.': 0, 'P': 100, 'N': 320, 'B': 330,
                       'R': 500, 'Q': 900, 'K': 200000,
                       '.': 0, 'p': -100, 'n': -320, 'b': -330,
                       'r': -500, 'q': -900, 'k': -200000}
        board = str(board)
        board = board.replace(' ', '')
        board = board.replace('\n', '')

        board_score = 0
        for i, v in enumerate(board):
            board_score += piece_score[v]
            board_score += self.place_score(i, v)

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

    def place_score(self, i, v):
        if v == '.':
            return 0
        else:
            return self.piece_square[v][i]
