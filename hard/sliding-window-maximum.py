#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sliding_window_maximum(nums, k):
    """
    给定一个数组，滑动窗口大小为k，滑动窗口从最左侧往右开始滑动，
    每次可以看到k个数字，窗口每次向右滑动1个位置，请返回每个窗口内的最大值
    :param nums: List[int]
    :param k: int
    :return: List[int]
    """
    p = []
    res = []
    for i in range(len(nums)):
        while len(p) > 0 and i - p[0][0] >= k:
            del p[0]
        while len(p) > 0 and p[-1][1] <= nums[i]:  # 保留最大的那个，且保持在第一位
            del p[-1]
        # while len(p) > 0 and p[0][1] <= nums[i]:  # 不可行，会超时
        #     del p[0]
        p.append((i, nums[i]))
        if i >= k - 1:
            res.append(p[0][1])

    return res

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sliding_window_maximum(nums, k))