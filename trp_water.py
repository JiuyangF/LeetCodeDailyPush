from copy import deepcopy

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height):
    sum_water = 0
    size = len(height)
    for i in range(size):
        max_left = 0
        max_right = 0
        for j in range(0, i + 1):
            max_left = max(max_left, height[j])
        for j in range(i, size):
            max_right = max(max_right, height[j])
        sum_water += min(max_left, max_right) - height[i]
    return sum_water


def trap_water_dy():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sum_water = 0
    size = len(height)
    max_left_lsit = [None]*size
    max_left_lsit[0] = height[0]
    max_right_list = [None]*size
    max_right_list[-1] = height[-1]

    for i in range(1, size):
        max_left_lsit[i] = max(height[i], max_left_lsit[i - 1])

    for i in range(size-1):
        max_right_list[size - 2 - i] = max(height[size - 2 - i], max_right_list[size - i - 1])

    for i in range(size):
        sum_water += min(max_left_lsit[i], max_right_list[i]) - height[i]
    return sum_water


def trap_two_point():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    left = 0
    right = len(height) - 1
    ans = 0
    left_max = 0
    right_max = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            ans += (left_max - height[left])
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            ans += (right_max - height[right])
            right -= 1
    return ans


def fab(n):
    # 终止条件 边界
    if n <= 2:
        return 1
    else:
        # 最优子结构 状态转移公式
        return fab(n - 1) + fab(n - 2)


# 记录已经计算过得 值
dict_fab = {}


def fab_2(n):
    # 终止条件 边界
    if n <= 2:
        return 1
    elif dict_fab.get(n):
        return dict_fab.get(n)
    else:
        # 最优子结构 状态转移公式
        dict_fab[n] = fab_2(n - 1) + fab_2(n - 2)
        return dict_fab[n]


# 最终优化 动态规划  （大问题化成若干相同类型的子问题 然后一个个解决子问题）
def fab_3(n):
    # 由前往后推
    a = 1
    b = 1
    if n <= 2:
        print('fab({})={}'.format(n, b))
        return 1
    for i in range(n - 2):
        print(a, b)
        a, b = b, a + b
    print('fab({})={}'.format(n, b))
    return b


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def fact_1(n):
    if n == 1:
        return n
    return n * fact(n - 1)


# print(fact(5))
# print(fact(1000))

if __name__ == '__main__':
    # print(trap(height))
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_water_dy())
    print(trap_two_point())
