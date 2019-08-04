# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 
#
from abc import abstractmethod
from BaseTree import Tree


class BinaryTree(Tree):
    """一个二叉树的抽象基类"""

    @abstractmethod
    def left(self, p):
        """返回p的左孩子，如果没有则返回None"""

    @abstractmethod
    def right(self, p):
        """返回p的右孩子，如果没有则返回None"""

    def sibling(self, p):
        """返回p的兄弟结点"""
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """生成一个p的子结点的迭代"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)



