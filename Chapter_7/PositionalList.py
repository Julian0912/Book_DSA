# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from DoublyLinkedBase import _DoublyLinkedBase
from DoublyLinkedBase import _Node


class Position(object):
    """创建一个位置数据对象封装结点对象"""

    def __init__(self, container, node: _Node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

    def __eq__(self, other):
        return isinstance(other, type(self)) and other.node is self.node

    def __ne__(self, other):
        return not (self == other)


class PositionalList(_DoublyLinkedBase):
    """每当要用到结点对象时，就使用位置数据对象p，
    在使用_validate方法判断p数据类型是否正确的同时，返回其封装的结点对象以供使用"""

    def _validate(self, p: Position):
        if not isinstance(p, Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return Position(self, node)

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p: Position):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p: Position):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # unfinished
    # 书，page185，代码段7-16
