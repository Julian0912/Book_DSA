# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from abc import ABCMeta, abstractmethod


class Tree(metaclass=ABCMeta):
    """树的基类"""

    class Position(metaclass=ABCMeta):
        """一个表示元素位置的基类"""

        @abstractmethod
        def element(self):
            """返回该位置的元素"""

        @abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def get_root(self):
        """返回根节点，如果为空树则返回None"""

    @abstractmethod
    def parent(self, p):
        """返回p的父节点，如果p是根节点则返回None"""

    @abstractmethod
    def num_children(self, p):
        """返回p的子结点总数"""

    @abstractmethod
    def children(self, p):
        """返回一个p的子结点的迭代"""

    @abstractmethod
    def __len__(self):
        """返回树的结点数"""

    def is_root(self, p) -> bool:
        return self.get_root() == p

    def is_leaf(self, p) -> bool:
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def depth(self, p) -> int:
        """返回结点p的深度"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def __base_height(self, p) -> int:
        if self.is_leaf(p):
            return 0
        return 1 + max(self.__base_height(c) for c in self.children(p))

    def height(self, p=None) -> int:
        """返回结点p的高度，默认选择根节点，即树的高度"""
        if p is None:
            p = self.get_root()
        return self.__base_height(p)

    def preorder(self, p=None):
        """先序遍历"""
        if p is None:
            p = self.get_root()
        if p is None:
            return None
        yield p
        for c in self.children(p):
            for other in self.preorder(c):
                yield other

    def postorder(self, p=None):
        """后序遍历"""
        if p is None:
            p = self.get_root()
        if p is None:
            return None
        for c in self.children(p):
            for other in self.postorder(c):
                yield other
        yield p

    # def __subtree_preorder(self, p):
    #     yield p
    #     for c in self.children(p):
    #         for other in self.__subtree_preorder(c):
    #             yield other
    #
    # def preorder(self):
    #     if not self.is_empty():
    #         for p in self.__subtree_preorder(self.get_root()):
    #             yield p
    #
    # def positions(self):
    #     return self.preorder()
    #
    # def __iter__(self):
    #     for p in self.positions():
    #         yield p.element()


