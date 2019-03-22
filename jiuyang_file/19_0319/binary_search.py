# -*- coding: utf-8 -*-
# @Time    :  12:13 PM
# @Author  : jiuyang
# @File    : binary_search.py


# 二分查找:思想，排序后的数组折半处理

def binary_search(nums, key):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            r = mid - 1
        else:
            l = mid + 1
    return 'not find'


if __name__ == '__main__':
    nums = [1, 2, 5, 6, 9, 36, 66, 77]
    print(binary_search(nums, 7))
