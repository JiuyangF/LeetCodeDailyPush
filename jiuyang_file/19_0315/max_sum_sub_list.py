# -*- coding: utf-8 -*-
# @Time    :  8:39 PM
# @Author  : jiuyang
# @File    : max_sum_sub_list.py


"""
最大子列和问题
"""


def max_sub_list_sum1(lists):
    max_sub = 0

    for i in range(len(lists)):
        tem_sum = 0
        for j in range(i, len(lists)):
            tem_sum += lists[j]
            if tem_sum >= max_sub:
                max_sub = tem_sum
    return max_sub


def max_sub_list_sum2(lists):
    max_sub, tem_sum = 0, 0
    for i in range(len(lists)):
        tem_sum += lists[i]
        if tem_sum > max_sub:
            max_sub = tem_sum
        elif tem_sum < 0:
            tem_sum = 0
    return max_sub


if __name__ == '__main__':
    s = [-2, 3, 4, 5, 7, -6, 8, - 26, 9, -6, 7, 8]
    print(max_sub_list_sum2(s))
