# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/1
# Copyright (c) 2018 linxin. All rights reserved.


class Solution:
    @classmethod
    def letterCasePermutation(cls, s):
        """
        :type s: str
        :rtype: List[str]
        """
        all_str = [s]
        d = {}

        for i in range(len(s)):
            c = s[i]
            if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')):
                d[i] = s[i]
                for new_s in all_str[:]:
                    all_str.append(cls.upper_lower_exchange(new_s, i))

        print(all_str)
        return all_str

    # ----------------------------------------------------------------------
    @classmethod
    def upper_lower_exchange(cls, s, k):
        """"""
        v = s[k]
        new_v = v.lower() if v.isupper() else v.upper()
        new_str2 = s[:k] + new_v + s[k + 1:]

        return new_str2


if __name__ == '__main__':
    Solution.letterCasePermutation('a1bc')
    Solution.letterCasePermutation('a1b2')
    Solution.letterCasePermutation('1a2b')
    Solution.letterCasePermutation('1a2b3c')
    Solution.letterCasePermutation('12345')
