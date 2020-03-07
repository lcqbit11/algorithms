#!/usr/bin/env python
# -*- coding: utf-8 -*-


def containerMostWater(nums):
    """
    给定一个非负的整数数组，每个元素表示其在横轴上的高度，请找到两个元素，他们和横轴组成的容器的面积最大，并返回最大的面积。
    :param nums: List[int]
    :return: int
    """
    left = 0
    right = len(nums) - 1
    res = 0
    while left < right:
        res = max(res, (right - left)*min(nums[left], nums[right]))
        if nums[left] >= nums[right]:
            right -= 1
        else:
            left += 1
    return res


if __name__ == "__main__":
    nums = [1,8,6,2,5,4,8,3,7]
    print(containerMostWater(nums))