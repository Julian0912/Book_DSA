# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
import ctypes


class DynamicArray(object):
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._array[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = obj  # self._n是长度，其数值在数组中正好是第一个空位置
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._array[j] = self._array[j - 1]
        self._array[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self._array[k] == value:
                for j in range(k, self._n - 1):
                    self._array[j] = self._array[j + 1]
                self._array[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')

    @staticmethod
    def _make_array(c):
        return (c * ctypes.py_object)()

    def _resize(self, c):
        new_a = self._make_array(c)
        for k in range(self._n):
            new_a[k] = self._array[k]
        self._array = new_a
        self._capacity = c
