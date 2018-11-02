# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(9)
    root.left = TreeNode(20)
