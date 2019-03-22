# -*- coding: utf-8 -*-
# @Time    :  6:01 PM
# @Author  : jiuyang
# @File    : max_square.py

class Solution(object):
    def __init__(self):
        pass

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        height = len(matrix)
        width = len(matrix[0])

        memo = [[0 for x in range(width)] for y in range(height)]

        ms = 0
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0:
                    memo[i][j] = int(matrix[i][j])
                    if memo[i][j] > ms:
                        ms = memo[i][j]
                elif matrix[i][j] == '1':
                    memo[i][j] = min([memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1]]) + 1
                    if memo[i][j] > ms:
                        ms = memo[i][j]
                else:
                    memo[i][j] = 0
        print(ms)
        return ms*ms


if __name__ == '__main__':
    # m = [
    #     ["1", "1", "1", "0", "0"],
    #     ["1", "1", "1", "0", "0"],
    #     ["1", "1", "1", "1", "1"],
    #     ["0", "1", "1", "1", "1"],
    #     ["0", "1", "1", "0", "1"],
    #     ["0", "1", "1", "1", "1"]
    # ]
    m = [["0", "1", "0", "0"],
         ["1", "0", "0", "1"],
         ["1", "1", "1", "1"],
         ["1", "1", "1", "1"],
         ["0", "1", "1", "1"]
         ]
    # m = [[1, 1, 1, 1, 1, 1, 1, 1,0],
    #      [1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0],]
    # m =  [
    #
    #     # ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
    #     ["1", "1",      "1", "1", "1", "1", "1", "1", "1", "1",      "1", "1", "1"],
    #     ["0", "1",      "1", "1", "1", "1", "1", "1", "1", "1",     "0", "1", "1"],
    #     ["1", "1",      "1", "1", "1", "1", "1", "1", "1", "1",     "0", "1", "0"],
    #     ["0", "0",      "1", "1", "1", "1", "1", "1", "1", "1",     "1", "1", "1"],
    #     ["1", "1",      "1", "1", "1", "1", "1", "1", "1", "1",     "1", "1", "0"],
    #     ["1", "0",      "1", "1", "1", "1", "1", "1", "1", "1",     "1", "1", "1"],
    #     ["1", "0",      "1", "1", "1", "1", "1", "1", "1", "1",     "1", "1", "1"],
    #     ["0", "1",      "1", "1", "1", "1", "1", "1", "1", "1",     "1", "1", "1"],
    #     # ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1"],
    #     # ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    #     # ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
    # ]
    m = [["1"]]

    s = Solution()
    s.maximalSquare(m)
