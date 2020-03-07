#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_points_on_a_line(nums):
    """
    给定一个二维平面上的n个点，请找到位于同一条直线上的点的最大数量
    :param nums: List[List[int]]
    :return: int
    """
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    res = 0
    l = len(nums)
    if l <= 1:
        return l
    for i in range(l - 1):
        m = {}
        duplicate = 1
        for j in range(i + 1, l):
            if nums[i][0] == nums[j][0] and nums[i][1] == nums[j][1]:
                duplicate += 1
            else:
                dx = nums[j][0] - nums[i][0]
                dy = nums[j][1] - nums[i][1]
                k = gcd(dx, dy)
                m[(dx / k, dy / k)] = m.get((dx / k, dy / k), 0) + 1
        res = max(res, duplicate)
        for k in m.keys():
            res = max(res, m[k] + duplicate)

    return res


if __name__ == "__main__":
    nums = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(max_points_on_a_line(nums))