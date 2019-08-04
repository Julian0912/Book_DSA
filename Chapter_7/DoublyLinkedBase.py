# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class EmptyError(Exception):
    pass


class _Node(object):
    __slots__ = 'element', 'prev', 'next'

    def __init__(self, element, prev, next):
        self.element = element
        self.prev = prev
        self.next = next


class _DoublyLinkedBase(object):
    """双向链表"""

    def __init__(self):
        self._header = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert(self, e, predecessor: _Node, successor: _Node):
        """我怎么有结点对象？？
        但有利于子类双端队列的插入操作"""
        newest = _Node(e, predecessor, successor)  # 该结点在创建的时候就已经指定前驱和后继结点了
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete(self, node: _Node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None  # 删除该无用结点与其他结点的不必要链接
        return element


class LinkedDeque(_DoublyLinkedBase):
    """双端队列，不需要初始化"""

    def first(self):
        if self.is_empty():
            raise EmptyError('deque is empty')
        return self._header.next.element

    def last(self):
        if self.is_empty():
            raise EmptyError('deque is empty')
        return self._trailer.prev.element

    def insert_first(self, e):
        self._insert(e, self._header, self._header.next)

    def insert_last(self, e):
        self._insert(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise EmptyError('deque is empty')
        return self._delete(self._header.next)

    def delete_last(self):
        if self.is_empty():
            raise EmptyError('deque is empty')
        return self._delete(self._trailer.prev)


if __name__ == '__main__':
    q = LinkedDeque()


