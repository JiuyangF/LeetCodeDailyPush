# -*- coding: utf-8 -*-
# Created by linxin on 2018/10/30
# Copyright (c) 2018 linxin. All rights reserved.


class Solution:
    @classmethod
    def max_profit_one_time(cls, prices):
        """
        交易一次求最大利润
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if not prices:
            return max_profit
        min_price = prices[0]
        for n in prices:
            if n < min_price:
                min_price = n
            else:
                max_profit = max(n - min_price, max_profit)
        return max_profit

    # ----------------------------------------------------------------------
    @classmethod
    def max_profit_more(cls, prices):
        """
        可交易多次 求最大利润
        :param prices:
        :return:
        """
        max_profit = 0
        n = len(prices)

        up_set = [[]]
        down_set = [[]]

        last_state = ''

        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                if last_state == '':
                    last_state = 'up'
                    up_set[-1].append(prices[0])
                    up_set[-1].append(prices[i])
                elif last_state == 'up':
                    up_set[-1].append(prices[i])
                elif last_state == 'down':  # down to up 的 拐点
                    last_state = 'up'
                    up_set.append([prices[i - 1], prices[i]])
            else:
                if last_state == '':
                    last_state = 'down'
                    down_set[-1].append(prices[0])
                    down_set[-1].append(prices[i])
                elif last_state == 'down':
                    down_set[-1].append(prices[i])
                elif last_state == 'up':  # up to down 的拐点
                    down_set.append([prices[i - 1], prices[i]])
                    last_state = 'down'
        # print('up_set', up_set)
        # print('down_set', down_set)

        for s in up_set:
            if s:
                max_profit += s[-1] - s[0]
        print('max_profit:', max_profit)
        return max_profit

    # ----------------------------------------------------------------------
    @classmethod
    def max_profit_more_2(cls, prices):
        """"""

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                p = prices[i] - prices[i - 1]
                max_profit += p

        print('max_profit:', max_profit)
        return max_profit


if __name__ == '__main__':
    Solution.max_profit_more([7, 1, 5, 3, 6, 4])
    Solution.max_profit_more([7, 6, 5, 4, 3, 2, 1])
    Solution.max_profit_more([1, 2, 3, 4, 5, 6, 7])

    print('#' * 20)

    Solution.max_profit_more_2([7, 1, 5, 3, 6, 4])
    Solution.max_profit_more_2([7, 6, 5, 4, 3, 2, 1])
    Solution.max_profit_more_2([1, 2, 3, 4, 5, 6, 7])
