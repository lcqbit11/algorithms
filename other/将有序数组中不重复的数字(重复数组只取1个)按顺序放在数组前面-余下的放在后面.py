#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fun(nums):
    if not nums:
        return

    l = len(nums)
    res = [nums[0]]
    tmp = []
    for i in range(1, l):
        if nums[i] != nums[i-1]:
            res.append(nums[i])
        else:
            tmp.append(nums[i])
    res.extend(tmp)
    return res


def fun1(nums):
    if not nums:
        return
    l = len(nums)
    start = end = 1
    for i in range(1, l):
        if nums[i] == nums[-1]:
            nums[start], nums[i]
            start = i














if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3, 4, 6, 8, 10, 10, 12, 12, 13]
    print(fun(nums))
