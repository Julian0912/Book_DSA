# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class MyVector(object):
    def __init__(self, d):
        self.__coords = [0] * d

    def __len__(self):
        return len(self.__coords)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = MyVector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        return self.__coords == other.__coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self.__coords)[1:-1] + '>'
