"""
一 、二叉查找树 ：
    1、若它的左子树不为空，则左子树上所有的节点值都小于它的根节点值。

    2、若它的右子树不为空，则右子树上所有的节点值均大于它的根节点值。

    3、它的左右子树也分别可以充当为二叉查找树。

二 、平衡二叉树 左右旋
    平衡二叉树，首先是一棵二叉查找树，但是它满足一点重要的特性：
        每一个结点的左子树和右子树的高度差最多为1。这个高度差限制就完全规避了上述的最坏情况，因此查找、插入和删除的时间复杂度都变成了O(lg n)。
        https://www.jianshu.com/p/3a6650269d39?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
    平衡因子

    旋转方式
    1、左-左型：做右旋。

    2、右-右型：做左旋转。

    3、左-右型：先做左旋，后做右旋。

    4、右-左型：先做右旋，再做左旋。
"""


class Node(object):
    # 节点类
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    """平衡二叉树 """

    def __init__(self):
        self.root = None

    # 左旋
    def left_rotate(self):
        pass

    # 右旋
    def right_rotate(self):
        pass

    # 插入
    def insert(self):
        pass

    # 删除
    def delete_node(self):
        pass
