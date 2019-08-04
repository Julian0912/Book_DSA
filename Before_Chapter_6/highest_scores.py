# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 
#


class GameEntry(object):
    """这是一个游戏实例，表示一个玩家对象，此处简化至(name, score)"""
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def __str__(self):
        return '({0}, {1})'.format(self.__name,self.__score)


class ScoreBoard(object):
    def __init__(self, capacity=10):
        self.__board = [None]*capacity
        self.__n = 0

    def __getitem__(self, item):
        return self.__board[item]

    def __str__(self):
        return '\n'.join(str(self.__board[j] for j in range(self.__n)))

    def add(self, entry:GameEntry):
        score = entry.get_score()
        good = self.__n < len(self.__board) or score > self.__board[-1].get_score()
        if good:
            if self.__n < len(self.__board):
                self.__n += 1
            j = self.__n - 1
            while j > 0 and self.__board[j-1].get_score() < score:
                self.__board[j] = self.__board[j-1]
                j -= 1
            self.__board[j] = entry




