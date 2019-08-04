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


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        return self.head.element

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('queue is empty')
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return e
