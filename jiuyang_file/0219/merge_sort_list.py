# -*- coding: utf-8 -*-
# @Time    :  11:58 AM
# @Author  : jiuyang
# @File    : merge_sort_list.py


def revers_merge_sort_list(list_1, list_2):
    """倒叙合并数组"""
    list_3 = []
    while list_1:
        if not list_2 or list_1[-1] >= list_2[-1]:
            list_3.append(list_1[-1])
            list_1.pop()
        else:
            list_3.append(list_2[-1])
            list_2.pop()
    for num in list_2[::-1]:
        list_3.append(num)
    return list_3


if __name__ == '__main__':
    list_1 = [4, 6, 25, 26, 39]
    list_2 = [1, 4, 6, 25, 26, 39]
    print(revers_merge_sort_list(list_1, list_2))
