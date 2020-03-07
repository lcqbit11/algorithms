#!/usr/bin/env python
# -*- coding: utf-8 -*-


def subsets(nums):
    """
    给定一个没有重复数字的整数数组，请返回其所有可能的子数组。
    :param nums: List[int]
    :return: List[List[int]]
    """
    def backtrack(nums, index, path, res):
        res.append(path)
        [backtrack(nums, i + 1, path + [nums[i]], res) for i in range(index, len(nums))]

    res = []
    backtrack(nums, 0, [], res)

    return res


if __name__ == "__main__":
    nums = [1,2,3]
    print(subsets(nums))
