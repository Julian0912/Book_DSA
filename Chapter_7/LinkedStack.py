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


class LinkedStack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = Node(e, self.head)  # next存储的是下一个结点对象地址（或None）
        self.size += 1

    def top(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        return self.head.element

    def pop(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        return e


if __name__ == '__main__':
    s = LinkedStack()
    s.push('a')
