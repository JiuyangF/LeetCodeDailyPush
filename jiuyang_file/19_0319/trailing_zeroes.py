# -*- coding: utf-8 -*-
# @Time    :  10:37 AM
# @Author  : jiuyang
# @File    : trailing_zeroes.py

class Solution(object):
    def trailingZeroes(self, n):
        """
        The number of trailing
        :type n: int
        :rtype: int
        """
        base = 5
        zeroes_num = 0

        while n >= base:
            zeroes_num += n // base
            base = base * 5
        return zeroes_num


if __name__ == '__main__':
    print(Solution().trailingZeroes(5))
