#!/usr/bin/env python
# -*- coding: utf-8 -*-


def subarray_sum_equals_k(nums, k):
    """
    给定一个数组，请找到一个连续子数组加和等于给定目标数值，并找到这样的子数组的总数（即有多少个子数组满足这样的条件）
    :param nums: List[int]
    :param target: int
    :return: int
    """
    l = len(nums)
    res = 0
    for i in range(l):
        tmp = 0
        for j in range(i, l):
            tmp += nums[j]
            if tmp == k:
                res += 1
    return res


def subarray_sum_equals_k1(nums, k):
    l = len(nums)
    res = 0
    sum_t = [0] * (l+1)
    for i in range(1, l+1):
        sum_t[i] = sum_t[i - 1] + nums[i-1]
    for i in range(l):
        for j in range(i, l):
            if sum_t[j + 1] - sum_t[i] == k:
                res += 1
    return res


def subarray_sum_equals_k2(nums, k):
    l = len(nums)
    res = 0
    m = {0: 1}
    sum = 0
    for i in range(l):  # 以当前元素结尾的子数组的和
        sum += nums[i]
        res += m.get(sum - k, 0)
        if sum not in m:
            m[sum] = 1
        else:
            m[sum] += 1
    return res


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum_equals_k2(nums, k))