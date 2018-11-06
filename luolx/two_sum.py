# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/2
# Copyright (c) 2018 linxin. All rights reserved.


# ----------------------------------------------------------------------
def two_sum(nums, target):
    """"""

    dic = {}
    n = len(nums)
    for i in range(n):
        other = target - nums[i]

        if dic.__contains__(other):
            return dic[other], i
        dic[nums[i]] = i


if __name__ == '__main__':
    # print(two_sum([3, 3], 6))
    print(two_sum([1, 3, 5, 2, 4, 6], 6))
