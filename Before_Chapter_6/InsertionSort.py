# -*- coding:utf8 -*-
# Author: Julian Black
# Description:
# 插入排序：
#     输入：含有若干个无序元素的列表
#     输出：一个非递减序列
#


def insert_sort(lst: list):
    for i in range(1, len(lst)):
        cur = lst[i]  # 拿出当前元素待比较
        j = i
        while j > 0 and lst[j - 1] > cur:  # 当前一个元素大于当前元素时
            lst[j] = lst[j - 1]  # 把前一个元素移到当前位置
            j -= 1
        lst[j] = cur
