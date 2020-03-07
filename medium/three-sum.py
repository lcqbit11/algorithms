#!/usr/bin/env python
# -*- coding: utf-8 -*-


def three_sum(nums):
    """
    给定一个包含n个元素的整数数组，是否包含三个元素a、b、c，满足a+b+c=0？请找出所有满足条件的不重复的三元组。
    :param nums: List[int]
    :return: List[List[int]]
    """
    if not nums:
        return
    res = []
    nums.sort()
    for i, value in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        tmpTarget = 0 - value
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == tmpTarget:
                res.append((value, nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > tmpTarget:
                right -= 1
            else:
                left += 1
    return res


if __name__ == "__main__":
    # nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    nums = [-2, 0, 1, 1, 2]
    print(three_sum(nums))