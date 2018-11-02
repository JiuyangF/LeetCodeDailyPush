# -*- coding: utf-8 -*-
# Created by linxin on 2018/10/31
# Copyright (c) 2018 linxin. All rights reserved.

"""
问题描述

如果我们有面值为1元、2元和5元的硬币若干枚，如何用最少的硬币凑够11元？
(表面上这道题可以用贪心算法，但贪心算法无法保证可以求出解，比如1元换成2元的时候)

我们要抽出动态规划里非常重要的两个概念：状态和状态转移方程。
上文中d(i)表示凑够i元需要的最少硬币数量，我们将它定义为该问题的”状态”， 这个状态是怎么找出来的呢？
我在另一篇文章 动态规划之背包问题(一)中写过： 根据子问题定义状态。你找到子问题，状态也就浮出水面了。
最终我们要求解的问题，可以用这个状态来表示：d(11)，即凑够11元最少需要多少个硬币。

那状态转移方程是什么呢？既然我们用d(i)表示状态，那么状态转移方程自然包含d(i)，
上文中包含状态d(i)的方程是：d(3)=min{d(3-1)+1, d(3-3)+1}。没错， 它就是状态转移方程，描述状态之间是如何转移的。当然，我们要对它抽象一下，

d(i)=min{ d(i-vj)+1 }，其中i-vj >=0，vj表示第j个硬币的面值;

"""

########################################################################
class Solution(object):
    """这是Solution"""

    coins = [1, 2, 5, 10, 20, 50, 100]

    def __init__(self):
        """"""
        pass

    # ----------------------------------------------------------------------
    @classmethod
    def min_coin_number_change(cls, money):
        """动态规划"""
        d = {k: 0 for k in range(money + 1)}
        for m in range(1, money + 1):
            min_coin = m
            for c in cls.coins:
                if c <= m:
                    cm = d[m - c] + 1  # d(i)=min{ d(i-vj)+1 }，其中i-vj >=0，vj表示第j个硬币的面值;
                    if cm < min_coin:
                        min_coin = cm
            d[m] = min_coin

        return d[money]

    # ----------------------------------------------------------------------
    @classmethod
    def tanxin_alg(cls, money):
        """贪心算法"""

        min_count = 0
        for i in range(1, len(cls.coins) + 1):
            c = cls.coins[-i]
            z = money // c
            money = money % c

            min_count += z

        return min_count


if __name__ == '__main__':
    m = 127
    print(Solution.min_coin_number_change(m))
    print(Solution.tanxin_alg(m))
