# -*- coding: utf-8 -*-
# @Time    :  10:08 AM
# @Author  : jiuyang
# @File    : find_peak_element.py

class Solution(object):
    def findPeakElement1(self, nums):
        """
        approach 1, linear scan
        in this approach, we use of the fact that two consecutive numbers nums[j] and nums[j+1]
        are never equal. thus, we can traverse over the nums array starting from the beginning.
        Whenever,wo find a number nums[i], wo only need to check id it is larger than the next number nums[i+1]
        for determining if nums[i] is the peak element.
        Time complexity :O(n) We traverse the nums array of size n once only
        Space complexity :O(1) Constant extra space is used
        如果前面一个元素大于后面的元素，则就是peak element 时间复杂度 O(n)
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findPeakElement2(self, nums):
        """
        approach 2 Recursive Binary Search
        Algorithm:
            We can view any given sequence in nums array as alternating ascending and descending
        sequences. By making use of this, and the fact we can return any peak as the result, wo can make
        the requires peak element.
            In case of simple Binary Search, we work on a sorted sequence of numbers and try to find out the
        required number by reducing the search space at every step. In this case, we use a modification of
        this simple Binary Search to our advantage. We start off by finding the middle element, mid from the
        given nums array. if this element happens tobe lying in a descending sequence of numbers. or a local
        falling slope(found by comparing nums[i] to its right neighbour), it means that the peak will always
        lie towards the left of this element. Thus, we reduce the search space to the left of mid(include itself)
        and perform the same process on the left subarray.

        递归二分查找，时间复杂度降到 O(log n)
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        # print(mid)
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        return self.search(nums, mid + 1, r)


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(Solution().findPeakElement2(nums))
