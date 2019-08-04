# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class TicTacToe(object):
    def __init__(self):
        self.__board = [[' '] * 3 for j in range(3)]
        self.__player = 'X'

    def __str__(self):
        rows = ['|'.join(self.__board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

    def __is_win(self, mark):
        board = self.__board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        for mark in 'XO':
            if self.__is_win(mark):
                return mark
        return None

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('invalid board position')
        if self.__board[i][j] != ' ':
            raise ValueError('board position occupied')
        if self.winner() is not None:
            raise ValueError('game is already complete')
        self.__board[i][j] = self.__player
        if self.__player == 'X':
            self.__player = 'O'
        else:
            self.__player = 'X'
