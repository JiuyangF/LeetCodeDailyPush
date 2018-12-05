# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/13
# Copyright (c) 2018 linxin. All rights reserved.

"""
递归求和
"""

# ----------------------------------------------------------------------
def recursion_sum(n):
    """"""
    if n == 0:
        return 0
    return n + recursion_sum(n - 1)


if __name__ == '__main__':
    print(recursion_sum(0))
    print(recursion_sum(1))
    print(recursion_sum(2))
