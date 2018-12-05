# -*- coding: utf-8 -*-
# Created by linxin on 2018/12/5
# Copyright (c) 2018 linxin. All rights reserved.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # ----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.root = TreeNode(3)
        self.root.left = TreeNode(9)
        rn = TreeNode(20)
        self.root.right = rn

        rn.left = TreeNode(15)
        rn.right = TreeNode(7)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        re = []
        que = [root]
        if not root:
            return re

        while que:
            cur_level = []
            next_level = []
            for n in que:
                cur_level.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            que = next_level
            if len(re) % 2 > 0:
                cur_level.reverse()
            re.append(cur_level)

        return re

if __name__ == '__main__':
    t = Solution()

    r = t.zigzagLevelOrder(t.root)
    print(r)