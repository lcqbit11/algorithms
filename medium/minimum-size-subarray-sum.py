#!/usr/bin/env python
# -*- coding: utf-8 -*-


def minimum_size_sub_array_sum(nums, target):
    """
    给定一个长度为n的正整数数组和一个正整数s，请找到一个加和>=s的连续子数组的最小长度，如果没有则返回0。
    :param nums: List[int]
    :param target: int
    :return: int
    """
    # j, sum = 0, 0
    # ans = float("inf")
    # for i in range(len(nums)):
    #     while j < len(nums) and sum < target:
    #         sum += nums[j]
    #         j += 1
    #     if sum >= target:
    #         ans = min(ans, j-i)
    #     sum -= nums[i]
    #
    # return ans if ans != float("inf") else 0

    start, sum = 0, 0
    ans = float("inf")
    # 两层循环总的的时间复杂度为O(n)，n+n，参考 https://www.cnblogs.com/NickyYe/p/4590699.html
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:  # 根据start的计算次数可以得出：该层的计算最多 len(nums) 次
            ans = min(ans, i-start+1)
            sum -= nums[start]
            start += 1

    return ans if ans != float("inf") else 0


if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    print(minimum_size_sub_array_sum(nums, 7))