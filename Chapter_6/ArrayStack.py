# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class EmptyError(Exception):
    pass


class ArrayStack(object):
    def __init__(self, init_e=None):
        self.__stack = []
        self.__n = 0  # 栈的长度
        if init_e is not None:
            init_ls = list(init_e)
            self.__stack.extend(init_ls)
            self.__n += len(init_ls)

    def __len__(self):
        return self.__n

    def __str__(self):
        return 'Stack({})'.format(self.__stack)

    def push(self, e):
        self.__stack.append(e)
        self.__n += 1

    def pop(self):
        if self.__n == 0:
            raise EmptyError('pop from empty stack')
        self.__n -= 1
        return self.__stack.pop()

    def top(self):
        if self.__n == 0:
            raise EmptyError('stack is empty')
        return self.__stack[-1]

    def is_empty(self):
        return self.__n == 0


if __name__ == '__main__':
    s = ArrayStack('hello')
    print(s.is_empty())
