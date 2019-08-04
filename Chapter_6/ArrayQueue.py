# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class EmptyError(Exception):
    pass


class ArrayQueue(object):
    """适当扩增和缩减底层数组（列表）的情况，见书"""
    def __init__(self, n=10):
        self.__queue = [None] * n  # 不考虑队列满的情况
        self.__n = n  # 列表长度
        self.__size = 0  # 队列中的元素数量
        self.__front = 0

    def __len__(self):
        return self.__size

    def __str__(self):
        return 'Queue({})'.format(self.__queue)

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, e):
        k = (self.__front + self.__size) % self.__n
        self.__queue[k] = e
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        e = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front = (self.__front + 1) % self.__n
        self.__size -= 1
        return e

    def first(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        return self.__queue[self.__front]


if __name__ == '__main__':
    q = ArrayQueue()
    print(q)
    q.enqueue('a')
    print(q)

