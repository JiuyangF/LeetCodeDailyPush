# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/5
# Copyright (c) 2018 linxin. All rights reserved.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


########################################################################
class Solution(object):
    """这是Solution"""

    def __init__(self):
        """"""
        pass

    # ----------------------------------------------------------------------
    def add_Two_Numbers(self, l1, l2):
        """"""

        rn = None
        cur = rn
        step_num = 0
        while l1 or l2:
            m = int(l1.val) if l1 else 0
            n = int(l2.val) if l2 else 0
            r = (m + n + step_num) % 10
            step_num = (m + n + step_num) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if not rn:
                rn = ListNode(r)
                cur = rn
            else:
                ln = ListNode(r)
                cur.next = ln
                cur = ln

        if step_num > 0:
            ln = ListNode(step_num)
            cur.next = ln

        print(self.linked_list_to_str(rn))
        return rn



    # ----------------------------------------------------------------------
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = self.linked_list_to_str(l1)
        s2 = self.linked_list_to_str(l2)

        n = max(len(s1), len(s2))
        s1 = s1.rjust(n, '0')
        s2 = s2.rjust(n, '0')

        rel_val = ''
        step_num = 0
        for i in range(n - 1, -1, -1):
            m = int(s1[i])
            n = int(s2[i])
            r = (m + n) % 10 + step_num
            step_num = (m + n) // 10
            rel_val = str(r) + rel_val

        print(rel_val)
        r = self.str_to_linked_list(rel_val)
        print(self.linked_list_to_str(r))
        return r

    def linked_list_to_str(self, l1):
        s = ''
        while l1:
            s += str(l1.val)
            l1 = l1.next

        return s

    def str_to_linked_list(self, s):
        h = ListNode(None)
        for i in range(1, len(s) + 1):
            c = int(s[-i])
            if -1 == i:
                h.val = c
            else:
                cn = ListNode(c)
                cn.next = h
                h = cn
        return h


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    # l1.next = ListNode(8)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    # l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(4)

    # s.addTwoNumbers(l1, l2)
    s.add_Two_Numbers(l1, l2)
    # s.addTwoNumbers('123456789', '123456789')
