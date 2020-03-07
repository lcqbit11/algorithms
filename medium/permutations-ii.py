#!/usr/bin/env python
# -*- coding: utf-8 -*-


def permutations_2(nums):
    """
    给定一个可能包含相同整数的数组，返回各个不重复的全排列数组
    :param nums: List[int]
    :return: List[List[int]]
    """
    def fun(nums, path, res):
        if not nums:
            return res.append(path)
        for i in range(0, len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            fun(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    nums.sort()
    res = []
    fun(nums, [], res)

    return res


if __name__ == "__main__":
    nums = [1,2,1]
    print(permutations_2(nums))