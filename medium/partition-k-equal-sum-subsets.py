#!/usr/bin/env python
# -*- coding: utf-8 -*-


def partition_k_equal_sum_subsets(nums, k):
    """
    给定一个整数数组和一个正整数k，请判断是否能将该数组分成k份非空子数组，且每个子数组中的所有元素加和都相等。
    :param nums: List[int]
    :param k: int
    :return: bool
    """
    def helper(nums, k, target, start, cur_sum, visited):
        if k == 1:
            return True
        if cur_sum > target:
            return False
        if cur_sum == target:
            return helper(nums, k-1, target, 0, 0, visited)
        for i in range(start, len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            if helper(nums, k, target, i + 1, cur_sum + nums[i], visited):
                return True
            visited[i] = False
        return False

    if not nums:
        return False
    sum_nums = sum(nums)
    if sum_nums % k:
        return False
    target = int(sum_nums/k)
    visited = [False] * len(nums)
    nums.sort(reverse=True)
    return helper(nums, k, target, 0, 0, visited)


if __name__ == "__main__":
    # nums = [4, 3, 2, 3, 5, 2, 1]
    # k = 4
    nums = [85,35,40,64,86,45,63,16,5364,110,5653,97,95]
    k = 7
    print(partition_k_equal_sum_subsets(nums, k))