# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class EmptyError(Exception):
    pass


class Node(object):
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next


class CircularQueue(object):
    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        return self.tail.next.element  # 尾结点的下一个即头结点

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            newest.next = newest
        else:
            newest.next = self.tail.next
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        head = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        return head.element

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next
