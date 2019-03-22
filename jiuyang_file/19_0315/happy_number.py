# -*- coding: utf-8 -*-
# @Time    :  6:41 PM
# @Author  : jiuyang
# @File    : happy_number.py

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        used_num = set()
        while 1:
            n = sum([int(x) ** 2 for x in str(n)])
            if n == 1:
                return True
            elif n in used_num:
                return False
            used_num.add(n)


if __name__ == '__main__':
    print(Solution().isHappy(0))
