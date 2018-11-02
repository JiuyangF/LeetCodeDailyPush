"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

思路：
用dictionary 存期望得到的数{期望数:期望数的index}（期望数= 目标数-当前数）
循环list 判断期望值是否在 dict 如果存在 则 返回对应的key  否则存期望数，接着找

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict_num = {}
    for key, value in enumerate(nums):
        depand = target - value
        if dict_num.__contains__(depand):
            return dict_num.get(depand), key
        dict_num[value] = key


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
