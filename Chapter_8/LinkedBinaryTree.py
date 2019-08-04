# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """二叉树的链式存储结构"""

    class Node(object):
        """非公开"""
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        """公开"""

        def __init__(self, container, node):
            self.container = container  # 合法的位置必须属于此位置列表，即LinkedBinaryTree类
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return isinstance(other, type(self)) and other.node is self.node

    def _validate(self, p):
        """如果p是合法的位置，则返回其封装的结点
        :return: Node
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        """返回一个封装了给定结点的位置实例，如果node为None则返回None"""
        return self.Position(self, node) if node is not None else None
        # 此处给Position类的container形参传的参数是self，即实例本身
        # 即所有合法的位置实例的container必须是LinkedBinaryTree实例

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        """返回一棵树的结点总数"""
        return self.size

    def get_root(self):
        """返回根节点的位置，如果是空树则返回None
        :return: Position
        """
        return self._make_position(self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, e):
        """为空树创建根节点，存储元素e，并返回根节点的位置，如果树非空，抛出异常"""
        if self.root is not None:
            raise ValueError('root exists')
        self.size = 1
        self.root = self.Node(e)
        return self._make_position(self.root)

    def add_left(self, p, e):
        """为p创建左孩子，存储元素e，并返回左孩子位置，如果已有左孩子，抛出异常"""
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('left child exists')
        self.size += 1
        node.left = self.Node(e, node)  # node is its parent
        return self._make_position(node.left)

    def add_right(self, p, e):
        """为p创建右孩子，存储元素e，并返回右孩子位置，如果已有右孩子，抛出异常"""
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('right child exists')
        self.size += 1
        node.right = self.Node(e, node)  # node is its parent
        return self._make_position(node.right)

    def replace(self, p, e):
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        """删除位置p的结点，用其子结点代替，如果有的话；
        返回删除结点存储的元素；
        如果p有两个子结点则抛出异常"""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node.left if node.left else node.right  # might be None
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self.root = child
        else:
            parent = child.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node  # 注销结点node
        return node.element

    def attach(self, p, t1, t2):
        """将树t1和t2连接为p的两个子结点"""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):  # 三棵树的类型必须相同，即同一类的实例
            raise TypeError('tree type must match')
        self.size += len(t1) + len(t2)
        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0


if __name__ == '__main__':
    t = LinkedBinaryTree()
    p_A = t.add_root('A')
    p_B = t.add_left(p_A, 'B')
    p_C = t.add_right(p_A, 'C')
    p_D = t.add_left(p_B, 'D')
    p_G = t.add_left(p_D, 'G')
    p_H = t.add_right(p_D, 'H')
    p_E = t.add_left(p_C, 'E')
    p_F = t.add_right(p_C, 'F')
    p_I = t.add_right(p_E, 'I')
    for pos in t.preorder():
        print(pos.node.element, end='')




