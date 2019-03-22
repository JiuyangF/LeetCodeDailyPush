# -*- coding: utf-8 -*-
# @Time    :  11:47 AM
# @Author  : jiuyang
# @File    : search_table.py


def find_repeated_num(num_list):
    """基础查找表算法"""
    nums = []  # 数组

    for num in num_list:

        # 如果这个数字在数组中已经存在 则说明重复出现，得到答案
        if num in nums:
            return num
        # 这个数字在数组中不存在 则添加
        else:
            nums.append(num)
    return '未发现重复的数字'


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(find_repeated_num(num_list))
