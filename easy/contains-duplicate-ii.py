#!/usr/bin/env python
# -*- coding: utf-8 -*-

def containsDuplicate2(nums, k):
    """
    有一个整型列表，请找出是否有两个元素值相同，且两者的下标相差至多为k
    :param nums: int
    :return: boolen
    """
    m = {}
    for i in range(len(nums)):
        if nums[i] in m and i - m[nums[i]] <= k:
            return True
        else:
            m[nums[i]] = i

    return False


if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    print(containsDuplicate2(nums, 2))