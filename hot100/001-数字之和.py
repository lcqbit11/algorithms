#!/usr/bin/env python
# -*- coding: utf -*-

#
#  给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def two_sum(nums, target):
    lens = len(nums)
    d = dict()
    for i in range(lens):
        d[nums[i]] = i
    for i in range(lens):
        num1 = nums[i]
        num2 = target - num1
        if d.get(num2, -1) >= 0 and d[num2] != i:
            return [i, d[num2]]


def two_sum_2(nums, target):
    d = dict()
    for i, n in enumerate(nums):
        tmp = target - n
        if tmp in d:
            return [d[tmp], i]
        else:
            d[n] = i

    return [-1, -1]


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))
