#!/usr/bin/env python
# -*- coding: utf-8 -*-


def subsets_ii(nums):
    """
    给定一个数组，数组中可能包含重复数字，请返回所有的子数组集合。
    :param nums: List[int]
    :return: List[List[int]]
    """
    def fun(nums, start, path, res, visited):
        res.append(path + [])
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            if i not in visited:
                visited[i] = 1
                fun(nums, i + 1, path + [nums[i]], res, visited)
                del visited[i]
    nums.sort()
    res = []
    visited = {}
    fun(nums, 0, [], res, visited)
    return res


if __name__ == "__main__":
    nums = [1,2,2]
    print(subsets_ii(nums))